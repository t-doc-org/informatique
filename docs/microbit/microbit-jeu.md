% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
solutions: remove
```

# Jeu

```{exec} micropython
:name: microbit-reset
:class: hidden
:when: never
from microbit import *
display.clear()
```

Dans cette partie, vous allez programmer un jeu pas à pas.

Le but du jeu est d'atteindre un emplacement donné en partant du centre
de l'écran du micro:bit. Les déplacements s'effectuent au moyen de
l'accéléromètre, comme si vous aviez une boule en équilibre sur l'écran.

## Accéléromètre

Le programme affiche ce que les fonctions `accelerometer.get_x()` et
`accelerometer.get_x()` renvoient. Essayez de comprendre comment cela fonctionne
en inclinant le microbit doucement dans différentes directions.\
Quelles sont les valeurs de x et y quand vous penchez à droite?\
Quelles sont les valeurs de x et y quand vous penchez à gauche?\
Quelles sont les valeurs de x et y quand vous penchez vers l'avant?\
Quelles sont les valeurs de x et y quand vous penchez vers l'arrière?

```{exec} micropython
:after: microbit-reset
:output-style: max-height: 10rem
from microbit import *

while True:
  print("x =", accelerometer.get_x(), "y =", accelerometer.get_y())
  sleep(1000)
```

## Fonctionnalités de base

1.  Le jeu contient quatre variables globales

    `x`: première coordonnée de la position du joueur. Au début du jeu, le joueur
    se trouve au centre de l'écran.

    `y`: deuxième coordonnée de la position du joueur. Au début du jeu, le joueur
    se trouve au centre de l'écran.

    `but_x`: première coordonnée de la position du but à atteindre. Elle est
    déterminée aléatoirement.

    `but_y`: deuxième coordonnée de la position du but à atteindre. Elle est
    déterminée aléatoirement.

    Déclarez et initialisez les quatres variables. Affichez la position du joueur
    avec une intensité maximale et la position du but à atteindre avec une
    intensité faible (par exemple 5).

2.  En utilisant une boucle `while True`, faites en sorte que lorsque vous
    inclinez le micro:bit dans une direction, le pixel se déplace aussi dans
    cette direction.

    Utilisez les valeurs de `accelerometer.get_x()` et `accelerometer.get_y()`.

3.  Après le déplacement, testez

    - si le pixel est sorti des dimensions de l'écran. Dans ce cas, la manche
     est perdue.
    - si le pixel est arrivé au but. Dans ce cas, la manche est gagnée.

    Affichez une image différente pour chacun de ces cas
    (et ajouter une musique).

4.  Afin de pouvoir effectuer plusieurs manches à la suite, créez une fonction
    `nouvelle_manche()` qui va réinitiliser les valeurs des variables
    (positions de l'utilisateur et du but)

5.  Ajoutez un score. Pour gagner une partie, il faut obtenir un score de 3.
    Chaque manche réussie rapporte un point. Une manche perdue remet le score à
    zéro.

## Programmation du jeu

Tout le jeu sera programmé dans cet éditeur. Pensez à tester chaque nouvelle
fonctionnalité avec plusieurs situations différentes.

```{exec} micropython
:after: microbit-reset
:editor: 48dc94ed-0d0c-4e60-95ad-a95b357c807d
from microbit import *

# écrivez le programme ici
```

````{solution}
```{exec} micropython
:after: microbit-reset
from microbit import *
from random import randint
import music

def nouvelle_manche():
    global x, y, but_x, but_y
    x = 2
    y = 2
    but_x = randint(0, 4)
    but_y = randint(0, 4)
    while but_x == x and but_y == y:
      but_x = randint(0, 4)
      but_y = randint(0, 4)

# initialisation des variables
SEUIL_ACC = 100
nouvelle_manche()
score = 0

display.set_pixel(x, y, 9)
display.set_pixel(but_x, but_y, 2)

while True:
  # mise à jour de l'écran
  display.clear()
  display.set_pixel(x, y, 9)          # affiche le joueur
  display.set_pixel(but_x, but_y, 5)  # affiche le but

  # interrogation les capteurs
  ax = accelerometer.get_x()
  ay = accelerometer.get_y()

  # modification la position du joueur
  if ax < -SEUIL_ACC:
    x -= 1
  if ax > SEUIL_ACC:
    x += 1
  if ay < -SEUIL_ACC:
    y -= 1
  if ay > SEUIL_ACC:
    y += 1

  # conditions de défaite
  if x < 0 or x > 4 or y < 0 or y > 4:
    display.show(Image.SAD)
    music.play(music.POWER_DOWN)
    score = 0
    sleep(1000)
    nouvelle_manche()

  # condition de victoire
  elif x == but_x and y == but_y:
    score += 1
    if score >= 3:
      display.show(Image.HAPPY)
      music.play(music.POWER_UP)
      sleep(1000)
      break
    nouvelle_manche()

  sleep(500)

print("Le jeu est terminé!")
```
````

## Améliorations

1.  Quand l'utilisateur appuye sur le bouton A, la partie est mise en pause.
    Pour reprendre la partie, il faut appuyer sur le bouton B.

2.  À chaque nouvelle partie, la vitesse de déplacement doit augmenter.

3.  Trouvez vos propres améliorations ou variantes.

```{exec} micropython
:after: microbit-reset
:editor: 48680cd0-82cb-4c58-a8c7-e6006fbc8414
from microbit import *

# écrivez le programme ici
```

````{solution}
```{exec} micropython
:after: microbit-reset
from microbit import *
from random import randint
import music

def nouvelle_manche():
    global x, y, but_x, but_y
    x = 2
    y = 2
    but_x = randint(0, 4)
    but_y = randint(0, 4)
    while but_x == x and but_y == y:
      but_x = randint(0, 4)
      but_y = randint(0, 4)

# initialisation des variables
SEUIL_ACC = 100
nouvelle_manche()
score = 0
vitesse = 500

display.set_pixel(x, y, 9)
display.set_pixel(but_x, but_y, 2)

while True:
  # mise en pause
  if button_a.is_pressed():
    while True:                  # attend jusqu'à ce que le bouton B soit appuyé
      if button_b.is_pressed():
        break

  # mise à jour de l'écran
  display.clear()
  display.set_pixel(x, y, 9)          # affiche le joueur
  display.set_pixel(but_x, but_y, 5)  # affiche le but

  # interrogation les capteurs
  ax = accelerometer.get_x()
  ay = accelerometer.get_y()

  # modification la position du joueur
  if ax < -SEUIL_ACC:
    x -= 1
  if ax > SEUIL_ACC:
    x += 1
  if ay < -SEUIL_ACC:
    y -= 1
  if ay > SEUIL_ACC:
    y += 1

  # conditions de défaite
  if x < 0 or x > 4 or y < 0 or y > 4:
    display.show(Image.SAD)
    music.play(music.POWER_DOWN)
    score = 0
    sleep(1000)
    nouvelle_manche()

  # condition de victoire
  elif x == but_x and y == but_y:
    score += 1
    if score >= 3:
      display.show(Image.HAPPY)
      music.play(music.POWER_UP)
      sleep(1000)
      score = 0
      vitesse = vitesse - 20
      if vitesse < 200:
        break
    nouvelle_manche()

  sleep(vitesse)

print("Le jeu est terminé!")
```
````

## Nouveau jeu

Imaginez votre propre jeu.

```{exec} micropython
:after: microbit-reset
:editor: c778448a-07ba-4a29-a85c-2f439684b725
from microbit import *

# écrivez le programme ici
```
