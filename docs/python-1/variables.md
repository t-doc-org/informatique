% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Variables

```{metadata}
hide-solutions: true
```

## Définition

Nous pouvons nous représenté une variable comme l'association d'une étiquette
(nom de la variable) et d'une boîte pouvant contenir une donnée (emplacement
dans la mémoire).

```{image} images/boites.png
:alt: Boites de variables
:width: 40%
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


## Exercice {num}`exo-py1`

1.  ```{exec} python
    :linenos:
    :when: load
    :class: hidden
    while True:
      resp = await input_line("60")
      resp = resp.lower()
      if resp == "int" or resp == "integer": break
      print("\x0cEssaie encore.")
    print("\x0cBravo!")
    ```

2.  ```{exec} python
    :linenos:
    :when: load
    :class: hidden
    while True:
      resp = await input_line("\"Hello Bob\"")
      resp = resp.lower()
      if resp == "str" or resp == "string": break
      print("\x0cEssaie encore.")
    print("\x0cBravo!")

3.  ```{exec} python
    :linenos:
    :when: load
    :class: hidden
    while True:
      resp = await input_line("1.34")
      resp = resp.lower()
      if resp == "float" or resp == "flottant": break
      print("\x0cEssaie encore.")
    print("\x0cBravo!")
    ```

4.  ```{exec} python
    :linenos:
    :when: load
    :class: hidden
    while True:
      resp = await input_line("True")
      resp = resp.lower()
      if resp == "bool" or resp == "booléen" or resp == "boolean": break
      print("\x0cEssaie encore.")
    print("\x0cBravo!")
    ```

5.  ```{exec} python
    :linenos:
    :when: load
    :class: hidden
    while True:
      resp = await input_line("\"45\"")
      resp = resp.lower()
      if resp == "str" or resp == "string": break
      print("\x0cEssaie encore.")
    print("\x0cBravo!")
    ```

6.  ```{exec} python
    :linenos:
    :when: load
    :class: hidden
    while True:
      resp = await input_line("-1.23")
      resp = resp.lower()
      if resp == "float" or resp == "flottant": break
      print("\x0cEssaie encore.")
    print("\x0cBravo!")
    ```

7.  ```{exec} python
    :linenos:
    :when: load
    :class: hidden
    while True:
      resp = await input_line("\"False\"")
      resp = resp.lower()
      if resp == "str" or resp == "string": break
      print("\x0cEssaie encore.")
    print("\x0cBravo!")
    ```

8.  ```{exec} python
    :linenos:
    :when: load
    :class: hidden
    while True:
      resp = await input_line("0.34")
      resp = resp.lower()
      if resp == "float" or resp == "flottant": break
      print("\x0cEssaie encore.")
    print("\x0cBravo!")
    ```

9.  ```{exec} python
    :linenos:
    :when: load
    :class: hidden
    while True:
      resp = await input_line("-12")
      resp = resp.lower()
      if resp == "int" or resp == "integer": break
      print("\x0cEssaie encore.")
    print("\x0cBravo!")
    ```

10. ```{exec} python
    :linenos:
    :when: load
    :class: hidden
    while True:
      resp = await input_line("False")
      resp = resp.lower()
      if resp == "bool" or resp == "booléen" or resp == "boolean": break
      print("\x0cEssaie encore.")
    print("\x0cBravo!")
    ```

## Affectation d'une variable

L'affectation d'une variable se fait avec un nom de variable, suivi du signe `=`
et de la valeur:

```{exec} python
:linenos:
:when: never
age = 17
prenom = "Bob"
moyenne = 5.2
promu = True
```

## Exercice {num}`exo-py1`

Ce code Python déclare 5 variables, mais contient une erreur par ligne. Trouver
et corriger les erreurs.

```{exec} python
:linenos:
:editable:
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


1. À la création d'une variable, le nom doit toujours être à gauche du signe
égal, et la valeur à droite.

2. Une valeur de type `str` doit être entourée de guillemets.

3. Une valeur de type `float` s'écrit non pas avec une virgule mais avec un
point.

4. Une valeur de type `bool` prend une majuscule à `True` et `False`.

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


## Exercice {num}`exo-py1`

Quel est le résultat des expressions suivantes en Python?

1.  ```{exec} python
    :linenos:
    :when: load
    :class: hidden
    while True:
      resp = await input_line("15 // 4 = ")
      if resp == "3": break
      print("\x0cIl faut effectuer la division entière de 23 par 5.")
    print("\x0cBravo!")
    ```

2.  ```{exec} python
    :linenos:
    :when: load
    :class: hidden
    while True:
      resp = await input_line("16 % 5 = ")
      if resp == "1": break
      print("\x0c% est le reste de la division entière")
    print("\x0cBravo!")
    ```

3.  ```{exec} python
    :linenos:
    :when: load
    :class: hidden
    while True:
      resp = await input_line("12 / 5 = ")
      if resp == "2.4": break
      if resp == "2,4":
        print("\x0cEn Python, il faut utiliser des points pour les nombres à virgule.")
      else:
        print("\x0cIl faut effectuer la division.")
    print("\x0cBravo!")
    ```

4.  ```{exec} python
    :linenos:
    :when: load
    :class: hidden
    while True:
      resp = await input_line("4 - 3 * 2 = ")
      if resp == "-2": break
      if resp == "2":
        print("\x0cEn Python, l'ordre de priorité est le même qu'en maths.")
      else:
        print("\x0cEssaie encore.")
    print("\x0cBravo!")
    ```

5.  ```{exec} python
    :linenos:
    :when: load
    :class: hidden
    while True:
      resp = await input_line("(1 + 2)**2 - 1 = ")
      if resp == "8": break
      print("\x0cEssaie encore.")
    print("\x0cBravo!")
    ```


## Exécution d'un programme

Lors de l'exécution d'un programme, Python va lire les instructions ligne par
ligne et les effectuer. Afin de comprendre comment fonctionne un programme et
évaluer le résultat, nous allons utiliser des tableaux d'états. Ceux-ci
permettent de connaître à chaque ligne, la valeur des variables.

## Exemple {num}`ex-var`

<table style="width: 100%"><tr style="text-align: center">
  <th>Programme</th><th>Tableau d'états</th>
</tr><tr style="vertical-align: top"><td>

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

</td><td style="padding-left: 1rem">

| ligne | a | b | c | d |
|:-----:|:-:|:-:|:-:|:-:|
| 1 | 10| ? | ? | ? |
| 2 | 10| 30| ? | ? |
| 3 | 10| 30| 40| ? |
| 4 | 10| 30| 40| 400|
| 5 | 20| 30| 40| 400 |

</td></tr></table>

## Exercice {num}`exo-py1`

Déterminer la valeur de chacune des variables de ce programme en créant un
tableau d'états.

```{exec} python
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

```{solution}

| x  | y  | z  |
| :-:| :-:| :-:|
| 10 | ?  | ?  |
| 10 | 2  | ?  |
| 10 | 2  | 20 |
| 10 | 30 | 20 |
| 20 | 30 | 20 |
| 20 | 30 | 40 |
| 20 | 5  | 40 |

````

## Exercice {num}`exo-py1`

Déterminer la valeur de chacune des variables de ce programme en créant un
tableau d'états.

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
print(nombe_habitants, cout, prix)
```

```{solution}
| nombre_habitants  | cout  | prix  |
| :--| :--| :--|
| 200 |  ? | ?  |
| 200 | 100  | ? |
| 200 | 100  | 20000 |
| 200 | 50 | 20000 |
| 100 | 50 | 20000 |
| 100 | 50 | 25000 |
| 400 | 50  | 25000 |
| 400 | 50  | 45000 |

```

## Exercice {num}`exo-py1`

Compléter le programme ci-dessous de manière à ce qu'il permette de calculer la
moyenne des notes principales dans la variable du même nom. La note de math est
de 4 et demi, la note de français de 6 et la note d'allemand de 5 et demi.

```{exec} python
:linenos:
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
```
Pour calculer la moyenne, on additionne toutes les notes avant de les diviser
par 3. Comme la division a la priorité sur l'addition, il ne faut pas oublier de
régler la priorité des opérations avec des parenthèses.
````

## Exercice {num}`exo-py1`
Écrire un petit programme en Python permettant de calculer le volume $V$ d'un
cylindre en fonction de son rayon et de son hauteur. Le programme contiendra les
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
:linenos:
:editable:
# Écrire le code ici

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

## Exercice {num}`exo-py1`
Écriver un programme Python contenant une variable `x` initialisée à 10.
Puis, compléter ce programme pour que celui-ci effectue les opérations
suivantes:

-   Ajoute 3 à `x`

-   Soustrais 8 à `x`

-   Multiplie `x` par 10

-   Divise `x` par 5

-   Élève `x` à la puissance 3

À la fin de l'exécution de ce programme, la variable `x` devrait contenir la
valeur `1000`


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

## Exercice {num}`exo-py1` (difficile)

Liser attentivement le programme ci-dessous et expliquer, en français, ce qu'il
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
