% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Fonctions - Introduction

```{exec} python
:name: py-chess
:when: never
:class: hidden
from chess import *
moves = []
def deplace(dx, dy): moves.append((dx, dy))
```

Dans cette partie, vous allez apprendre à déplacer des pièces d'échec. Les
commandes suivantes sont à disposition:
- `aller_nord()` qui déplace la pièce d'une case vers le nord (haut)
- `aller_sud()` qui déplace la pièce d'une case vers le sud (bas)
- `aller_est()` qui déplace la pièce d'une case vers l'est (droite)
- `aller_ouest()` qui déplace la pièce d'une case vers l'ouest (gauche)

```{exec} python
:name: py-deplacements
:when: never
:class: hidden
def aller_nord():
  deplace(0, 1)

def aller_sud():
  deplace(0, -1)

def aller_est():
  deplace(1, 0)

def aller_ouest():
  deplace(-1, 0)
```

```{tip}
:class: dropdown

Aux échecs, chaque pièce se déplace différemment :

- La **tour** se déplace d'un nombre quelconque de cases horizontalement ou
  verticalement.
- Le **roi** se déplace d'une seule case dans toutes les directions.
- La **dame** se déplace d'un nombre quelconque de cases verticalement,
  horizontalement ou en diagonale sans pouvoir sauter une pièce.
- Le **fou** se déplace d'un nombre quelconque de cases en diagonale sans
  pouvoir sauter une pièce.
- Le **cavalier** se déplace en L, c'est-à-dire de deux cases dans une direction
  (horizontalement ou verticalement), puis d'une case perpendiculairement. Il
  est le seul à pouvoir sauter par-dessus une pièce lors de son mouvement.
- Le **pion** avance d'une case à la fois. Il se déplace d'une case en diagonale
  en prenant une pièce adverse. S'il n'a pas encore bougé, il peut avancer de
  deux cases d'un coup, sans pouvoir sauter une pièce.
```

## Exercice {num}`exo-py1-fct`

Écrivez un programme qui déplace la tour sur les cases indiquées, dans l'ordre.
Évitez les répétitions.

```{exec} python
:after: py-chess py-deplacements
:then: py-tour-1-check
:when: load
:editor: bc14c658-6c17-4bb0-a340-17f5cd89b942
# Écrivez le programme ici
```

```{exec} python
:name: py-tour-1-check
:when: never
:class: hidden
await render_and_check(
  Board(5, 4).piece(White.rook, 0, 0), moves,
 3 * [(0, 1)])
```

````{solution}
```{exec} python
:after: py-chess py-deplacements
:then: py-tour-1-check
:editor:
for _ in range(3):
  aller_nord()
```
````

## Exercice {num}`exo-py1-fct`

Écrivez un programme qui déplace la tour sur les cases indiquées, dans l'ordre.
Évitez les répétitions.

```{exec} python
:after: py-chess py-deplacements
:then: py-tour-2-check
:when: load
:editor: de1f184a-7716-4fbc-97c3-3f8dc8e37b26
# Écrivez le programme ici
```

```{exec} python
:name: py-tour-2-check
:when: never
:class: hidden
await render_and_check(
  Board(5, 4).piece(White.rook, 0, 0), moves,
  2 * [(1, 0)] + 3 * [(0, 1)])
```

````{solution}
```{exec} python
:after: py-chess py-deplacements
:then: py-tour-2-check
:editor:
for _ in range(2):
  aller_est()
for _ in range(3):
  aller_nord()
```
````

## Exercice {num}`exo-py1-fct`

Écrivez un programme qui déplace la tour sur les cases indiquées, dans l'ordre.
Évitez les répétitions.

```{exec} python
:after: py-chess py-deplacements
:then: py-tour-3-check
:when: load
:editor: 4efbf6a9-e18e-463a-9a69-8e651706e508
# Écrivez le programme ici
```

```{exec} python
:name: py-tour-3-check
:when: never
:class: hidden
await render_and_check(
  Board(5, 4).piece(White.rook, 0, 0), moves,
  [(4, 0)] + [(0, 2)] + [(-3, 0)])
```

````{solution}
```{exec} python
:after: py-chess py-deplacements
:then: py-tour-3-check
:editor:
for _ in range(4):
  aller_est()
for _ in range(2):
  aller_nord()
for _ in range(3):
  aller_ouest()
```
````

## Exercice {num}`exo-py1-fct`

Écrivez un programme qui déplace le roi sur les cases indiquées, dans l'ordre.
Évitez les répétitions.

```{exec} python
:after: py-chess py-deplacements
:then: py-roi-1-check
:when: load
:editor: c66f739b-be52-4940-b368-d5b9b1c117d3
# Écrivez le programme ici
```

```{exec} python
:name: py-roi-1-check
:when: never
:class: hidden
await render_and_check(
  Board(5, 5).piece(White.king, 0, 0), moves,
  5 * [(1, 1)])
```

````{solution}
```{exec} python
:after: py-chess py-deplacements
:then: py-roi-1-check
:editor:
for _ in range(4):
  aller_est()
  aller_nord()
```
````

## Exercice {num}`exo-py1-fct`

Écrivez un programme qui déplace le roi sur les cases indiquées, dans l'ordre.
Évitez les répétitions.

```{exec} python
:after: py-chess py-deplacements
:then: py-roi-2-check
:when: load
:editor: 33fa19d1-6896-423a-a54f-d61dcf677153
# Écrivez le programme ici
```

```{exec} python
:name: py-roi-2-check
:when: never
:class: hidden
await render_and_check(
  Board(5, 5).piece(White.king, 0, 0), moves,
  2 * [(1, 0)] + [(1, 1)] + [(0, 1)] + [(0, 1)] + [(1, 1)])
```

````{solution}
```{exec} python
:after: py-chess py-deplacements
:then: py-roi-2-check
:editor:
for _ in range(2):
  aller_est()
aller_nord()
aller_nord()
aller_est()
aller_nord()
aller_est()
aller_nord()
```
````

```{important}
En observant le code de l'exercice précédent, on constate qu'il y a des suites
d'instructions qui se répètent. En effet, pour se déplacer en diagonale, il faut
toujours se déplacer une fois vers l'est et une fois vers le nord.

Pour éviter les répétitions d'une suite d'instructions qui ne peuvent pas être
évitées avec une boucle, il est possible de définir de nouvelles fonctions,
comme par exemple `aller_nord_est()`.
```

## Exercice {num}`exo-py1-fct`

Une nouvelle fonction `aller_nord_est()` a été définie.
1. Observez la construction de la définition d'une fonction. Comment définir une
nouvelle fonction?
2. Observez l'appel de la fonction à la ligne 7. Comment appeler une fonction?
3.

```{exec} python
:after: py-chess py-deplacements
:then: py-roi-3-check
:when: load
:editor: 85b69fdf-28f8-410a-b5e7-3114489c1e7b
# Définition de la fonction
def aller_nord_est():
  aller_nord()
  aller_est()

# Appel la fonction aller_nord_est()
aller_nord_est()

# Complétez le programme ici
```

```{exec} python
:name: py-roi-3-check
:when: never
:class: hidden
await render_and_check(
  Board(5, 5).piece(White.king, 0, 0), moves,
  4 * [(1, 1)])
```

````{solution}
```{exec} python
:after: py-chess py-deplacements
:then: py-roi-3-check
:editor:
# Définition de la fonction
def aller_nord_est():
  aller_nord()
  aller_est()

# Appel la fonction aller_nord_est()
aller_nord_est()

# Complétez le programme ici
for _ in range(3):
  aller_nord_est()
```
````


<!-- ## Exercice {num}`exo-py1-fct`

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

## Exercice {num}`exo-py1-fct`

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
 -->
