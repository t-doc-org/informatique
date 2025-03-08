#!/usr/bin/env python
# Copyright 2025 Caroline Blank <caro@c-space.org>
# SPDX-License-Identifier: CC-BY-NC-SA-4.0

import enum
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
         'python', path.resolve()] + sys.argv[1:],
        shell=sys.platform == 'win32').returncode)

import datetime
import json
import re
import sqlite3


@util.main
def main(argv, stdin, stdout, stderr):
    """Program entry point."""
    parser = util.get_arg_parser(stdin, stdout, stderr)(
        prog=pathlib.Path(argv[0]).name,
        description="Requêtes liées au labo de didactique.",
        help_description="Affiche l'aide et termine.")
    root = parser.add_subparsers(title='Sous-commandes')
    root.required = True

    p = root.add_parser('details', help="Affiche le détail des sessions.")
    p.set_defaults(handler=cmd_details)
    add_query_options(p)
    add_common_options(p)

    p = root.add_parser('names', help="Liste les noms d'utilisateurs.")
    p.set_defaults(handler=cmd_names)
    add_query_options(p)
    add_common_options(p)

    p = root.add_parser('sessions', help="Liste les sessions.")
    p.set_defaults(handler=cmd_sessions)
    add_query_options(p)
    add_common_options(p)

    p = root.add_parser('stats', help="Calcule des statistiques.")
    p.set_defaults(handler=cmd_stats)
    arg = p.add_argument
    arg('--per', dest='per', choices=['', 'name', 'session'], default='',
        help="Groupe les sessions pour le calcul de statistiques.")
    add_query_options(p)
    add_common_options(p)

    cfg = parser.parse_args(argv[1:])
    return cfg.handler(cfg, query(cfg))


def add_common_options(parser):
    """Add common options to a parser."""
    arg = parser.add_argument_group("Options communes").add_argument
    arg('--color', dest='color', choices=['auto', 'false', 'true'],
        default='auto',
        help="Contrôle l'utilisation de la couleur (par défaut: %(default)s).")
    arg('--debug', action='store_true', dest='debug',
        help="Active des fonctionnalités de débogage.")


def add_query_options(parser):
    """Add request options to a parser."""
    arg = parser.add_argument_group("Options de base de données").add_argument
    arg('--start', metavar='WHEN', type='timestamp', dest='start', default=None,
        help="Limite la requête aux entrées après WHEN (yyyy-mm-dd HH:MM:SS).")
    arg('--end', metavar='WHEN', type='timestamp', dest='end', default=None,
        help="Limite la requête aux entrées avant WHEN (yyyy-mm-dd HH:MM:SS).")
    arg('--name', metavar='REGEXP', type='regexp', dest='name', default=None,
        help="Limite la requête aux entrées dont le nom correspond à REGEXP.")
    arg('--session', metavar='REGEXP', type='regexp', dest='session',
        default=None,
        help="Limite la requête aux entrées dont l'identifiant de session "
             "correspond à REGEXP.")
    arg('--store', metavar='PATH', type='path', dest='store',
        default='tmp/store.sqlite',
        help="Chemin d'accès de la base de données (par défaut: %(default)s).")


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
    identity = lambda v: v
    sort, group = (sorted, lambda s: s.name) if cfg.per == 'name' \
                  else (identity, identity) if cfg.per == 'session' \
                  else (identity, lambda s: '')
    for s in sessions.values():
        groups.setdefault(group(s), []).append(s)
    indent = "  " if cfg.per else ""
    o = cfg.stdout
    for g, ss in sort(groups.items()):
        if cfg.per == 'name':
            o.write(f"{o.CYAN}{g}{o.NORM}\n")
        elif cfg.per == 'session':
            o.write(f"{o.CYAN}{g.id}{o.NORM} [{g.htime}, name: {g.name}]\n")
        st = stats(ss)
        o.write(f"{indent}{o.LWHITE}Sessions:{o.NORM} {len(ss)}, durée "
                f"{st.session_duration.min_mean_max()}\n")
        outcomes = {outcome.value[2]: count
                    for outcome, count in st.questions.items() if count > 0}
        o.write(f"{indent}{o.LWHITE}Questions:{o.NORM} "
                f"{sum(st.questions.values())}"
                f"{"".join(f", {lab}: {c}" for lab, c in outcomes.items())}\n")
        o.write(f"{indent}{o.LWHITE}Réponses:{o.NORM} {st.answers}, "
                f"correctes: {st.correct_answers}, "
                f"fausses: {st.answers - st.correct_answers}\n")
        o.write(f"{indent}{o.LWHITE}Score:{o.NORM} {st.score.min_mean_max()} "
                f"[{", ".join(str(sc) for sc in sorted(st.score))}]\n")


def stats(sessions):
    """Compute statistics over a set of sessions."""
    sessions = list(sessions)
    return types.SimpleNamespace(
        session_duration=Sample(s.duration for s in sessions),
        questions={o: sum(1 if isinstance(e, Question) and e.outcome == o else 0
                          for s in sessions for c in s.conversations.values()
                          for e in c.exchanges)
                      for o in Outcome},
        answers=sum(1 if isinstance(e, Correction) else 0
                    for s in sessions for c in s.conversations.values()
                    for e in c.exchanges),
        correct_answers=sum(1 if isinstance(e, Correction) and e.passed else 0
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
    if (v := cfg.start) is not None:
        terms.append(":start <= time")
        params['start'] = v.timestamp() * 1000
    if (v := cfg.end) is not None:
        terms.append("time < :end")
        params['end'] = v.timestamp() * 1000
    terms.append("location regexp 'https?://[^/]+(/informatique)?"
                 "/python-1/labo-didactique\\.html(\\?.*)?(#.*)?'")
    if (v := cfg.session) is not None:
        terms.append("session regexp :session")
        params['session'] = v.pattern
    if (v := cfg.name) is not None:
        terms.append("data ->> '$.name' regexp :name")
        params['name'] = v.pattern

    # Query the database and construct an in-memory data structure.
    with store.Store(cfg.store).connect('mode=ro') as db:
        db.create_function(
            'regexp', 2, lambda pat, v: re.fullmatch(pat, v) is not None,
            deterministic=True)
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
        o.write(f"{o.YELLOW}Session:{o.NORM} {o.LWHITE}{self.name}{o.NORM}"
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
    def next(self):
        i = self.conversation.exchanges.index(self)
        return self.conversation.exchanges[i + 1] \
               if i < len(self.conversation.exchanges) - 1 else None

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


class Outcome(enum.Enum):
    SCORED = ('LGREEN', "RÉUSSIE", "réussies")
    CORRECTED = ('LYELLOW', "CORRIGÉE", "corrigées")
    HELP = ('LMAGENTA', "AIDÉE", "aidées")
    ABANDONED = ('MAGENTA', "ABANDONNÉE", "abandonnées")
    ERROR = ('RED', "ERREUR", "erreurs")


class Question(ConversationEntry):
    """A new question generated by the LLM."""
    def __init__(self, conversation, time, data):
        super().__init__(conversation, time, data)
        self.text = data['conversation']['messages'][-1]['content'].strip()

    @property
    def outcome(self):
        fail_seen, e = False, self
        while e := e.next:
            if isinstance(e, Error): return Outcome.ERROR
            elif isinstance(e, Question): return Outcome.ABANDONED
            elif isinstance(e, Correction):
                if e.passed:
                    return Outcome.CORRECTED if fail_seen else Outcome.SCORED
                fail_seen = True
            elif isinstance(e, Help): return Outcome.HELP
        return Outcome.ABANDONED

    def write(self, o, indent):
        elapsed = f"+{fmt(self.elapsed)}, " if self.prev else ""
        color, label = self.outcome.value[:2]
        o.write(f"{indent}{o.LCYAN}Question:{o.NORM}"
                f" [{elapsed}niveau: {self.level + 1},"
                f" score: {self.score}, {getattr(o, color)}{label}{o.NORM}]\n")
        o.write(f"{indented(indent + "  ", self.text)}\n")


class Correction(ConversationEntry):
    """The LLM response to a request for correcting an answer."""
    def __init__(self, conversation, time, data):
        super().__init__(conversation, time, data)
        self.code = data.get('code', '').rstrip()
        self.text = data['conversation']['messages'][-1]['content'].strip()

    @property
    def passed(self): return self.text == "ok" or self.text.endswith("ok")

    def write(self, o, indent):
        ok = f"{o.LGREEN}OK{o.NORM}" if self.passed else f"{o.LRED}FAUX{o.NORM}"
        o.write(f"{indent}{o.LYELLOW}Correction:{o.NORM}"
                f" [+{fmt(self.elapsed)}, {ok}]\n")
        indent += "  "
        if self.text != "ok": o.write(f"{indented(indent, self.text)}\n")
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
    main()
