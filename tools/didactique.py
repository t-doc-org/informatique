#!/usr/bin/env python
# Copyright 2025 Caroline Blank <caro@c-space.org>
# SPDX-License-Identifier: CC-BY-NC-SA-4.0

import os
import pathlib
import sys
import types

try:
    from tdoc.common import store
    from tdoc.common import util
except ImportError:
    path = pathlib.Path(sys.argv[0])
    import subprocess
    sys.exit(subprocess.run(
        [os.environ.get('TDOC_RUN', path.parent.resolve().parent / 'run.py'),
         'python', path.resolve()] + sys.argv[1:]).returncode)

import datetime
import json
import sqlite3


def main(argv, stdin, stdout, stderr):
    """Program entry point."""
    parser = util.get_arg_parser(stderr)(
        prog=pathlib.Path(argv[0]).name, add_help=False,
        description="Requêtes liées au labo de didactique.")
    root = parser.add_subparsers(title='Sous-commandes', dest='subcommand')
    root.required = True

    arg = parser.add_argument_group("Options").add_argument
    arg('--help', action='help', help="Affiche ce message et termine.")
    arg('--color', dest='color', choices=['auto', 'false', 'true'],
        default='auto',
        help="Contrôle l'utilisation de la couleur (par défaut: %(default)s).")

    p = root.add_parser('details', add_help=False,
                        help="Affiche le détail des sessions.")
    p.set_defaults(handler=cmd_details)
    arg = p.add_argument_group("Options").add_argument
    add_common_args(arg)

    p = root.add_parser('names', add_help=False,
                        help="Liste les noms d'utilisateurs.")
    p.set_defaults(handler=cmd_names)
    arg = p.add_argument_group("Options").add_argument
    add_common_args(arg)

    p = root.add_parser('sessions', add_help=False,
                        help="Liste les sessions.")
    p.set_defaults(handler=cmd_sessions)
    arg = p.add_argument_group("Options").add_argument
    add_common_args(arg)

    p = root.add_parser('stats', add_help=False,
                        help="Calcule des statistiques.")
    p.set_defaults(handler=cmd_stats)
    arg = p.add_argument_group("Options").add_argument
    add_common_args(arg)
    arg('--per', dest='per', choices=['', 'name', 'session'], default='',
        help="Groupe les sessions pour le calcul de statistiques.")

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


def cmd_details(cfg, sessions):
    """Run the "details" command."""
    for i, s in enumerate(sessions.values()):
        if i > 0: cfg.stdout.write("\n")
        s.write(cfg.stdout)


def cmd_names(cfg, sessions):
    """Run the "names" command."""
    names = set(s.name for s in sessions.values())
    for name in sorted(set(s.name for s in sessions.values())):
        cfg.stdout.write(f"{name}\n")


def cmd_sessions(cfg, sessions):
    """Run the "sessions" command."""
    o = cfg.stdout
    for s in sessions.values():
        o.write(f"{o.CYAN}{s.id}{o.NORM} [{s.htime}, name: {s.name}]\n")


def cmd_stats(cfg, sessions):
    """Run the "stats" command."""
    groups = {}
    group = (lambda s: s.name) if cfg.per == 'name' \
            else (lambda s: s.id) if cfg.per == 'session' \
            else (lambda s: '')
    for s in sessions.values():
        groups.setdefault(group(s), []).append(s)
    indent = "  " if cfg.per else ""
    o = cfg.stdout
    for g, ss in sorted(groups.items()):
        if g: o.write(f"{o.CYAN}{g}:{o.NORM}\n")
        st = stats(ss)
        o.write(f"{indent}{o.LWHITE}Sessions:{o.NORM} {len(ss)}, durée "
                f"{st.session_duration.min_mean_max()}\n")
        o.write(f"{indent}{o.LWHITE}Réponses:{o.NORM} {st.answers}, "
                f"correctes: {st.correct_answers}, "
                f"fausses: {st.answers - st.correct_answers}\n")
        o.write(f"{indent}{o.LWHITE}Demandes d'aide:{o.NORM} {st.helps}\n")
        o.write(f"{indent}{o.LWHITE}Score:{o.NORM} {st.score.min_mean_max()} "
                f"[{", ".join(str(sc) for sc in sorted(st.score))}]\n")


def stats(sessions):
    """Compute statistics over a set of sessions."""
    sessions = list(sessions)
    return types.SimpleNamespace(
        session_duration=Sample(s.duration for s in sessions),
        answers=sum(1 if isinstance(e, Correction) else 0
                    for s in sessions for c in s.conversations.values()
                    for e in c.exchanges),
        correct_answers=sum(1 if isinstance(e, Correction) and e.passed else 0
                            for s in sessions for c in s.conversations.values()
                            for e in c.exchanges),
        helps=sum(1 if isinstance(e, Help) else 0
                  for s in sessions for c in s.conversations.values()
                  for e in c.exchanges),
        score=Sample(s.score for s in sessions),
    )


def fmt(v):
    if v is None: return "-"
    if isinstance(v, float): return f"{v:.1f}"
    if isinstance(v, datetime.timedelta):
        return str(v - datetime.timedelta(microseconds=v.microseconds))
    return str(v)


class Sample(list):
    """A statistical sample of values."""
    @property
    def min(self): return min(self)

    @property
    def max(self): return max(self)

    @property
    def mean(self):
        if not self: return
        return sum(self, start=self[0].__class__()) / len(self)

    def min_mean_max(self, fmt=fmt):
        return f"min: {fmt(self.min)}, moy: {fmt(self.mean)}, " \
               f"max: {fmt(self.max)}"


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
                 "/python-1/labo-didactique\\.html(\\?.*)?(#.*)?'")
    if (value := cfg.session) is not None:
        terms.append("session regexp :session")
        params['session'] = value
    if (value := cfg.name) is not None:
        terms.append("data ->> '$.name' regexp :name")
        params['name'] = value

    # Query the database and construct an in-memory data structure.
    with store.Store(cfg.store).connect('mode=ro') as db:
        sessions = {}
        incomplete = set()
        for time, session, data in db.execute(f"""
            select time, session, data from log
            where {' and '.join(terms)}
            order by time;
        """, params):
            time = datetime.datetime.fromtimestamp(time / 1000)
            data = json.loads(data)
            typ = data['type']
            action = data.get('action')
            if typ == 'error':
                et = Error
            elif typ == 'response' and action == 'new':
                et = Question
            elif typ == 'response' and action == 'correct':
                et = Correction
            elif typ == 'response' and action == 'help':
                et = Help
            else:
                cfg.stderr.write(
                    "ATTENTION: Saut d'une entrée de log inconnue "
                    f"[type: {typ}, action: {action}]\n")
                continue
            cid = data['id']
            if (s := sessions.get(session)) is None:
                if (cid != 0 or action != 'new'
                        or len(data['conversation']['messages']) != 2):
                    if session not in incomplete:
                        incomplete.add(session)
                        cfg.stderr.write(
                            "ATTENTION: Saut d'une session incomplète "
                            f"[id: {session}]\n")
                    continue
                s = sessions[session] = Session(session, time, data['name'])
            if (c := s.conversations.get(cid)) is None:
                c = s.conversations[cid] = Conversation(s, time, cid)
            c.exchanges.append(et(c, time, data))
    return sessions


def indented(indent, text):
    """Indent some text."""
    return f"{indent}{indent.join(text.splitlines(True))}"


def last_value(mapping):
    return mapping[next(reversed(mapping))]


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

    @property
    def duration(self):
        return last_value(self.conversations).exchanges[-1].time - self.time

    @property
    def score(self):
        return max(
            e.score + (1 if isinstance(e, Correction) and e.passed else 0)
            for c in self.conversations.values() for e in c.exchanges)


class Conversation:
    """A conversation with the LLM."""
    def __init__(self, session, time, id):
        self.session, self.time, self.id = session, time, id
        self.exchanges = []

    @property
    def htime(self):
        return self.time.isoformat(sep=' ', timespec='seconds')

    def write(self, o, indent):
        o.write(f"{indent}{o.CYAN}Conversation:{o.NORM}"
                f" [{self.htime}, id: {self.id}]\n")
        for e in self.exchanges:
            e.write(o, indent + "  ")


class ConversationEntry:
    """An entry in the conversation with the LLM."""
    def __init__(self, conversation, time, data):
        self.conversation, self.time = conversation, time
        self.action = data['action']
        self.score = data['score']
        self.level = data.get('level', self.score // 2)

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
        return self.time - prev.time


class Error(ConversationEntry):
    """An error returned by the LLM."""
    def __init__(self, conversation, time, data):
        super().__init__(conversation, time, data)
        self.text = data['error'].strip()
        self.code = data.get('code')

    def write(self, o, indent):
        o.write(f"{indent}{o.RED}Erreur du LLM:{o.NORM}"
                f" [{self.htime}, action: {self.action}]\n")
        o.write(f"{indented(indent + "  ", self.text)}\n")
        if self.code is not None:
            o.write(f"{indent}  {o.LWHITE}Code:{o.NORM}\n")
            o.write(f"{indented(indent + "    ", self.code)}\n")


class Question(ConversationEntry):
    """A new question generated by the LLM."""
    def __init__(self, conversation, time, data):
        super().__init__(conversation, time, data)
        self.text = data['conversation']['messages'][-1]['content'].strip()

    def write(self, o, indent):
        elapsed = f"+{fmt(self.elapsed)}, " if self.prev else ""
        o.write(f"{indent}{o.LCYAN}Question:{o.NORM}"
                f" [{elapsed}niveau: {self.level + 1},"
                f" score: {self.score}]\n")
        o.write(f"{indented(indent + "  ", self.text)}\n")


class Correction(ConversationEntry):
    """The LLM response to a request for correcting an answer."""
    def __init__(self, conversation, time, data):
        super().__init__(conversation, time, data)
        self.code = data.get('code', '').rstrip()
        self.text = data['conversation']['messages'][-1]['content'].strip()

    @property
    def passed(self): return self.text == "ok"

    def write(self, o, indent):
        ok = f"{o.LGREEN}OK{o.NORM}" if self.passed else f"{o.LRED}FAUX{o.NORM}"
        o.write(f"{indent}{o.LYELLOW}Correction:{o.NORM}"
                f" [+{fmt(self.elapsed)}, {ok}]\n")
        indent += "  "
        if not self.passed: o.write(f"{indented(indent, self.text)}\n")
        if self.code:
            o.write(f"{indent}{o.LWHITE}Code:{o.NORM}\n")
            o.write(f"{indented(indent + "  ", self.code)}\n")


class Help(ConversationEntry):
    """The LLM response to a help request."""
    def __init__(self, conversation, time, data):
        super().__init__(conversation, time, data)
        self.code = data.get('code', '').rstrip()
        self.text = data['conversation']['messages'][-1]['content'].strip()

    def write(self, o, indent):
        o.write(f"{indent}{o.LMAGENTA}Aide:{o.NORM} [+{fmt(self.elapsed)}]\n")
        indent += "  "
        o.write(f"{indented(indent, self.text)}\n")
        if self.code:
            o.write(f"{indent}{o.LWHITE}Code:{o.NORM}\n")
            o.write(f"{indented(indent + "  ", self.code)}\n")


if __name__ == '__main__':
    try:
        sys.exit(main(sys.argv, sys.stdin, sys.stdout, sys.stderr))
    except SystemExit:
        raise
    except KeyboardInterrupt:
        sys.exit(1)
