% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
solutions: dynamic
```

# Labo - Micro:bit

```{exec} micropython
:name: microbit-reset
:class: hidden
:when: never
from microbit import *
display.clear()
```

## Introduction

Le BBC micro:bit est un microcontrôleur développé par la BBC pour encourager la
programmation dans les écoles en Angleterre. Il s'agit d'un mini-ordinateur
programmable notamment en Python. En raison de son prix attractif (~15 CHF), son
utilisation est très répandue.

### Composants du micro:bit

Le micro:bit contient tous les composants essentiels d'un ordinateur, à savoir

- CPU (Central Processing Unit), ou **processeur** qui est le "cerveau" pouvant
  être programmé en Python ou dans un autre langage de programmation. C'est lui
  qui exécute les programmes et pilote tous les autres composants.

- RAM (Random Access Memory) ou **mémoire vive** qui permet de stocker les
  programmes exécutés ainsi que les données traitées par le programme.

- La **carte-mère** qui interconnecte tous les composants entre eux (c'est le
  système nerveux en quelque sorte).

```{figure} images/composants-microbit.png
:alt: Composants du micro:bit
:width: 100%
:align: center
```

```{important}
Faites attention aux points suivants lorsque vous utilisez le micro:bit:

- Le connecteur micro-USB utilisé pour programmer le micro:bit est fragile.
  Ne forcez jamais le câble et manipulez-le en douceur pour connecter
  déconnecter le câble.

- Évitez de toucher les connecteurs (Edge Connectors) et les connecteurs à
  l'arrière. Il arrive parfois qu'on soit chargé en électricité statique
  (très fort voltage), ce qui peut totalement détruire le micro:bit.

- Manipulez de préférence le micro:bit en le tenant par la tranche.
```

### Exécuter un programme

Voici la procédure pour exécuter un programme sur le micro:bit:

1.  Connectez le micro:bit au port USB de l'ordinateur\
    Faites attention à ne pas abîmer le connecter micro USB du micro:bit, car il
    est très fragile. Ne portez pas le microbit par le câble.

2.  Connectez l'éditeur au micro:bit\
    Cliquez sur l'icône **Tools** et sélectionnez **Connect**. Dans la boite de
    dialogue qui s'est ouverte, sélectionnez l'élément proposé et appuyez sur
    **Connexion**.

3.  Exécutez le programme sur le micro:bit\
    Appuyez sur le bouton **Run**.

### Exercice {nump}`exercice`

Le programme suivant affiche un sourire sur la matrice LED 5x5 du micro:bit.\
Exécutez-le sur le micro:bit.

```{exec} micropython
:after: microbit-reset
from microbit import *

smile = Image("00000:09090:00900:90009:09990")
display.show(smile)
```

## Affichage de texte

### Exercice {nump}`exercice`

1.  Exécutez le programme suivant et répondez aux questions:
    - Que fait ce programme?
    - Que fait `display.scroll("Salut!")`?
    - Que fait `sleep(2000)`?

2.  Modifiez le programme pour qu'il affiche 4 fois "Salut!".

```{exec} micropython
:after: microbit-reset
:editor:
from microbit import *

display.scroll("Salut!")
sleep(2000)
display.scroll("Comment vas-tu?")
```

````{solution}
```{exec} micropython
:after: microbit-reset
from microbit import *

for _ in range(4):
    display.scroll("Salut!")
    sleep(2000)
```
````

## Affichage d'image

### Image matricielle

Une image matricielle ou bitmap est une image composée de pixels de couleur. Dans
le cas du micro:bit, chaque pixel est représenté par une LED qui peut être
allumée ou éteinte, ce qui correspond à un dessin en noir et blanc.

```{figure} images/heart-microbit.png
:alt: Image matricielle
:align: center
:width: 70%
```

Il est donc possible de créer ses propres images ainsi:

```{exec} micropython
:when: never
img = Image("09090:"
            "99999:"
            "99999:"
            "09990:"
            "00900")
```

Le **module microbit** contient de nombreuses images intégrées, telles que
`Image.HEART`, `Image.HEART_SMALL`, `Image.HAPPY`, `Image.SAD`,
`Image.PACMAN`, `Image.GHOST`, `Image.SKULL`, etc.

### Exercice {nump}`exercice`

1.  Sans l'exécuter, que fait le programme suivant?
    ```{exec} micropython
    :after: microbit-reset
    :editor:
    from microbit import *

    img = Image("00000:"
                "09990:"
                "09090:"
                "09990:"
                "00000")

    display.show(img)
    ```

2.  Exécutez le programme sur le micro:bit pour vérifier votre réponse.
3.  Modifiez le programme ci-dessus pour afficher une croix sur le microbit.

````{solution}
```{exec} micropython
:after: microbit-reset
from microbit import *

img = Image("90009:"
            "09090:"
            "00900:"
            "09090:"
            "90009")

display.show(img)
```
````

### Exercice {nump}`exercice`

1.  Écrivez un programme qui affiche l'image de pacman, attend 2 secondes et
    ensuite affiche l'image d'un fantôme.

2.  Modifiez le programme de la partie 1 pour qu'il change d'images toute les
    secondes en continu.
    ````{tip}
    :class: dropdown
    Pour faire défiler les images de manière continue, on utilise une boucle
    `while`. Cette boucle s'exécute tant que la condition reste vraie. En
    écrivant `while True`, on crée une boucle infinie, c’est-à-dire qu'elle
    s'exécutera sans fin, sauf si on l’interrompt manuellement.

    ```{exec} python
    :when: never
    # Ce code va afficher le texte sans s'arrêter
    while True:
        print("Bonjour !")
    ```
    ````

```{exec} micropython
:after: microbit-reset
:editor: 7371706b-13af-4bbd-961c-d6b9fff172e3
from microbit import *

# écrivez le programme ici
```

````{solution}
1.  ```{exec} micropython
    :after: microbit-reset
    from microbit import *

    display.show(Image.PACMAN)    # affiche l'image de pacman
    sleep(2000)                   # attend 2 secondes
    display.show(Image.GHOST)     # affiche l'image du fantôme
    ```
2.  ```{exec} micropython
    :after: microbit-reset
    from microbit import *

    while True:
      display.show(Image.PACMAN)  # affiche l'image de pacman
      sleep(1000)                 # attend une seconde
      display.show(Image.GHOST)   # affiche l'image du fantôme
      sleep(1000)                 # attend une seconde
    ```
````

## Utilisation des boutons A et B

Le micro:bit contient deux boutons A et B sur sa face avant. Lorsqu'un bouton
est appuyé, une action se produira dans votre programme.

La fonction `was_pressed()` retourne la value `True` si le bouton a été
enfoncé depuis le début du programme ou depuis le dernier appel de cette
fonction.

### Exemple {nump}`exemple`

```{exec} micropython
:after: microbit-reset
:console-style: max-height: 10rem
from microbit import *

while True:
  if button_a.was_pressed():
    print("Le bouton A a été appuyé.")
  elif button_b.was_pressed():
    print("Le bouton B a été appuyé.")
  else:
    print("Aucun bouton n'a été appuyé.")
  sleep(1000)
```

### Exercice {nump}`exercice`

Écrivez un programme qui affiche une image lorsque le bouton A est appuyé et
affiche une autre image lorsque c'est le bouton B.

```{exec} micropython
:after: microbit-reset
:editor: f75832f8-7b90-43c5-b767-c94bd144ff9c
from microbit import *

# écrivez le programme ici
```

````{solution}
```{exec} micropython
:after: microbit-reset
from microbit import *

while True:
    if button_a.was_pressed():
        display.show(Image.HAPPY)
    elif button_b.was_pressed():
        display.show(Image.SAD)
    sleep(1000)
```
````

### Exercice {nump}`exercice`

Testez les deux programmes suivants.
- Quelles différences y a-t-il entre les deux programmes?
- Que fait la fonction `is_pressed()`?

```{exec} micropython
:after: microbit-reset
from microbit import *

while True:
    if button_a.was_pressed():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
    sleep(200)
```

```{exec} micropython
:after: microbit-reset
from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
    sleep(200)
````

```{solution}
La fonction `was_pressed()` détecte lorsque le bouton a été appuyé une
fois et effectue le bloc d'instructions. Si on laisse le bouton appuyé,
le bloc d'instructions ne sera effectué qu'une seule fois.

La fonction `is_pressed()` détecte lorsque le bouton est enfoncé et
effectue le bloc d'instructions tant que celui-ci est enfoncé.
```

## Changement d'état d'un pixel

Un pixel est un point dans une image. Sur le micro:bit un pixel est représenté
par une LED qui a une coordonnée x et y. La coordonnée (0, 0) se trouve en haut
à gauche de l'image.

```{figure} images/pixel-microbit.png
:alt: leds du microbit
:align: center
:width: 30%
```

La fonction `display.set_pixel(x, y, intensite)` permet d'appliquer la valeur de
l'**intensité** à la LED de coordonnée (x, y). L'intensité est un nombre entre
0 et 9 où 0 signifie que la LED est éteinte et 9 la luminosité maximale.

### Exercice {nump}`exercice`

Écrivez un programme qui allume la LED du milieu de l'image avec la valeur
maximale et les LED des quatre coins avec une valeur intermédiaire.

```{exec} micropython
:after: microbit-reset
:editor: 5c2ee4bf-d7e1-4cbf-b3eb-af285d595b65
from microbit import *

# écrivez le programme ici
```

````{solution}
```{exec} micropython
:after: microbit-reset
from microbit import *

display.set_pixel(2, 2, 9)
display.set_pixel(0, 0, 5)
display.set_pixel(4, 0, 5)
display.set_pixel(0, 4, 5)
display.set_pixel(4, 4, 5)
```
````

## Exercice {nump}`exercice`

1.  Écrivez un programme qui affiche un décompte: 9, 8, ... et lorsque le
    compteur est arrivé à 0, affichez "BOOM" suivi de l'image d'un crâne.
    (Image.SKULL).

2.  Ajoutez un son après l'affichage du crâne.
    ```{tip}
    Le micro:bit permet d'ajouter des sons. Voir le site officiel
    [microbit.org](https://python.microbit.org/v/3/reference/sound) pour les
    détails.
    ```

```{exec} micropython
:after: microbit-reset
:editor: 19595626-3460-4a8f-87e0-1ea19608c46d
from microbit import *

# écrivez le programme ici
```

````{solution}
```{exec} micropython
:after: microbit-reset
from microbit import *
import music

compteur = 9
while compteur > 0:
  display.show(compteur)
  compteur -= 1
  sleep(1000)
display.scroll("BOOM")
display.show(Image.SKULL)
music.play(music.POWER_DOWN)
```
````

## Exercice {nump}`exercice`

Écrivez un programme qui:

- allume le pixel du centre de l'écran,
- si l'utilisateur appuie sur le bouton A, le pixel se déplace à gauche,
- si l'utilisateur appuie sur le bouton B, le pixel se déplace à droite,
- si le pixel est au bord de l'écran, il ne se passe rien.

```{tip}
La fonction `display.clear()` permet d'effacer tout l'écran, c'est-à-dire
éteindre toutes les LED.
```

```{exec} micropython
:after: microbit-reset
:editor: bc25d9aa-1607-434c-ad45-9996b601a080
from microbit import *

# écrivez le programme ici
```

````{solution}
```{exec} micropython
:after: microbit-reset
from microbit import *

x = 2
y = 2
display.set_pixel(x, y, 9)
while True:
    if button_a.was_pressed():
        if x != 0:
            x -= 1
    elif button_b.was_pressed():
        if x != 4:
            x +=  1
    display.clear()
    display.set_pixel(x, y, 9)
    sleep(200)
```
````

## Exercice {nump}`exercice`

1.  Écrivez un programme qui simule un lancer de dé, c'est-à-dire que lorsque
    vous secouez le micro:bit, un nombre aléatoire entre 1 et 6 doit s'afficher.

2.  Modifiez le programme de la partie 1 pour qu'il affiche la valeur obtenue
    comme sur un dé: &#9856; &#9857; &#9858; &#9859; &#9860; et &#9861;.

```{tip}
Le micro:bit contient un accéléromètre qui permet de connaître sa position,
ainsi que ses mouvements. La fonction `accelerometer.was_gesture('shake')`
renvoie `True` si le micro:bit a été secoué.
```

```{exec} micropython
:after: microbit-reset
:editor: b2c3b835-b497-4e25-9871-d3d756bb6862
from microbit import *

# écrivez le programme ici
```

````{solution}
1.  ```{exec} micropython
    :after: microbit-reset
    from microbit import *
    from random import randint

    while True:
      if accelerometer.was_gesture('shake'):
        display.show(randint(1, 6))
    ```
2.  ```{exec} micropython
    :after: microbit-reset
    from microbit import *
    from random import randint

    while True:
      if accelerometer.was_gesture('shake'):
        n = randint(1, 6)
        if n == 1:
          display.show(Image("00000:00000:00900:00000:00000"))
        elif n == 2:
          display.show(Image("90000:00000:00000:00000:00009"))
        elif n == 3:
          display.show(Image("90000:00000:00900:00000:00009"))
        elif n == 4:
          display.show(Image("90009:00000:00000:00000:90009"))
        elif n == 5:
          display.show(Image("90009:00000:00900:00000:90009"))
        elif n == 6:
          display.show(Image("90009:00000:90009:00000:90009"))
    ```
````

## Exercice {nump}`exercice`

Écrivez un programme qui mesure votre temps de réaction en secondes.

1.  Des images d'animaux défilent aléatoirement sur l'écran. (`Image.RABBIT`,
    `Image.COW`, `Image.TORTOISE`, `Image.DUCK`, `Image.SNAKE`,
    `Image.BUTTERFLY`, `Image.GIRAFFE`)

2.  Lorsqu'une flèche vers la droite `Image.ARROW_E` apparaît, il faut appuyer
    le plus rapidement possible sur le bouton B. Le temps de réaction sera
    calculé et affiché.

3.  Ajoutez une difficulté supplémentaire:\
    Lorsqu'une flèche vers la gauche `Image.ARROW_W` apparaît, il faut appuyer
    sur le bouton A.

```{tip}
La fonction `running_time()` renvoie le nombre de millisecondes depuis le
démarrage du micro:bit.
```

```{exec} micropython
:after: microbit-reset
:editor: 5c335679-263a-4f68-b264-b0d4015582e7
from microbit import *

# écrivez le programme ici
```

````{solution}
```{exec} micropython
:after: microbit-reset
from microbit import *
from random import randint

while True:
  nombre = randint(1, 32)
  if nombre <= 5:
    display.show(Image.RABBIT)
  elif nombre <= 10:
    display.show(Image.COW)
  elif nombre <= 15:
    display.show(Image.TORTOISE)
  elif nombre <= 20:
    display.show(Image.DUCK)
  elif nombre <= 25:
    display.show(Image.BUTTERFLY)
  elif nombre <= 30:
    display.show(Image.SNAKE)
  elif nombre == 31:
    display.show(Image.ARROW_E)
    debut = running_time()
    while True:
      if button_b.was_pressed():
        fin = running_time()
        break
    temps_ecoule = (fin - debut)/1000
    display.scroll(temps_ecoule)
    sleep(2000)
  elif nombre == 32:
    display.show(Image.ARROW_W)
    debut = running_time()
    while True:
      if button_a.was_pressed():
        fin = running_time()
        break
    temps_ecoule = (fin - debut)/1000
    display.scroll(temps_ecoule)
    sleep(2000)
  sleep(200)
```
````
