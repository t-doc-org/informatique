% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Fonctions - Introduction

```{exec} python
:name: py-chess
:when: never
:class: hidden
:include: chess.py
moves = []
def deplace(dx, dy): moves.append((dx, dy))
```

## Exercice {num}`exo-py1`

Ecrivez une fonction `deplace_roi(direction)` qui déplace un roi dans la
direction demandée. L'argument `direction` est une chaîne de caractère contenant
l'un des points cardinaux `n`, `ne`, `e`, `se`, `s`, `so`, `o` ou `no`.

La fonction `deplace(dx, dy)` déplace la pièce d'un nombre de cases vers la
gauche (`dx < 0`) ou la droite (`dx > 0`) et / ou le haut (`dy > 0`) ou le bas
(`dy < 0`).

```{exec} python
:name: py-roi
:when: never
:editor:
def deplace_roi(direction):
  x, y = 0, 0
  if 'e' in direction: x = 1
  elif 'o' in direction: x = -1
  if 'n' in direction: y = 1
  elif 's' in direction: y = -1
  deplace(x, y)
```

Utilisez la fonction `deplace_roi()` pour déplacer le roi sur les cases
indiquées, dans l'ordre.

```{exec} python
:after: py-chess py-roi
:then: py-roi-check
:when: load
:editor:
deplace_roi('n')
deplace_roi('se')
deplace_roi('s')
deplace_roi('o')
```

```{exec} python
:name: py-roi-check
:when: never
:class: hidden
await render_and_check(
  Board(3, 3).piece(White.king, 1, 1), moves,
  [(0, 1), (1, -1), (0, -1), (-1, 0)])
```

## Exercice {num}`exo-py1`

Utilisez la fonction `deplace_roi()` pour déplacer le roi sur les cases
indiquées, dans l'ordre. Évitez les répétitions.

```{exec} python
:after: py-chess py-roi
:then: py-roi-2-check
:when: load
:editor:
for i in range(4):
  deplace_roi('e')
for i in range(3):
  deplace_roi('n')
deplace_roi('o')
for i in range(3):
  deplace_roi('so')
```

```{exec} python
:name: py-roi-2-check
:when: never
:class: hidden
await render_and_check(
  Board(5, 4).piece(White.king, 0, 0), moves,
  4 * [(1, 0)] + 3 * [(0, 1)] + [(-1, 0)] + 3 * [(-1, -1)])
```
