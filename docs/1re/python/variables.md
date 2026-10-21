% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{defaults} exec
:editor-config: store: 'cloud'
```

```{exec} python
:name: fonctions_dessin_svg
:class: hidden
:include: fonctions-dessin.py
:when:
creation_image(600, 400, "#FFFFFF")
```

```{exec} python
:name: rendu
:class: hidden
:include: fonctions-dessin.py
:when:
# Affiche l'image
render(img)
```

# Variables

## Définition

Nous pouvons nous représenter une variable comme l'association d'une étiquette
(nom de la variable) et d'une case pouvant contenir une donnée (emplacement
dans la mémoire).

```{image} images/boites.png
:alt: Boites de variables
:width: 50%
:align: center
```

Une variable permet de stocker une valeur numérique, une chaîne de caractères,
etc. qu'on réutilisera par la suite dans notre programme. Pour un programmeur,
une variable est définie par un **nom**. Mais pour l'ordinateur, il
s'agit d'une adresse (emplacement de la mémoire où est stockée cette donnée).

```{attention}
Règles à respecter:

- Le nom de la variable doit correspondre à son contenu.\
  Exemple: age, hauteur
- Le caractère \_ permet de séparer les mots dans un nom de variable.\
  Exemple: cote_carre
- Le nom d'une variable ne doit pas contenir de caractère accentué.
- Le nom d'une variable doit commencer par une lettre ou le caractère de
  soulignement.
- Le nom d'une variable ne peut contenir que les caractères alphanumériques
  (A-z 0-9 et \_)
- Les majuscules et les minuscules font une différence.
  Exemple: mon\_age, mon\_Age, mon\_AGE sont trois variables différentes
```

## Types de données

En Python, il existe 4 types de données primitifs.

| Type      | Nom       | Description                      | Exemple            |
|---------  |--------   |----------------------------------|--------------------|
| **int**   | integer   | Nombres entiers                  | 4                  |
| **float** | flottant  | Nombres à virgules               | 4.125              |
| **str**   | string    | Chaînes de caractères            | "Bonjour"          |
| **bool**  | booléen   | Résultat d'un test: Vrai ou Faux | 2<1 renvoie False  |

### Exercice {num2}`exercice`

De quel type sont les valeurs suivantes?

```{role} select(quiz-select)
:right:
:options: |
: int
: float
: str
: bool
```

```{quiz}
:style: max-width: 20rem;
{.lower-alpha-paren}
1.  {select}`int`   `60`
2.  {select}`str`   `"Hello Bob"`
3.  {select}`float` `1.34`
4.  {select}`bool`  `True`
5.  {select}`str`   `"45"`
6.  {select}`float` `-1.23`
7.  {select}`str`   `"False"`
8.  {select}`float` `0.34`
9.  {select}`int`   `-12`
10. {select}`bool`  `False`
```

## Affectation d'une variable

L'affectation d'une variable se fait avec un nom de variable, suivi du signe `=`
et de la valeur.

```{exec} python
:linenos:
:when:
age = 17                  # La variable age est de type int
prenom = "Bob"            # La variable prenom est de type str
moyenne = 5.2             # La variable moyenne est de type float
promu = True              # La variable promu est de type bool
```

### Exercice {num2}`exercice`

Ce programme Python déclare 5 variables, mais contient une erreur par ligne.
Trouvez et corrigez-les.

```{tip}
Lisez toujours le message d'erreur qui donne différentes informations:
- la ligne de l'erreur
- où se trouve probablement l'erreur sur la ligne
- le type d'erreur
- une explication
```

```{exec} python
:editor:
6 = age
message = Je suis absent
note = 4,5
porte_ouverte = false
nombre de voitures = 10
```

````{solution}
```{exec} python
:linenos:
age = 6
message = "Je suis absent"
note = 4.5
porte_ouverte = False
nombre_de_voitures = 10
```

1.  À la création d'une variable, le nom doit toujours être à gauche du signe
    égal, et la valeur à droite.
2.  Une valeur de type `str` doit être entourée de guillemets.
3.  Une valeur de type `float` s'écrit non pas avec une virgule mais avec un
    point.
4.  Une valeur de type `bool` prend une majuscule à `True` et `False`.
5.  Les noms de variables ne peuvent pas contenir d'espaces. Généralement, en
    Python, on les remplace alors par le caractère de soulignement.
````

## Opérateurs mathématiques

Les opérateurs mathématiques permettent de faire des calculs simples avec les
nombres.

| Opérateur | Nom                                   | Exemple | Résultat |
| :-------: | :-----------------------------------: | :-----: | :------: |
| +         | Addition                              | 3 + 4   | 7        |
| -         | Soustraction                          | 9 - 12  | -3       |
| *         | Multiplication                        | 5 * 6   | 30       |
| /         | Division                              | 11 / 2  | 5.5      |
| **        | Puissance                             | 2 ** 3  | 8        |
| //        | Division entière                      | 26 // 6 | 4        |
| %         | Modulo (reste de la division entière) | 26 mod 6| 2        |


### Exercice {num2}`exercice`

Quel est le résultat des expressions suivantes en Python?

```{role} input(quiz-input)
:right: width: 5rem;
:check: json trim
```

```{quiz}
:style: max-width: 30rem;
{.lower-alpha-paren}
1.  {input}`{"3": true}`
    {quiz-hint}`Il faut effectuer la division entière de 15 par 4.`
    `15 // 4`
2.  {input}`{"1": true}`
    {quiz-hint}`% est le reste de la division entière.`
    `16 % 5`
3.  {input}`{"2.4": true,
             "2,4": "En Python, il faut utiliser un point pour les nombres à
                     virgule."}`
    {quiz-hint}`Il faut effectuer la division.`
    `12 / 5`
4.  {input}`{"-2": true,
             "2": "En Python, l'ordre de priorité est le même qu'en maths."}`
    `4 - 3 * 2`
5.  {input}`{"8": true}`
    `(1 + 2) ** 2 - 1`
```

## Exécution d'un programme

Lors de l'exécution d'un programme, Python va lire les instructions ligne par
ligne et les effectuer. Afin de comprendre comment fonctionne un programme et
évaluer le résultat, nous allons utiliser des tableaux d'états. Ceux-ci
permettent de connaître à chaque ligne, la valeur des variables.

### Exemple {num2}`exemple`

````{list-grid}
:style: grid-template-columns: 1fr min-content;
- # Programme
  ```{exec} python
  :linenos:
  a = 10
  b = 30
  c = a + b
  d = c * a
  a = 2 * a

  # Affiche les valeurs des variables
  print(a, b, c, d)
  ```
- # Tableau d'états
  | ligne | a | b | c | d |
  |:-----:|:-:|:-:|:-:|:-:|
  | 1 | 10| ? | ? | ? |
  | 2 | 10| 30| ? | ? |
  | 3 | 10| 30| 40| ? |
  | 4 | 10| 30| 40| 400|
  | 5 | 20| 30| 40| 400|
````

### Exercice {num2}`exercice`

La fonction `rectangle(position_x, position_y, largeur, hauteur, couleur)`
est une fonction qui permet de dessiner un rectangle avec les propriétés
données entre parenthèses.

```{defaults} quiz-check
:randomize:
:class: grid-4
```

{.lower-alpha-paren}
1. Qu'affiche le progamme suivant?

    ```{exec} python
    :name: ex1.1
    :after: fonctions_dessin_svg
    :when:
    :linenos:
    position_x = 50
    position_y = 50
    largeur = 150
    hauteur = 150
    couleur = "red"

    rectangle(position_x, position_y, largeur, hauteur, couleur)
    ```
    `````{quiz}
    ````{quiz-check}
    - :
      ```{exec} python
      :after: ex1.1
      :when: load
      :then: rendu
      :class: hidden
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      :after: fonctions_dessin_svg
      :then: rendu
      position_x = 50
      position_y = 50
      largeur = 150
      hauteur = 150
      couleur = "blue"

      rectangle(position_x, position_y, largeur, hauteur, couleur)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      :after: fonctions_dessin_svg
      :then: rendu
      position_x = 50
      position_y = 50
      largeur = 150
      hauteur = 150
      couleur = "green"

      rectangle(position_x, position_y, largeur, hauteur, couleur)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      :after: fonctions_dessin_svg
      :then: rendu
      position_x = 50
      position_y = 50
      largeur = 150
      hauteur = 150
      couleur = "yellow"

      rectangle(position_x, position_y, largeur, hauteur, couleur)
      ```
    ````
    `````

2. Qu'affiche le progamme suivant?

    ```{exec} python
    :name: ex1.2
    :after: fonctions_dessin_svg
    :when:
    :linenos:
    position_x = 50
    position_y = 50
    largeur = 300
    hauteur = 150
    couleur = "blue"

    rectangle(position_x, position_y, largeur, hauteur, couleur)
    ```
    `````{quiz}
    ````{quiz-check}
    - :
      ```{exec} python
      :after: ex1.2
      :when: load
      :then: rendu
      :class: hidden
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      :after: fonctions_dessin_svg
      :then: rendu
      position_x = 50
      position_y = 50
      largeur = 150
      hauteur = 300
      couleur = "blue"

      rectangle(position_x, position_y, largeur, hauteur, couleur)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      :after: fonctions_dessin_svg
      :then: rendu
      position_x = 50
      position_y = 50
      largeur = 150
      hauteur = 150
      couleur = "blue"

      rectangle(position_x, position_y, largeur, hauteur, couleur)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      :after: fonctions_dessin_svg
      :then: rendu
      position_x = 50
      position_y = 50
      largeur = 450
      hauteur = 150
      couleur = "blue"

      rectangle(position_x, position_y, largeur, hauteur, couleur)
      ```
    ````
    `````
3.  Qu'affiche le progamme suivant?

    ```{exec} python
    :name: ex1.3
    :after: fonctions_dessin_svg
    :when:
    :linenos:
    position_x = 350
    position_y = 50
    largeur = 200
    hauteur = 200
    couleur = "green"

    rectangle(position_x, position_y, largeur, hauteur, couleur)
    ```
    `````{quiz}
    ````{quiz-check}
    - :
      ```{exec} python
      :after: ex1.3
      :when: load
      :then: rendu
      :class: hidden
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      :after: fonctions_dessin_svg
      :then: rendu
      position_x = 50
      position_y = 50
      largeur = 200
      hauteur = 200
      couleur = "green"

      rectangle(position_x, position_y, largeur, hauteur, couleur)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      :after: fonctions_dessin_svg
      :then: rendu
      position_x = 150
      position_y = 50
      largeur = 200
      hauteur = 200
      couleur = "green"

      rectangle(position_x, position_y, largeur, hauteur, couleur)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      :after: fonctions_dessin_svg
      :then: rendu
      position_x = 250
      position_y = 50
      largeur = 200
      hauteur = 200
      couleur = "green"

      rectangle(position_x, position_y, largeur, hauteur, couleur)
      ```
    ````
    `````
4.  Qu'affiche le progamme suivant?

    ```{exec} python
    :name: ex1.4
    :after: fonctions_dessin_svg
    :when:
    :linenos:
    position_x = 50
    position_y = 200
    largeur = 100
    hauteur = 100
    couleur = "red"

    rectangle(position_x, position_y, largeur, hauteur, couleur)
    ```
    `````{quiz}
    ````{quiz-check}
    - :
      ```{exec} python
      :after: ex1.4
      :when: load
      :then: rendu
      :class: hidden
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      :after: fonctions_dessin_svg
      :then: rendu
      position_x = 50
      position_y = 100
      largeur = 100
      hauteur = 100
      couleur = "red"

      rectangle(position_x, position_y, largeur, hauteur, couleur)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      :after: fonctions_dessin_svg
      :then: rendu
      position_x = 50
      position_y = 300
      largeur = 100
      hauteur = 100
      couleur = "red"

      rectangle(position_x, position_y, largeur, hauteur, couleur)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      :after: fonctions_dessin_svg
      :then: rendu
      position_x = 50
      position_y = 0
      largeur = 100
      hauteur = 100
      couleur = "red"

      rectangle(position_x, position_y, largeur, hauteur, couleur)
      ```
    ````
    `````

5.  Qu'affiche le progamme suivant?

    ```{exec} python
    :name: ex1.5
    :after: fonctions_dessin_svg
    :when:
    :linenos:
    position_x = 0
    position_y = 0
    largeur = 100
    hauteur = 100
    couleur = "blue"

    rectangle(position_x, position_y, largeur, hauteur, couleur)
    ```
    `````{quiz}
    ````{quiz-check}
    - :
      ```{exec} python
      :after: ex1.5
      :when: load
      :then: rendu
      :class: hidden
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      :after: fonctions_dessin_svg
      :then: rendu
      position_x = 500
      position_y = 300
      largeur = 100
      hauteur = 100
      couleur = "blue"

      rectangle(position_x, position_y, largeur, hauteur, couleur)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      :after: fonctions_dessin_svg
      :then: rendu
      position_x = 0
      position_y = 300
      largeur = 100
      hauteur = 100
      couleur = "blue"

      rectangle(position_x, position_y, largeur, hauteur, couleur)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      :after: fonctions_dessin_svg
      :then: rendu
      position_x = 500
      position_y = 0
      largeur = 100
      hauteur = 100
      couleur = "blue"

      rectangle(position_x, position_y, largeur, hauteur, couleur)
      ```
    ````
    `````

### Exercice {num2}`exercice`

{.lower-alpha-paren}
1. Qu'affiche le progamme suivant?

    ```{exec} python
    :name: ex2.1
    :after: fonctions_dessin_svg
    :when:
    :linenos:
    point_1 = (50, 50)
    point_2 = (350, 50)
    point_3 = (150, 200)
    couleur = "green"

    point_1 = (300, 100)
    point_2 = (500, 50)
    point_3 = (400, 300)
    couleur = "blue"

    triangle(point_1, point_2, point_3, couleur)
    ```
    `````{quiz}
    ````{quiz-check}
    - :
      ```{exec} python
      :after: ex2.1
      :when: load
      :then: rendu
      :class: hidden
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      :after: fonctions_dessin_svg
      :then: rendu
      point_1 = (50, 50)
      point_2 = (550, 100)
      point_3 = (150, 300)
      couleur = "green"
      triangle(point_1, point_2, point_3, couleur)

      point_1 = (300, 100)
      point_2 = (500, 50)
      point_3 = (400, 300)
      couleur = "blue"
      triangle(point_1, point_2, point_3, couleur)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      :after: fonctions_dessin_svg
      :then: rendu
      point_1 = (300, 100)
      point_2 = (500, 50)
      point_3 = (400, 300)
      couleur = "blue"
      triangle(point_1, point_2, point_3, couleur)

      point_1 = (50, 50)
      point_2 = (550, 100)
      point_3 = (150, 300)
      couleur = "green"
      triangle(point_1, point_2, point_3, couleur)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      :after: fonctions_dessin_svg
      :then: rendu
      point_1 = (50, 50)
      point_2 = (550, 100)
      point_3 = (150, 300)
      couleur = "green"
      triangle(point_1, point_2, point_3, couleur)
      ```
    ````
    `````

2. Qu'affiche le progamme suivant?

    ```{exec} python
    :name: ex2.2
    :after: fonctions_dessin_svg
    :when:
    :linenos:
    position_x = 200
    position_y = 200
    largeur = 100
    hauteur = 100
    couleur = "blue"
    couleur = "violet"

    rectangle(position_x, position_y, largeur, hauteur, couleur)
    cercle(position_x, position_y, largeur, couleur)
    ```
    `````{quiz}
    ````{quiz-check}
    - :
      ```{exec} python
      :after: ex2.2
      :when: load
      :then: rendu
      :class: hidden
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      :after: fonctions_dessin_svg
      :then: rendu
      position_x = 200
      position_y = 200
      largeur = 100
      hauteur = 100
      couleur = "blue"

      rectangle(position_x, position_y, largeur, hauteur, couleur)
      couleur = "violet"
      cercle(position_x, position_y, largeur, couleur)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      :after: fonctions_dessin_svg
      :then: rendu
      position_x = 200
      position_y = 200
      largeur = 100
      hauteur = 100
      couleur = "blue"

      cercle(position_x, position_y, largeur, couleur)
      couleur = "violet"
      rectangle(position_x, position_y, largeur, hauteur, couleur)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      :after: fonctions_dessin_svg
      :then: rendu
      position_x = 200
      position_y = 200
      largeur = 100
      hauteur = 100
      couleur = "blue"

      rectangle(position_x, position_y, largeur, hauteur, couleur)
      cercle(position_x, position_y, largeur, couleur)
      ```
    ````
    `````

### Exercice {num2}`exercice`

Définissez les variables pour dessiner

{.lower-alpha-paren}
1.  un cercle de rayon **100** positionné en **(100; 100)** et de couleur
    **verte**.

2.  un cercle de rayon **200** positionné en **(250; 150)** et de couleur
    **magenta**.

```{exec} python
:editor: c82bdfda-3c43-4d2a-872a-f0b40cb52d6b
:after: fonctions_dessin_svg
:then: rendu
# définition des variables

cercle(centre_x, centre_y, rayon, couleur)
```

````{solution}
{.lower-alpha-paren}
1.  ```{exec} python
    :editor:
    :after: fonctions_dessin_svg
    :then: rendu
    # définition des variables
    rayon = 100
    centre_x = 100
    centre_y = 100
    couleur = "green"

    cercle(centre_x, centre_y, rayon, couleur)
    ```
2.  ```{exec} python
    :editor:
    :after: fonctions_dessin_svg
    :then: rendu
    # définition des variables
    rayon = 200
    centre_x = 250
    centre_y = 150
    couleur = "magenta"

    cercle(centre_x, centre_y, rayon, couleur)
    ```
````




### Exercice {num2}`exercice`

Déterminez la valeur de chacune des variables de ce programme en créant un
tableau d'états.

```{exec} python
:linenos:
:when:
x = 10
y = 2
z = y * x
y = z + x
x = y - z / 2
z = z * 2
y = 5

# Affiche les valeurs des variables
print(x, y, z)
```

`````{solution}
````{list-grid}
:style: grid-template-columns: 1fr min-content;
- ```{exec} python
  :linenos:
  x = 10
  y = 2
  z = y * x
  y = z + x
  x = y - z / 2
  z = z * 2
  y = 5

  # Affiche les valeurs des variables
  print(x, y, z)
  ```
- | ligne | x  | y  | z  |
  |:-----:| :-:| :-:| :-:|
  | 1 | 10 | ?  | ?  |
  | 2 | 10 | 2  | ?  |
  | 3 | 10 | 2  | 20 |
  | 4 | 10 | 30 | 20 |
  | 5 | 20 | 30 | 20 |
  | 6 | 20 | 30 | 40 |
  | 7 | 20 | 5  | 40 |
````
`````

### Exercice {num2}`exercice`

Déterminez la valeur de chacune des variables de ce programme en créant un
tableau d'états.

```{exec} python
:linenos:
:when:
nombre_habitants = 150 + 25 * 2
cout = 100
prix = nombre_habitants * cout
cout = cout / 2
nombre_habitants = nombre_habitants - 100
prix = prix + nombre_habitants * cout
nombre_habitants = 400
prix = prix + nombre_habitants * cout

# Affiche les valeurs des variables
print(nombre_habitants, cout, prix)
```

````{solution}
```{exec} python
:linenos:
nombre_habitants = 150 + 25 * 2
cout = 100
prix = nombre_habitants * cout
cout = cout / 2
nombre_habitants = nombre_habitants - 100
prix = prix + nombre_habitants * cout
nombre_habitants = 400
prix = prix + nombre_habitants * cout

# Affiche les valeurs des variables
print(nombre_habitants, cout, prix)
```

| ligne | nombre_habitants  | cout  | prix  |
|:-----:| :--| :--| :--|
| 1 | 200 |  ? | ?  |
| 2 | 200 | 100  | ? |
| 3 | 200 | 100  | 20000 |
| 4 | 200 | 50 | 20000 |
| 5 | 100 | 50 | 20000 |
| 6 | 100 | 50 | 25000 |
| 7 | 400 | 50  | 25000 |
| 8 | 400 | 50  | 45000 |

````

### Exercice {num2}`exercice`

Complétez le programme ci-dessous de manière à ce qu'il calcule la moyenne des
notes principales dans la variable du même nom. La note de math est de 4 et
demi, la note de français de 6 et la note d'allemand de 5 et demi.

```{exec} python
:editor: 184beb38-78ed-48e5-89ee-2c19101727fd
# Complétez le programme
math =
francais =
allemand =
moyenne =

# Affiche la valeur de la moyenne
print(moyenne)
```

````{solution}
```{exec} python
:linenos:
math = 4.5
francais = 6
allemand = 5.5
moyenne = (math + francais + allemand) / 3

# Affiche la valeur de la moyenne
print(moyenne)
```
Pour calculer la moyenne, on additionne toutes les notes avant de diviser le
résultat par le nombre de notes, ici 3.

Comme la division a la priorité sur l'addition, il ne faut pas oublier de
régler la priorité des opérations avec des parenthèses.
````

### Exercice {num2}`exercice`
Écrivez un petit programme en Python permettant de calculer le volume d'un
cylindre en fonction de son rayon et de sa hauteur. Le programme contiendra les
lignes suivantes :

-   Créer une variable `pi` contenant la valeur `3.14`.

-   Créer une variable `hauteur` contenant la valeur `30`

-   Créer une variable `rayon` contenant la moitié de 11

-   Créer une variable `aire_disque` contenant le résultat de
    $\pi \cdot r^2$

-   Créer une variable `volume` contenant le résultat de l'aire du
    disque multiplié par la hauteur.

Au terme de l'exécution de ce programme, la variable `volume` devrait
contenir la valeur `2849.55`

```{exec} python
:editor: ac388a32-91a1-438e-b082-71550202565c
# Écrivez le programme ici

# Affiche le volume
print(volume)
```

````{solution}
```{exec} python
:linenos:
pi = 3.14
hauteur = 30
rayon = 11 / 2 #ou rayon = 5.5
aire_disque = pi * rayon ** 2
volume = aire_disque * hauteur

# Affiche le volume
print(volume)
```
````

## Opérateurs d'affectation

Les opérateurs d'affectation combinée permettent de modifier la valeur des
variables avec une notation simplifiée. Il existe pour tous les opérateurs
mathématiques, voici les principaux.

| Opérateur | Exemple | Équivalent à |
| :-------: | :-----: | :----------: |
| =         | x = 6   | x = 6        |
| +=        | x += 6  | x = x + 6    |
| -=        | x -= 6  | x = x - 6    |
| \*=       | x \*= 6 | x = x * 6    |
| /=        | x /= 6  | x = x / 6    |

### Exercice {num2}`exercice`

Écrivez un programme Python contenant une variable `x` initialisée à 10.
Puis, complétez ce programme pour que celui-ci effectue les opérations
suivantes en utilisant les opérateurs d'affectation combinée:

-   Ajoute 3 à `x`

-   Soustrais 8 à `x`

-   Multiplie `x` par 10

-   Divise `x` par 5

-   Élève `x` à la puissance 3

À la fin de l'exécution de ce programme, la variable `x` devrait contenir la
valeur `1000`

```{exec} python
:editor: df136ddf-cd4a-4044-88f0-b061f0568d69
# Écrivez le programme ici
```


````{solution}
```{exec} python
:linenos:
x = 10
x += 3
x -= 8
x *= 10
x /= 5
x **= 3

print(x)
```
````

### Exercice {num2}`exercice`

Lisez attentivement le programme ci-dessous et expliquez, en français, ce qu'il
fait. À quoi correspondent les variables `h1`, `h2`, et `total`.

```{exec} python
:linenos:
CHF_par_h1 = 32.5
CHF_par_h2 = 40
heure_debut = 20
temps_de_travail = 8.5
h1 = (heure_debut + temps_de_travail)
h2 = temps_de_travail - h1
total = h1 * CHF_par_h1 + h2 * CHF_par_h2
```

```{solution}
:class: note dropdown
Ce programme permet de calculer et stocker le salaire d'un employé dans la
variable `total`. De toute évidence, cet employé travail de nuit comme il a
commencé à 20h et a travaillé durant 8 heures et demie. La variable `h1`
contient le nombre d'heures passées après minuit (en effet, le reste de la
division entière de 28.5 par 24 nous donne 4.5, et l'employé a bien fini de
travailler à 4 heure et demie). Ainsi, en soustrayant `h1` aux nombres d'heures
travaillées au total, `h2` contient le nombre d'heures travaillées avant minuit.
Ces deux variables permettent de calculer le salaire total avec les taux corrects.
```
