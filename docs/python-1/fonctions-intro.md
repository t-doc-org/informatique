% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Fonctions - Introduction

## Déplacement des pièces

Aux échecs, chaque pièce se déplace différemment:

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

```{exec} python
:name: py-chess
:when: never
:class: hidden
from chess import *
moves = []
def deplace(dx, dy): moves.append((dx, dy))
```

```{exec} python
:name: py-deplacements
:when: never
:class: hidden
def nord():
  deplace(0, 1)

def sud():
  deplace(0, -1)

def est():
  deplace(1, 0)

def ouest():
  deplace(-1, 0)
```

```{exec} python
:name: py-deplacements-2
:when: never
:class: hidden
def sud_est():
  deplace(1, -1)

def sud_ouest():
  deplace(-1, -1)

def nord_est():
  deplace(1, 1)

def nord_ouest():
  deplace(-1, 1)
```

## Exercice {nump}`exercice`

1. Essayez de comprendre le programme en comparant le programme et le résultat.
2. Modifiez le programme pour que le roi suive les numéros.

```{exec} python
:after: py-chess py-deplacements
:then: py-roi-1-check
:editor: 9c8a69d8-8540-4864-901c-395277902e53
:when: load
nord()
est()
nord()
nord()
ouest()
```

```{exec} python
:name: py-roi-1-check
:when: never
:class: hidden
await render_and_check(
  Board(5, 4).piece(White.king, 2, 0), moves,
 [(0, 1), (-1, 0), (0, 1), (-1, 0), (0, -1), (0, -1), (1, 0)])
```

````{solution}
```{exec} python
:after: py-chess py-deplacements
:then: py-roi-1-check
for _ in range(2):
  nord()
  ouest()
sud()
sud()
est()
```
````

## Exercice {nump}`exercice`

Écrivez le programme qui permet à la tour de prendre tous les pions noirs en un
minimum de coups.


```{exec} python
:after: py-chess py-deplacements
:then: py-tour-1-check
:editor: 5352b74a-be0a-46e9-966c-e61ed25c766c
:when: load
# Écrivez le programme ici
```

```{exec} python
:name: py-tour-1-check
:when: never
:class: hidden
board = Board(5, 5)
board.piece(Black.pawn, 1, 1)
board.piece(Black.pawn, 2, 1)
board.piece(Black.pawn, 3, 2)
board.piece(Black.pawn, 4, 3)
await render_check_and_take(board.piece(White.rook, 0, 0), moves)
```

````{solution}
```{exec} python
:after: py-chess py-deplacements
:then: py-tour-1-check
est()
nord()
est()
est()
nord()
est()
nord()
```
````

## Exercice {nump}`exercice`

Le programme de l'exercice précédent contient des répétitions de suites
d'instructions (nord() suivi de est()), mais il n'est pas possible d'utiliser
une boucle `for`, car il y a d'autres instructions entre.
La solution est de définir une nouvelle fonction `diagonale()`.

Résolvez l'exercice précédent en appelant la fonction `diagonale` à la place de
répéter du programme.

De cette manière le programme est plus lisible!

```{exec} python
:after: py-chess py-deplacements
:then: py-tour-1-check
:editor: d788a976-e9e5-41ec-83f4-9215b0f62b19
:when: load
# définition de la fonction diagonale
def diagonale():
  est()
  nord()

# appel de la fonction
diagonale()
```

````{solution}
```{exec} python
:after: py-chess py-deplacements
:then: py-tour-1-check
# définition de la fonction diagonal
def diagonale():
  est()
  nord()

# programme principal
diagonale()
est()
diagonale()
diagonale()
```
````


## Exercice {nump}`exercice`

Pour avoir des pièces qui se déplacent vraiment en diagonale comme le roi,
de nouvelles fonctions ont été définies.

1. Essayez de comprendre le programme en comparant le programme et le résultat.
2. Modifiez le programme pour que le roi suive les numéros.

```{exec} python
:after: py-chess py-deplacements py-deplacements-2
:then: py-roi-3-check
:when: load
:editor: e617f139-035e-4af2-b49f-3620f38349e7
nord_ouest()
nord()
nord_est()
sud_ouest()
```

```{exec} python
:name: py-roi-3-check
:when: never
:class: hidden
await render_and_check(
  Board(5, 4).piece(White.king, 2, 0), moves,
  [(0, 1), (1, 1), (1, 1), (0, -1), (0, -1), (0, -1), (-1, 0), (-1, 0), (-1, 1), (-1, 1)])
```

````{solution}
```{exec} python
:after: py-chess py-deplacements py-deplacements-2
:then: py-roi-3-check
nord()
nord_est()
nord_est()
for _ in range(3):
  sud()
ouest()
ouest()
nord_ouest()
nord_ouest()
```
````

## Exercice {nump}`exercice`

Modifiez le programme pour que la tour suive les numéros.

```{exec} python
:after: py-chess py-deplacements
:then: py-tour-2-check
:when: load
:editor: a19e71d9-284c-42e3-885f-a60f918132d7
for _ in range(3):
  nord()
```

```{exec} python
:name: py-tour-2-check
:when: never
:class: hidden
await render_and_check(
  Board(5, 4).piece(White.rook, 0, 0), moves,
  4 * [(1, 0)] + 2 * [(0, 1)] + 3 * [(-1, 0)] + [(0, 1)] + 2 * [(1, 0)])
```

````{solution}
```{exec} python
:after: py-chess py-deplacements py-deplacements-2
:then: py-tour-2-check
for _ in range(4):
  est()
for _ in range(2):
  nord()
for _ in range(3):
  ouest()
nord()
for _ in range(2):
  est()
```
````

## Exercice {nump}`exercice`

On constate qu'il y a beaucoup de répétitions malgré l'utilisation de boucles
`for` et cela ne représente pas réellement le déplacement de la tour qui se
déplace en général de plusieurs cases en un coup.

Il serait mieux de pouvoir indiquer entre parenthèse le nombre de cases
desquelles on veut déplacer la tour. Pour cela, il faut définir une nouvelle
fonction.

1. Définissez de la même manière les autres fonctions `aller_est`, `aller_ouest`
  et `aller_sud`.
2. Résolvez l'exercice précédent en appeler les fonctions.

```{exec} python
:after: py-chess py-deplacements
:then: py-tour-2-check
:when: load
:editor: a64c9b31-40ab-4001-83e3-ddc6b6f53c18
# définition de la fonction aller_nord qui prend le nombre de cases en paramètre
def aller_nord(nb_cases):
  for _ in range(nb_cases):
    nord()

# appel de la fonction pour que le programme effectue l'action demandée
aller_nord(3)
```

````{solution}
```{exec} python
:after: py-chess py-deplacements py-deplacements-2
:then: py-tour-2-check
# définitions des fonctions
def aller_nord(nb_cases):
  for _ in range(nb_cases):
    nord()

def aller_sud(nb_cases):
  for _ in range(nb_cases):
    sud()

def aller_est(nb_cases):
  for _ in range(nb_cases):
    est()

def aller_ouest(nb_cases):
  for _ in range(nb_cases):
    ouest()

# appel de la fonction pour que le programme effectue l'action demandée
aller_est(4)
aller_nord(2)
aller_ouest(3)
aller_nord(1)
aller_est(2)
```
````

```{exec} python
:name: py-deplacements-3
:when: never
:class: hidden
def nord(n):
  deplace(0, n)

def sud(n):
  deplace(0, -n)

def est(n):
  deplace(n, 0)

def ouest(n):
  deplace(-n, 0)
```


## Exercice {nump}`exercice`

En utilisant les fonctions `nord(nb_cases)`, `sud(nb_cases)`, `est(nb_cases)` et
`ouest(nb_cases)`, écrivez le programme pour que la tour prenne tous les pions
noirs en un minimum de coups.

```{exec} python
:after: py-chess py-deplacements-3
:then: py-tour-3-check
:when: load
:editor: 80e4aab5-c336-456f-9b40-c5acd3911445
# Écrivez le programme ici
```

```{exec} python
:name: py-tour-3-check
:when: never
:class: hidden
board = Board(5, 5)
board.piece(Black.pawn, 0, 4)
board.piece(Black.pawn, 3, 4)
board.piece(Black.pawn, 3, 1)
board.piece(Black.pawn, 1, 1)
board.piece(Black.pawn, 1, 3)
board.piece(Black.pawn, 2, 3)
await render_check_and_take(board.piece(White.rook, 0, 0), moves)
```

````{solution}
```{exec} python
:after: py-chess py-deplacements py-deplacements-3
:then: py-tour-3-check
nord(4)
est(3)
sud(3)
ouest(2)
nord(2)
est(1)
```
````

## Exercice {nump}`exercice`

La fonction `deplace(x, y)` a été définie.
1. Essayez de comprendre le programme en comparant le programme et le résultat.
2. Modifiez le programme pour que le roi suive les numéros.


```{exec} python
:after: py-chess
:then: py-dame-1-check
:when: load
:editor: a9e3a33d-87ea-4262-a3b2-4e96bd862fac
deplace(2, 0)
deplace(-4, 4)
deplace(0, -3)
```

```{exec} python
:name: py-dame-1-check
:when: never
:class: hidden
await render_and_check(
  Board(8, 8).piece(White.queen, 5, 0), moves,
  [(0, 4)] + [(-5, 0)] + [(0, -3)] + [(6, 6)])
```

````{solution}
```{exec} python
:after: py-chess
:then: py-dame-1-check
deplace(0, 4)
deplace(-5, 0)
deplace(0, -3)
deplace(6, 6)
```
````

## Exercice {nump}`exercice`

En utilisant la fonction `deplace(x, y)`, définissez une fonction
`deplace_fou(direction, nb_cases)` où le premier paramètre est la direction du
mouvement ("ne", "se", "so" ou "no") et le deuxième est le nombre de cases.


```{exec} python
:after: py-chess
:then: py-fou-1-check
:when: load
:editor: 3177f22c-18e0-4fb0-9de3-1b1e61e9c543
def deplace_fou(direction, nb_cases):
  # Complétez la définition de la fonction
  pass

# programme principale qui déplace le fou en suivant les numéros
deplace_fou("no", 2)

```

```{exec} python
:name: py-fou-1-check
:when: never
:class: hidden
await render_and_check(
  Board(8, 8).piece(White.bishop, 2, 0), moves,
  [(5, 5)] + [(-2, 2)] + [(-5, -5)] + [(1, -1)])
```

````{solution}
```{exec} python
:after: py-chess
:then: py-fou-1-check
def deplace_fou(direction, nb_cases):
  if direction == "ne":
    deplace(nb_cases, nb_cases)
  elif direction == "se":
    deplace(nb_cases, -nb_cases)
  elif direction == "no":
    deplace(-nb_cases, nb_cases)
  elif direction == "so":
    deplace(-nb_cases, -nb_cases)
  else:
    print("direction non valide")

deplace_fou("ne", 5)
deplace_fou("no", 2)
deplace_fou("so", 5)
deplace_fou("se", 1)
```
````

```{exec} python
:name: py-deplacements-fou
:when: never
:class: hidden
def deplace_fou(direction, nb_cases):
  if direction == "ne":
    deplace(nb_cases, nb_cases)
  elif direction == "se":
    deplace(nb_cases, -nb_cases)
  elif direction == "no":
    deplace(-nb_cases, nb_cases)
  elif direction == "so":
    deplace(-nb_cases, -nb_cases)
  else:
    print("direction non valide")
```

## Exercice {nump}`exercice`

En utilisant la fonction `deplace_fou(direction, nb_cases)` définie à l'exercice
précédent, déplace le fou prendre le pion noir.


```{exec} python
:after: py-chess py-deplacements-fou
:then: py-fou-2-check
:when: load
:editor: 455b60ce-403f-4995-9e3f-98f86214fb04
# Écrivez le programme ici

```

```{exec} python
:name: py-fou-2-check
:when: never
:class: hidden
board = Board(8, 8)
board.piece(White.pawn, 4, 1)
board.piece(White.pawn, 5, 4)
board.piece(White.pawn, 3, 4)
board.piece(White.pawn, 2, 3)
board.piece(White.pawn, 4, 1)
board.piece(White.pawn, 6, 5)
board.piece(Black.pawn, 4, 5)
await render_check_and_take(board.piece(White.bishop, 5, 0), moves)
```

````{solution}
```{exec} python
:after: py-chess py-deplacements-fou
:then: py-fou-2-check
deplace_fou("ne", 1)
deplace_fou("no", 2)
deplace_fou("so", 2)
deplace_fou("no", 2)
deplace_fou("ne", 3)
deplace_fou("se", 1)
```
````


## Exercice {nump}`exercice`

En utilisant la fonction `deplace(x, y)`, définissez une fonction
`deplace_roi`. Quels paramètres sont nécessaires?


```{exec} python
:after: py-chess
:then: py-roi-4-check
:when: load
:editor: 8b17e107-454d-48ec-a45e-a626527baa8a
# Écrivez le programme ici


```

```{exec} python
:name: py-roi-4-check
:when: never
:class: hidden
await render_and_check(
  Board(8, 8).piece(White.king, 4, 0), moves,
  [(1, 1)] + [(0, 1)] + [(0, 1)] + [(1, 1)] + [(-1, 1)] + [(0, 1)] + [(-1, -1)] )
```

````{solution}
Le roi se déplaçant toujours d'une seule case, un seul paramètre, la direction
est nécessaire.
```{exec} python
:after: py-chess
:then: py-roi-4-check
def deplace_roi(direction):
  if direction == "n":
    deplace(0, 1)
  elif direction == "s":
    deplace(0, -1)
  elif direction == "e":
    deplace(1, 0)
  elif direction == "o":
    deplace(-1, 0)
  elif direction == "ne":
    deplace(1, 1)
  elif direction == "se":
    deplace(1, -1)
  elif direction == "no":
    deplace(-1, 1)
  elif direction == "so":
    deplace(-1, -1)
  else:
    print("direction non valide")

deplace_roi("ne")
deplace_roi("n")
deplace_roi("n")
deplace_roi("ne")
deplace_roi("no")
deplace_roi("n")
deplace_roi("so")
```
````

## Exercice {nump}`exercice`

En utilisant la fonction `deplace(x, y)`, définissez une fonction
`deplace_cavalier` qui permet depuis le centre d'atteindre chacun des pions
noirs. Quels paramètres sont nécessaires?


```{exec} python
:after: py-chess
:then: py-cavalier-1-check
:when: load
:editor: a3e67fea-d5fb-4f80-8161-c63120091a6f
# Écrivez le programme ici


```

```{exec} python
:name: py-cavalier-1-check
:when: never
:class: hidden
board = Board(8, 8)
board.piece(Black.pawn, 1, 4)
board.piece(Black.pawn, 2, 5)
board.piece(Black.pawn, 4, 5)
board.piece(Black.pawn, 5, 4)
board.piece(Black.pawn, 5, 2)
board.piece(Black.pawn, 4, 1)
board.piece(Black.pawn, 2, 1)
board.piece(Black.pawn, 1, 2)
await render_check_and_take(board.piece(White.knight, 3, 3), moves)
```

````{solution}
Le cavalier se déplaçant toujours du même nombre de cases (2 et 1), un seul
paramètre, la direction est nécessaire.
```{exec} python
:after: py-chess
:then: py-cavalier-1-check
def deplace_cavalier(direction):
  if direction == "ne":
    deplace(1, 2)
  elif direction == "en":
    deplace(2, 1)
  elif direction == "no":
    deplace(-1, 2)
  elif direction == "on":
    deplace(-2, 1)
  elif direction == "se":
    deplace(1, -2)
  elif direction == "es":
    deplace(2, -1)
  elif direction == "so":
    deplace(-1, -2)
  elif direction == "os":
    deplace(-2, -1)
  else:
    print("direction non valide")

deplace_cavalier("on")
deplace_cavalier("es")
deplace_cavalier("no")
deplace_cavalier("se")
deplace_cavalier("ne")
deplace_cavalier("so")
deplace_cavalier("en")
deplace_cavalier("os")
deplace_cavalier("es")
deplace_cavalier("on")
deplace_cavalier("se")
deplace_cavalier("no")
deplace_cavalier("so")
deplace_cavalier("ne")
deplace_cavalier("os")
deplace_cavalier("en")
```
````

```{exec} python
:name: py-deplacements-cavalier
:when: never
:class: hidden
def deplace_cavalier(direction):
  if direction == "ne":
    deplace(1, 2)
  elif direction == "en":
    deplace(2, 1)
  elif direction == "no":
    deplace(-1, 2)
  elif direction == "on":
    deplace(-2, 1)
  elif direction == "se":
    deplace(1, -2)
  elif direction == "es":
    deplace(2, -1)
  elif direction == "so":
    deplace(-1, -2)
  elif direction == "os":
    deplace(-2, -1)
  else:
    print("direction non valide")
```


## Exercice {nump}`exercice`

En utilisant la fonction `deplace_cavalier(direction)` définie à l'exercice
précédent, déplacez le cavalier pour prendre tous les pions noirs en un
minimum de coups.


```{exec} python
:after: py-chess py-deplacements-cavalier
:then: py-cavalier-2-check
:when: load
:editor: 0f472020-c25d-4d14-a443-e647c6c737fe
# Écrivez le programme ici


```

```{exec} python
:name: py-cavalier-2-check
:when: never
:class: hidden
board = Board(8, 8)
board.piece(Black.pawn, 3, 2)
board.piece(Black.pawn, 5, 3)
board.piece(Black.pawn, 4, 5)
board.piece(Black.pawn, 2, 6)
board.piece(Black.pawn, 3, 4)
board.piece(Black.pawn, 5, 5)
board.piece(Black.pawn, 6, 3)
await render_check_and_take(board.piece(White.knight, 2, 0), moves)
```

````{solution}
```{exec} python
:after: py-chess py-deplacements-cavalier
:then: py-cavalier-2-check
deplace_cavalier("ne")
deplace_cavalier("en")
deplace_cavalier("no")
deplace_cavalier("on")
deplace_cavalier("se")
deplace_cavalier("en")
deplace_cavalier("se")
```
````

## Exercice {nump}`exercice`

En utilisant la fonction `deplace(x, y)`, définissez une fonction
`deplace_dame`. Quels paramètres sont nécessaires?


```{exec} python
:after: py-chess
:then: py-dame-2-check
:when: load
:editor: 27976cba-efa5-45db-9a18-9fffaf4ceeb6
# Écrivez le programme ici

```

```{exec} python
:name: py-dame-2-check
:when: never
:class: hidden
await render_and_check(
  Board(8, 8).piece(White.queen, 3, 0), moves,
  [(0, 7)] + [(4, -4)] + [(-2, -2)] + [(-5, 5)] + [(0, -1)])
```

````{solution}
La dame se déplace dans toutes les directions et de plusieurs cases, deux
paramètres sont nécessaires.
```{exec} python
:after: py-chess
:then: py-dame-2-check
def deplace_dame(direction, nb_cases):
  if direction == "n":
    deplace(0, nb_cases)
  elif direction == "s":
    deplace(0, -nb_cases)
  elif direction == "e":
    deplace(nb_cases, 0)
  elif direction == "o":
    deplace(-nb_cases, 0)
  elif direction == "ne":
    deplace(nb_cases, nb_cases)
  elif direction == "se":
    deplace(nb_cases, -nb_cases)
  elif direction == "no":
    deplace(-nb_cases, nb_cases)
  elif direction == "so":
    deplace(-nb_cases, -nb_cases)
  else:
    print("direction non valide")

deplace_dame("n", 7)
deplace_dame("se", 4)
deplace_dame("so", 2)
deplace_dame("no", 5)
deplace_dame("s", 1)
```
````

```{exec} python
:name: py-deplacements-dame
:when: never
:class: hidden
def deplace_dame(direction, nb_cases):
  if direction == "n":
    deplace(0, nb_cases)
  elif direction == "s":
    deplace(0, -nb_cases)
  elif direction == "e":
    deplace(nb_cases, 0)
  elif direction == "o":
    deplace(-nb_cases, 0)
  elif direction == "ne":
    deplace(nb_cases, nb_cases)
  elif direction == "se":
    deplace(nb_cases, -nb_cases)
  elif direction == "no":
    deplace(-nb_cases, nb_cases)
  elif direction == "so":
    deplace(-nb_cases, -nb_cases)
  else:
    print("direction non valide")
```

## Exercice {nump}`exercice`

En utilisant la fonction `deplace_dame(direction, nb_cases)` définie à
l'exercice précédent, déplacez la dame pour prendre tous les pions noirs en un
minimum de coups.

```{exec} python
:after: py-chess py-deplacements-dame
:then: py-dame-3-check
:when: load
:editor: 54d79281-f256-403d-ae1e-64e0f5bd276b
# Écrivez le programme ici

```

```{exec} python
:name: py-dame-3-check
:when: never
:class: hidden
board = Board(8, 8)
board.piece(White.pawn, 0, 1)
board.piece(White.pawn, 1, 2)
board.piece(White.pawn, 2, 2)
board.piece(White.pawn, 3, 1)
board.piece(White.pawn, 4, 3)
board.piece(White.pawn, 5, 1)
board.piece(White.pawn, 6, 1)
board.piece(White.pawn, 7, 1)
board.piece(White.knight, 1, 0)
board.piece(White.knight, 3, 3)
board.piece(White.bishop, 0, 2)
board.piece(White.bishop, 6, 3)
board.piece(White.rook, 0, 0)
board.piece(White.rook, 5, 0)
board.piece(White.king, 6, 0)
board.piece(Black.pawn, 0, 6)
board.piece(Black.pawn, 1, 4)
board.piece(Black.pawn, 5, 4)
board.piece(Black.pawn, 7, 6)
board.piece(Black.pawn, 3, 6)
board.piece(Black.pawn, 0, 3)
await render_check_and_take(board.piece(White.queen, 3, 0), moves)
```

````{solution}
```{exec} python
:after: py-chess py-deplacements-dame
:then: py-dame-3-check
deplace_dame("ne", 1)
deplace_dame("no", 3)
deplace_dame("e", 4)
deplace_dame("ne", 2)
deplace_dame("o", 4)
deplace_dame("so", 3)
deplace_dame("n", 3)
```
````

## Exercice {nump}`exercice`

En utilisant la fonction `deplace_cavalier(direction)` définie à l'exercice
précédent, déplacez le cavalier pour prendre tous les pions noirs en un minimum de coups.


```{exec} python
:after: py-chess py-deplacements-cavalier
:then: py-cavalier-3-check
:when: load
:editor: 09e9312f-e506-4252-9d81-0452340a023e
# Écrivez le programme ici

```

```{exec} python
:name: py-cavalier-3-check
:when: never
:class: hidden
board = Board(4, 4)
board.piece(Black.pawn, 2, 0)
board.piece(Black.pawn, 0, 1)
board.piece(Black.pawn, 1, 1)
board.piece(Black.pawn, 2, 1)
board.piece(Black.pawn, 3, 1)
board.piece(Black.pawn, 0, 2)
board.piece(Black.pawn, 1, 2)
board.piece(Black.pawn, 2, 2)
board.piece(Black.pawn, 3, 2)
board.piece(Black.pawn, 1, 3)
board.piece(Black.pawn, 2, 3)
board.piece(White.rook, 0, 0)
board.piece(White.rook, 0, 3)
board.piece(White.rook, 3, 0)
board.piece(White.rook, 3, 3)
await render_check_and_take(board.piece(White.knight, 1, 0), moves)
```

````{solution}
```{exec} python
:after: py-chess py-deplacements-cavalier
:then: py-cavalier-3-check
deplace_cavalier("ne")
deplace_cavalier("os")
deplace_cavalier("es")
deplace_cavalier("no")
deplace_cavalier("es")
deplace_cavalier("no")
deplace_cavalier("so")
deplace_cavalier("en")
deplace_cavalier("on")
deplace_cavalier("se")
deplace_cavalier("on")
```
````

## Exercice {nump}`exercice`

En utilisant la fonction `deplace_cavalier(direction)` définie à l'exercice
précédent, déplacez le cavalier pour prendre tous les pions noirs en un minimum de coups.

```{exec} python
:after: py-chess py-deplacements-cavalier
:then: py-cavalier-4-check
:when: load
:editor: bcb5a1f2-98ef-4e0d-85f6-c8d4d4e46ea5
# Écrivez le programme ici

```

```{exec} python
:name: py-cavalier-4-check
:when: never
:class: hidden
board = Board(5, 5)
for i in range(5):
  for j in range(5):
    if i != 2 or j != 2:
      board.piece(Black.pawn, i, j)
await render_check_and_take(board.piece(White.knight, 2, 2), moves)
```

<!--
## Exercice {nump}`exercice`

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

## Exercice {nump}`exercice`

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

## Exercice {nump}`exercice`

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

## Exercice {nump}`exercice`

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
En observant le programme de l'exercice précédent, on constate qu'il y a des suites
d'instructions qui se répètent. En effet, pour se déplacer en diagonale, il faut
toujours se déplacer une fois vers l'est et une fois vers le nord.

Pour éviter les répétitions d'une suite d'instructions qui ne peuvent pas être
évitées avec une boucle, il est possible de définir de nouvelles fonctions,
comme par exemple `aller_nord_est()`.
```

## Exercice {nump}`exercice`

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
```` -->

<!--
## Exercice {nump}`exercice`

Écrivez une fonction `deplace_roi(direction)` qui déplace un roi dans la
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

## Exercice {nump}`exercice`

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
``` -->
