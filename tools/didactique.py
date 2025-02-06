#!/usr/bin/env python
# Copyright 2025 Caroline Blank <caro@c-space.org>
# SPDX-License-Identifier: CC-BY-NC-SA-4.0

import os
import pathlib
import sys

try:
    from tdoc.common import store
    from tdoc.common import util
except ImportError:
    path = pathlib.Path(sys.argv[0])
    import subprocess
    sys.exit(subprocess.run(
        [os.environ.get('TDOC_RUN', path.parent.resolve().parent / 'run.py'),
         'python', path.resolve()] + sys.argv[1:]).returncode)

import argparse
import datetime
import json
import sqlite3

# TODO: Command "users", computes per-user stats
# TODO: Per-session stats
# TODO: Global stats


def main(argv, stdin, stdout, stderr):
    """Program entry point."""
    class Parser(argparse.ArgumentParser):
        def _print_message(self, message, file=None):
            super()._print_message(message, stderr)
    parser = Parser(prog=pathlib.Path(argv[0]).name, add_help=False,
                    description="Requêtes liées au labo de didactique.")
    root = parser.add_subparsers(title='Sous-commandes', dest='subcommand')
    root.required = True

    arg = parser.add_argument_group("Options").add_argument
    arg('--help', action='help', help="Affiche ce message et termine.")
    arg('--color', dest='color', choices=['auto', 'false', 'true'],
        default='auto',
        help="Contrôle l'utilisation de la couleur (par défaut: %(default)s).")

    p = root.add_parser('sessions', add_help=False, help="Liste les sessions.")
    p.set_defaults(handler=cmd_sessions)
    arg = p.add_argument_group("Options").add_argument
    add_common_args(arg)

    cfg = parser.parse_args(argv[1:])
    color = None if cfg.color == 'auto' else cfg.color == 'true'
    cfg.stdout = util.AnsiStream(stdout, color)
    cfg.stderr = util.AnsiStream(stderr, color)
    if cfg.start is not None:
        cfg.start = datetime.datetime.fromisoformat(cfg.start)
    if cfg.end is not None:
        cfg.end = datetime.datetime.fromisoformat(cfg.end)
    return cfg.handler(cfg, query(cfg))


def add_common_args(arg):
    """Add common options to a parser."""
    arg('--help', action='help', help="Affiche ce message et termine.")
    arg('--start', metavar='WHEN', dest='start', default=None,
        help="Limite la requête aux entrées après WHEN (yyyy-mm-dd HH:MM:SS).")
    arg('--end', metavar='WHEN', dest='end', default=None,
        help="Limite la requête aux entrées avant WHEN (yyyy-mm-dd HH:MM:SS).")
    arg('--name', metavar='REGEXP', dest='name', default=None,
        help="Limite la requête aux entrées dont le nom correspond à REGEXP.")
    arg('--session', metavar='REGEXP', dest='session', default=None,
        help="Limite la requête aux entrées dont l'identifiant de session "
             "correspond à REGEXP.")
    arg('--store', metavar='PATH', dest='store', default='tmp/store.sqlite',
        help="Chemin d'accès de la base de données.")


def cmd_sessions(cfg, sessions):
    """Run the "sessions" command."""
    for i, s in enumerate(sessions.values()):
        if i > 0: cfg.stdout.write("\n")
        s.write(cfg.stdout)


def query(cfg):
    """Query the database, using the user-provided restrictions."""
    terms, params = [], {}
    if (value := cfg.start) is not None:
        terms.append(":start <= time")
        params['start'] = value.timestamp() * 1000
    if (value := cfg.end) is not None:
        terms.append("time < :end")
        params['end'] = value.timestamp() * 1000
    terms.append("location regexp 'https?://[^/]+(/informatique)?"
                 "/python-1/labo-didactique\\.html\\?.*'")
    if (value := cfg.session) is not None:
        terms.append("session regexp :session")
        params['session'] = value
    if (value := cfg.name) is not None:
        terms.append("data ->> '$.name' regexp :name")
        params['name'] = value

    # Query the database and construct an in-memory data structure.
    with store.Store(cfg.store).connect('mode=ro') as db:
        sessions = {}
        for time, session, data in db.execute(f"""
            select time, session, data from log
            where {' and '.join(terms)}
            order by time;
        """, params):
            time = datetime.datetime.fromtimestamp(time / 1000)
            data = json.loads(data)
            cid = data['id']
            typ = data['type']
            action = data.get('action')
            if (s := sessions.get(session)) is None:
                if (cid != 0 or action != 'new'
                        or len(data['conversation']['messages']) != 2):
                    continue  # The start of the session is missing
                s = sessions[session] = Session(session, time, data['name'])
            if (c := s.conversations.get(cid)) is None:
                c = s.conversations[cid] = Conversation(s, time, cid)
            if typ == 'error':
                e = Error(c, time, data)
            elif typ == 'response' and action == 'new':
                e = Question(c, time, data)
            elif typ == 'response' and action == 'correct':
                e = Correction(c, time, data)
            elif typ == 'response' and action == 'help':
                e = Help(c, time, data)
            else:
                cfg.stderr.write(
                    f"ATTENTION: Saut d'une entrée de log [type: {typ},"
                    f" action: {action}]")
                continue
            c.exchanges.append(e)
    return sessions


def indented(indent, text):
    """Indent some text."""
    return f"{indent}{indent.join(text.splitlines(True))}"


def time_delta(dt1, dt2):
    """Return the time delta from dt1 to dt2, without microseconds."""
    delta = dt2 - dt1
    return delta - datetime.timedelta(microseconds=delta.microseconds)


class Session:
    """A training session."""
    def __init__(self, id, time, name):
        self.id, self.time, self.name = id, time, name
        self.conversations = {}

    def write(self, o):
        o.write(f"{o.YELLOW}Session:{o.NORM} {self.name}"
                f" [{self.htime}, id: {self.id}]\n")
        for c in self.conversations.values():
            c.write(o, "  ")

    @property
    def htime(self):
        return self.time.isoformat(sep=' ', timespec='seconds')


class Conversation:
    """A conversation with the LLM."""
    def __init__(self, session, time, id):
        self.session, self.time, self.id = session, time, id
        self.exchanges = []

    def write(self, o, indent):
        o.write(f"{indent}{o.CYAN}Conversation:{o.NORM}"
                f" [{self.htime}, id: {self.id}]\n")
        for e in self.exchanges:
            e.write(o, indent + "  ")

    @property
    def htime(self):
        return self.time.isoformat(sep=' ', timespec='seconds')


class ConversationEntry:
    """An entry in the conversation with the LLM."""
    def __init__(self, conversation, time):
        self.conversation, self.time = conversation, time

    @property
    def htime(self):
        return self.time.isoformat(sep=' ', timespec='seconds')

    @property
    def prev(self):
        i = self.conversation.exchanges.index(self)
        return self.conversation.exchanges[i - 1] if i > 0 else None

    @property
    def elapsed(self):
        if (prev := self.prev) is None: return datetime.timedelta()
        return time_delta(prev.time, self.time)


class Error(ConversationEntry):
    """An error returned by the LLM."""
    def __init__(self, conversation, time, data):
        super().__init__(conversation, time)
        self.text = data['error'].strip()
        self.action = data['action']
        self.code = data.get('code')

    def write(self, o, indent):
        o.write(f"{indent}{o.RED}Erreur du LLM:{o.NORM}"
                f" [{self.htime}, action: {self.action}]\n")
        o.write(f"{indented(indent + "  ", self.text)}\n")
        if self.code is not None:
            o.write(f"{indent}  Code:\n")
            o.write(f"{indented(indent + "    ", self.code)}\n")


class Question(ConversationEntry):
    """A new question generated by the LLM."""
    def __init__(self, conversation, time, data):
        super().__init__(conversation, time)
        self.score = data['score']
        self.level = data.get('level', self.score // 2)
        self.text = data['conversation']['messages'][-1]['content'].strip()

    def write(self, o, indent):
        elapsed = f"+{self.elapsed}, " if self.prev else ""
        o.write(f"{indent}{o.LCYAN}Question:{o.NORM}"
                f" [{elapsed}niveau: {self.level + 1},"
                f" score: {self.score}]\n")
        o.write(f"{indented(indent + "  ", self.text)}\n")


class Correction(ConversationEntry):
    """The LLM response to a request for correcting an answer."""
    def __init__(self, conversation, time, data):
        super().__init__(conversation, time)
        self.code = data.get('code', '').rstrip()
        self.text = data['conversation']['messages'][-1]['content'].strip()

    def write(self, o, indent):
        ok = f"{o.LGREEN}OK{o.NORM}" if self.text == "ok" \
             else f"{o.LRED}FAUX{o.NORM}"
        o.write(f"{indent}{o.LYELLOW}Correction:{o.NORM}"
                f" [+{self.elapsed}, {ok}]\n")
        indent += "  "
        if self.text != "ok": o.write(f"{indented(indent, self.text)}\n")
        if self.code:
            o.write(f"{indent}Code:\n")
            o.write(f"{indented(indent + "  ", self.code)}\n")


class Help(ConversationEntry):
    """The LLM response to a help request."""
    def __init__(self, conversation, time, data):
        super().__init__(conversation, time)
        self.code = data.get('code', '').rstrip()
        self.text = data['conversation']['messages'][-1]['content'].strip()

    def write(self, o, indent):
        o.write(f"{indent}{o.LMAGENTA}Aide:{o.NORM} [+{self.elapsed}]\n")
        indent += "  "
        o.write(f"{indented(indent, self.text)}\n")
        if self.code:
            o.write(f"{indent}Code:\n")
            o.write(f"{indented(indent + "  ", self.code)}\n")


if __name__ == '__main__':
    try:
        sys.exit(main(sys.argv, sys.stdin, sys.stdout, sys.stderr))
    except SystemExit:
        raise
    except KeyboardInterrupt:
        sys.exit(1)
