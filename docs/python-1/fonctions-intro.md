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

## Exercice {num}`exo-py1-fct`

1. Essayez de comprendre le programme en comparant le code et le résultat.
2. Modifiez le code pour que le roi suive les numéros.

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
:editor:
for _ in range(2):
  nord()
  ouest()
sud()
sud()
est()
```
````

## Exercice {num}`exo-py1-fct`

Le roi peut aussi se déplacer en diagonale.

Écrivez le code qui permet au roi de passer pas chacun de ces numéros dans
l'ordre (Il n'y a pas de "Bravo" qui apparaîtra même si l'exercice est réussi).


```{exec} python
:after: py-chess py-deplacements
:then: py-roi-2-check
:editor: 5352b74a-be0a-46e9-966c-e61ed25c766c
:when: load
# Écrivez le programme ici
```

```{exec} python
:name: py-roi-2-check
:when: never
:class: hidden
await render_and_check(
  Board(8, 6).piece(White.king, 0, 0), moves,
 [(1, 1), (1, 0), (1, 0), (1, 1), (0, 1), (0, 1), (1,1)])
```

````{solution}
```{exec} python
:after: py-chess py-deplacements
:then: py-roi-2-check
:editor:
nord()
est()
est()
est()
nord()
est()
nord()
nord()
nord()
est()
```
````

## Exercice {num}`exo-py1-fct`

Le code de l'exercice précédent contient des répétitions de suites
d'instructions (nord() suivi de est()), mais il n'est pas possible d'utiliser
une boucle `for`, car il y a d'autres instructions entre.
La solution est de définir une nouvelle fonction `diagonale()`.

Résolvez l'exercice précedent en appelant la fonction `diagonale` à la place de
répéter du code (Il n'y a pas de "Bravo" qui apparaîtra même si l'exercice est
réussi).

De cette manière le code est plus lisible!

```{exec} python
:after: py-chess py-deplacements
:then: py-roi-2-check
:editor: d788a976-e9e5-41ec-83f4-9215b0f62b19
:when: load
# définition de la fonction diagonale
def diagonale():
  nord()
  est()

# appel de la fonction
diagonale()
```

````{solution}
```{exec} python
:after: py-chess py-deplacements
:then: py-roi-2-check
:editor:
# définition de la fonction diagonals
def diagonale():
  nord()
  est()

# programme principal
diagonale()
est()
est()
diagonale()
nord()
nord()
diagonale()
```
````


## Exercice {num}`exo-py1-fct`

Pour avoir vraiment des pièces qui se déplacent en diagonale, de nouvelles
fonctions ont été définies.

1. Essayez de comprendre le programme en comparant le code et le résultat.
2. Modifiez le code pour que le roi suive les numéros.

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
:editor:
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

## Exercice {num}`exo-py1-fct`

Modifiez le code pour que la tour suive les numéros.

```{exec} python
:after: py-chess py-deplacements
:then: py-tour-1-check
:when: load
:editor: a19e71d9-284c-42e3-885f-a60f918132d7
for _ in range(3):
  nord()
```

```{exec} python
:name: py-tour-1-check
:when: never
:class: hidden
await render_and_check(
  Board(5, 4).piece(White.rook, 0, 0), moves,
  4 * [(1, 0)] + 3 * [(0, 1)] + 2 * [(-1, 0)])
```

````{solution}
```{exec} python
:after: py-chess py-deplacements py-deplacements-2
:then: py-tour-1-check
:editor:
for _ in range(4):
  est()
for _ in range(3):
  nord()
for _ in range(2):
  ouest()
```
````

## Exercice {num}`exo-py1-fct`

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
:then: py-tour-1-check
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
:then: py-tour-1-check
:editor:
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
aller_nord(3)
aller_ouest(2)
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


## Exercice {num}`exo-py1-fct`

En utilisant les fonctions `nord(nb_cases)`, `sud(nb_cases)`, `est(nb_cases)` et
`ouest(nb_cases)`, écrivez le code pour la tour suive les cases numérotées.

```{exec} python
:after: py-chess py-deplacements-3
:then: py-tour-2-check
:when: load
:editor: 80e4aab5-c336-456f-9b40-c5acd3911445
# Écrivez le programme ici
```

```{exec} python
:name: py-tour-2-check
:when: never
:class: hidden
await render_and_check(
  Board(8, 8).piece(White.rook, 0, 0), moves,
  [(7, 0)] + [(0, 7)] + [(-7, 0)] + [(0, -7)] + [(5, 0)] + [(0, 5)] + [(-5, 0)] + [(0, -5)] + [(3, 0)] + [(0, 3)] + [(-3, 0)] + [(0, -3)])
```

````{solution}
```{exec} python
:after: py-chess py-deplacements py-deplacements-3
:then: py-tour-2-check
:editor:
n = 7
for _ in range(3):
  est(n)
  nord(n)
  ouest(n)
  sud(n)
  n -= 2
```
````

## Exercice {num}`exo-py1-fct`

La fonction `deplace(x, y)` a été définie.
1. Essayez de comprendre le programme en comparant le code et le résultat.
2. Modifiez le code pour que le roi suive les numéros.


```{exec} python
:after: py-chess
:then: py-reine-1-check
:when: load
:editor: a9e3a33d-87ea-4262-a3b2-4e96bd862fac
deplace(2, 0)
deplace(-4, 4)
deplace(0, -3)
```

```{exec} python
:name: py-reine-1-check
:when: never
:class: hidden
await render_and_check(
  Board(8, 8).piece(White.queen, 5, 0), moves,
  [(0, 4)] + [(-5, 0)] + [(0, -3)] + [(6, 6)])
```

````{solution}
```{exec} python
:after: py-chess
:then: py-reine-1-check
:editor:
deplace(0, 4)
deplace(-5, 0)
deplace(0, -3)
deplace(6, 6)
```
````

## Exercice {num}`exo-py1-fct`

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
:editor:
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

## Exercice {num}`exo-py1-fct`

En utilisant la fonction `deplace_fou(direction, nb_cases)` définie à l'exercice
précédent, déplace le fou afin d'aller manger le pion noir.


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
await render_and_check(
  board.piece(White.bishop, 5, 0), moves,
  [(1, 1)] + [(-2, 2)] + [(-2, -2)] + [(-2, 2)] + [(3, 3)] + [(1, -1)])
```

````{solution}
```{exec} python
:after: py-chess
:then: py-fou-2-check
:editor:
# à compléter
```
````


## Exercice {num}`exo-py1-fct`

En utilisant la fonction `deplace(x, y)`, définissez une fonction
`deplace_roi`. Quels paramètres sont nécessaires?


```{exec} python
:after: py-chess
:then: py-roi-4-check
:when: load
:editor: 8b17e107-454d-48ec-a45e-a626527baa8a
# Ecrivez le programme ici


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
:editor:
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

## Exercice {num}`exo-py1-fct`

En utilisant la fonction `deplace(x, y)`, définissez une fonction
`deplace_cavalier` qui permet depuis le centre d'atteindre chacun des pions
noirs. Quels paramètres sont nécessaires?


```{exec} python
:after: py-chess
:then: py-cavalier-1-check
:when: load
:editor: a3e67fea-d5fb-4f80-8161-c63120091a6f
# Ecrivez le programme ici


```

```{exec} python
:name: py-cavalier-1-check
:when: never
:class: hidden
await render_and_check(
  Board(8, 8).piece(White.knight, 3, 3), moves,
  [(-2, 1)] + [(2, -1)] + [(-1, 2)] + [(1, -2)] + [(1, 2)] + [(-1, -2)] + \
  [(2, 1)] + [(-2, -1)] + [(2, -1)] + [(-2, 1)] + [(1, -2)] + [(-1, 2)] + \
  [(-1, -2)] + [(1, -2)] + [(-2, -1)] + [(2, 1)])
```

````{solution}
Le cavalier se déplaçant toujours du même nombre de cases (1 et 2), un seul
paramètre, la direction est nécessaire.
```{exec} python
:after: py-chess
:then: py-cavalier-1-check
:editor:
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


## Exercice {num}`exo-py1-fct`

En utilisant la fonction `deplace_cavalier(direction)`définie à l'exercice
précédent, déplacez le cavalier pour manger tous les pions.


```{exec} python
:after: py-chess py-deplacements-cavalier
:then: py-cavalier-2-check
:when: load
:editor: 4ceaf5be-85ee-4926-9f2d-304441b161c3
# Ecrivez le programme ici


```

```{exec} python
:name: py-cavalier-2-check
:when: never
:class: hidden
await render_and_check(
  Board(8, 8).piece(White.knight, 2, 0), moves,
  [(1, 2)] + [(2, 1)] + [(-1, 2)] + [(-2, 1)] + [(1, -2)] + [(2, 1)] + [(1, -2)])
```

````{solution}
```{exec} python
:after: py-chess py-deplacements-cavalier
:then: py-cavalier-2-check
:editor:
deplace_cavalier("ne")
deplace_cavalier("en")
deplace_cavalier("no")
deplace_cavalier("on")
deplace_cavalier("se")
deplace_cavalier("en")
deplace_cavalier("se")
```
````

## Exercice {num}`exo-py1-fct`

En utilisant la fonction `deplace(x, y)`, définissez une fonction
`deplace_reine`. Quels paramètres sont nécessaires?


```{exec} python
:after: py-chess
:then: py-reine-2-check
:when: load
:editor: 27976cba-efa5-45db-9a18-9fffaf4ceeb6
# Ecrivez le programme ici

```

```{exec} python
:name: py-reine-2-check
:when: never
:class: hidden
await render_and_check(
  Board(8, 8).piece(White.queen, 3, 0), moves,
  [(0, 7)] + [(4, -4)] + [(-2, -2)] + [(-5, 5)] + [(0, -1)])
```

````{solution}
La reine se déplace dans toutes les directions et de plusieurs cases, deux
paramètres sont nécessaires.
```{exec} python
:after: py-chess
:then: py-reine-2-check
:editor:
def deplace_reine(direction, nb_cases):
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

deplace_reine("n", 7)
deplace_reine("se", 4)
deplace_reine("so", 2)
deplace_reine("no", 5)
deplace_reine("s", 1)
```
````

```{exec} python
:name: py-deplacements-reine
:when: never
:class: hidden
def deplace_reine(direction, nb_cases):
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


<!--
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
```` -->

<!--
## Exercice {num}`exo-py1-fct`

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
``` -->
