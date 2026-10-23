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

# Entrées et sorties

## Fonction `print()`

La fonction `print()` permet d'afficher une phrase ou la valeur d'un objet sur
la console.

## Exemple {num2}`exemple`

{.lower-alpha-paren}
1.  Affichage d'une chaine de caractère. Ce qui se trouve entre guillemets sera
    affiché tel quel.

    ```{exec} python
    :editor:
    print("Hello world!")
    ```
2.  Affichage de la valeur d'une variable.

    ```{exec} python
    :editor:
    a = 10
    print(a)
    a += 5
    print(a)
    ```
3.  Affichage d'une chaîne de caractère et de la valeur d'une variable. Il faut
    utiliser une virgule pour séparer les différents éléments.

    ```{exec} python
    :editor:
    prix_choco = 17.20
    print("Le prix de la boîte de chocolat est de", prix_choco, "CHF.")
    ```

### Exercice {num2}`exercice`

Écrivez un programme qui affiche exactement ce texte:

```{exec} python
:then: py-ex-1-sol
:when: load
:class: hidden
```

```{exec} python
:editor: 39661323-0c23-419d-9d91-fadd12c137dc
# Écrivez le programme ici
```

% TODO: Validation de l'exercice par un vu, s'il est correctement réalisé

````{solution}
```{exec} python
:name: py-ex-1-sol
:linenos:
print("Salut!")
print("Je suis élève au collège Sainte-Croix.")
print("J'ai 16 ans.")
print("J'aime bien jouer au volley.")
```
````

### Exercice {num2}`exercice`

{.lower-alpha-paren}
1.  Sans exécuter le programme ci-dessous, prédisez ce qu'il affichera.

    ```{exec} python
    :linenos:
    salutations = "Bonjour"
    print(salutations)
    print("salutations")
    ```
2.  Quel est l'impact des guillemets sur le mot `salutations`?

```{solution}
{.lower-alpha-paren}
2.  Lorsque le mot `salutations` est écrit sans guillemets, il fait référence à
la variable. L'affichage substitue donc la variable par son contenu. Lorsque des
guillemets entourent `salutations`, alors le mot est considéré comme une chaîne
de type caractère et le mot est alors affiché tel quel.
```

### Exercice {num2}`exercice`

{.lower-alpha-paren}
1.  Écrivez un programme qui permet d'effectuer les 4 opérations de base
    (addition, soustraction, multiplication et division) avec les nombres 13 et
    2 en affichant le résultat.
2.  Nous aimerions faire de même avec 10 et 3, 8 et 5, ainsi que 15 et 29.\
    Comment faire pour ne pas tout réécrire à chaque fois?\
    Notez la réponse par un commentaire dans le code.

```{exec} python
:editor: bbe7500d-5a86-4648-9701-5ccc08ddff8c
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
print(13 + 2)
print(13 - 2)
print(13 * 2)
print(13 / 2)

# Il faut utiliser des variables.
a = 13              # changer la valeur de a
b = 2               # changer la valeur de b
print(a + b)
print(a - b)
print(a * b)
print(a / b)
```
````

### Exercice {num2}`exercice`

Écrivez un programme qui permet d'afficher les calculs suivants, ainsi que la
réponse:

{.lower-alpha-paren}
1. 452.52 + 27.78 =
2. 5.65 * 3.4 =
3. 4 569 - 8 532 =
4. 56 / 3 =
5. Calculer le quotient de la division entière de 345 par 37.
6. Calculer le reste de la division de 345 par 37.

```{exec} python
:editor: 13d4f2e9-0a6c-4ada-891e-8c61dd9ab1d2
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
print("452.52 + 27.78 = ", 452.52 + 27.78)
print("5.65 * 3.4 = ", 5.65 * 3.4)
print("4569 - 8532 = ", 4569 - 8532)
print("56 / 3 = ", 56 / 3)
print("Le quotient de la division entière de 345 par 37 est ", 345 // 37)
print("Le reste de la division de 345 par 37 est ", 345 % 37)
```
````

### Exercice {num2}`exercice`

{.lower-alpha-paren}
1.  Avant de l'exécuter, expliquez en français ce que fait/calcule le programme
    suivant:

    ```{exec} python
    :editor: 04e50d20-dbc2-4f09-b8dd-8135adaf9406
    :reset: show
    :name: achats
    prix_livre = 9.30
    prix_jeu = 59
    prix_manga = 13.50

    print("Montant total des achats de Luc:",
          2 * prix_livre + 1 * prix_jeu + 3 * prix_manga, "francs.")
    print("Montant total des achats de Juliette:",
          1 * prix_livre + 2 * prix_jeu + 2 * prix_manga, "francs.")
    ````

2.  En période de soldes, les jeux vidéo sont à 50 %, les livres à 5 CHF et les
    mangas ont 6 CHF de rabais. Écrivez le programme qui correspond à ces
    changements.

    ```{exec} python
    :editor: 7b1c5323-09e9-4e1d-9f32-f28d9d5743d4
    :after: achats
    print("Après réductions")
    # Complétez le programme ici

    # définition des variables (prix des articles)

    # calcul et affichage des montants à payer
    ```
3.  Que se passe-t-il si les prix de base (dans l'éditeur de la partie a)
    changent? Est-ce que les prix après réductions s'adaptent aussi?
    Si ce n'est pas le cas, adapter votre programme pour que les prix après
    réductions soient calculer en fonction des prix de base.

````{solution}
```{exec} python
:linenos:
# définition des variables (prix des articles)
prix_livre = 9.30
prix_jeu = 59
prix_manga = 13.50

# calcul et affichage des montants à payer
print("Montant total des achats de Luc:",
      2 * prix_livre + 1 * prix_jeu + 3 * prix_manga, "francs.")
print("Montant total des achats de Juliette:",
      1 * prix_livre + 2 * prix_jeu + 2 * prix_manga, "francs.")

# 2.
print("Après réductions")
# définition des variables (prix des articles)
prix_livre = 5
prix_jeu = prix_jeu * 50 / 100
prix_manga = prix_manga - 6

# calcul et affichage des montants à payer
print("Montant total des achats de Luc avec réductions:",
      2 * prix_livre + 1 * prix_jeu + 3 * prix_manga, "francs.")
print("Montant total des achats de Juliette avec réductions:",
      1 * prix_livre + 2 * prix_jeu + 2 * prix_manga, "francs.")
```
````

## Fonction input()

La fonction `input(...)` donne la main à l'utilisateur et attend que celui-ci
donne une réponse et la valide en appuyant sur {kbd}`Enter`.

La valeur saisie doit être obligatoirement affectée à une variable, sinon elle
sera perdue.

La valeur rentrée par l'utilisateur est stockée sous forme de
chaîne de caractères (de type `str`). Pour effectuer des calculs, il faut la
convertir en `int` (nombre entier) ou en `float` (nombre à virgule).

```{exec} python
:when:
nom_variable = input("...")
```

### Exemple {num2}`exemple`

```{exec} python
prenom = input("Comment t'appelles-tu?")  # prenom est une chaîne de caractères
age = int(input("Quel est ton age?"))    # age est un nombre entier
taille = float(input("Quelle est ta taille en mètres?")) # taille est un nombre à virgule
print(prenom, age, taille)
```

### Exercice {num2}`exercice`

{.lower-alpha-paren}
1.  Complétez le programme pour demander à l'utilisateur la couleur du carré.

    ```{exec} python
    :editor: 52dd0403-306d-4767-b937-0f4632d6caf3
    :after: fonctions_dessin_svg
    :then: rendu
    couleur =
    position_x = 100
    position_y = 50
    cote = 300

    rectangle(position_x, position_y, cote, cote, couleur)
    ```

    ````{solution}
    ```{exec} python
    :editor:
    :after: fonctions_dessin_svg
    :then: rendu
    # définition des variables
    couleur = input("Quelle doit être la couleur du carré?")
    position_x = 100
    position_y = 50
    cote = 300

    rectangle(position_x, position_y, cote, cote, couleur)
    ```
    ````

2.  Complétez le programme pour demander à l'utilisateur le côté du carré.

    ```{exec} python
    :editor: 79450216-3949-435f-86ee-f70aea4b0694
    :after: fonctions_dessin_svg
    :then: rendu
    cote =
    couleur = "cyan"
    position_x = 100
    position_y = 50

    rectangle(position_x, position_y, cote, cote, couleur)
    ```

    ````{solution}
    ```{exec} python
    :editor:
    :after: fonctions_dessin_svg
    :then: rendu
    # définition des variables
    cote = int(input("Quelle doit être la longueur du côté de carré?"))
    couleur = "cyan"
    position_x = 100
    position_y = 50

    rectangle(position_x, position_y, cote, cote, couleur)
    ```
    ````

2.  Complétez le programme pour demander à l'utilisateur la couleur, le côté et la position (coordonnées x et y) du carré.

    ```{exec} python
    :editor: fe81fd86-5851-48f5-9f4a-f6aa7ad7bc32
    :after: fonctions_dessin_svg
    :then: rendu

    rectangle(position_x, position_y, cote, cote, couleur)
    ```

    ````{solution}
    ```{exec} python
    :editor:
    :after: fonctions_dessin_svg
    :then: rendu
    # définition des variables
    couleur = input("Quelle doit être la couleur du carré?")
    cote = int(input("Quelle doit être la longueur du côté de carré?"))
    position_x = int(input("Quelle doit être la position x du carré?"))
    position_y = int(input("Quelle soit être la position y du carré?"))

    rectangle(position_x, position_y, cote, cote, couleur)
    ```
    ````


### Exercice {num2}`exercice`

Écrivez un programme qui demande à l'utilisateur son nom, son prénom et où il
habite. Le programme affichera:

```{code-block} text
Quel est ton nom?
Quel est ton prénom?
Où habites-tu?
Bonjour {afficher le prénom} {afficher le nom}, heureux de faire ta connaissance.
Je vois que tu habites à {afficher le lieu}.
```

```{exec} python
:editor: 7bca82f8-116c-4826-9c54-4bed0bc2a8a1
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
nom = input("Quel est ton nom? ")
prenom = input("Quel est ton prénom? ")
lieu = input("Où habites-tu? ")
print("Bonjour", prenom, nom, ", heureux de faire ta connaissance.")
print("Je vois que tu habites à", lieu)
```
````

### Exercice {num2}`exercice`

Le programme ci-dessous contient une erreur par ligne. Trouvez et corrigez-les.

```{tip}
Lisez toujours le message d'erreur qui donne différentes informations:
- la ligne de l'erreur
- où se trouve probablement l'erreur sur la ligne
- le type d'erreur
- une explication
```

```{exec} python
:editor:
print("Bienvenue dans ce nouveau programme!)
print(nombre_de_pommes = 10)
print("Vous devez payer" nombre_de_pommes * 1.5 "CHF")
print(Fin du programme)
```

````{solution}
```{exec} python
:linenos:
print("Bienvenue dans ce nouveau programme!")
nombre_de_pommes = 10
print("Vous devez payer", nombre_de_pommes * 1.5, "CHF")
print("Fin du programme")
```
````

% ### Exercice {num2}`exercice`
%
% Le programme ci-dessous devrait permettre de calculer l'année de naissance de
% l'utilisateur. Toutefois, celui-ci contient au moins une erreur par ligne.
% Trouvez et corrigez-les.
%
% ```{exec} python
% :editor:
% age = input("Quel âge as-tu? ")
% annee = input("En quelle année sommes-nous? ")
% print("Vous êtes né.e en" annee - age "ou en" annee - age - 1)
% ```
%
% ````{solution}
% ```{exec} python
% :linenos:
% age = int(input("Quel âge as-tu? "))
% annee = int(input("En quelle année sommes-nous? "))
% print("Vous êtes né.e en", annee - age, "ou en", annee - age - 1)
% ```
% ````

% ### Exercice {num2}`exercice`
%
% Écrivez un programme qui convertit des mégaoctets en bits.\
% Le programme affichera:
%
% ```{code-block} text
% Nombre de mégaoctets:
% {afficher le nombre de mégaoctets} Mo donnent {afficher le nombre de bits} bits.
% ```
%
% ```{exec} python
% :editor: 159755bc-7e41-48c4-9f88-0cc605a1929a
% # Écrivez le programme ici
% ```
%
% ````{solution}
% ```{exec} python
% :linenos:
% nb_mo = float(input("Nombre de mégaoctets: "))
% # 1 octet = 8 bits
% nb_bits = int(nb_mo * 8 * 1000000)
% print(nb_mo, "Mo donnent", nb_bits, "bits.")
% ```
% ````

### Exercice {num2}`exercice`

Écrivez un programme permettant de convertir des degrés Fahrenheit en degrés
Celsius. Pour une température en Fahrenheit $F$, on trouve son équivalent en
Celsius $C$ avec la formule :

$$C = \frac{F - 32}{1.8}$$

Par exemple, si l'utilisateur entre la valeur `60.2`, alors le programme
affichera:

```{code-block} text
Température en °F: 60.2
Merci, 60.2 °F équivalent à 15.666666666666668 °C
```

```{exec} python
:editor: 2fabc445-fc9f-4275-a016-aec79668c153
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
fahrenheit = float(input("Température en °F: "))
celsius = (fahrenheit - 32) / 1.8
print("Merci,", fahrenheit, "°F équivaut à", celsius, "°C")
```
````
