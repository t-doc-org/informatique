% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Entrées et sorties

```{metadata}
hide-solutions: true
```

## Fonction `print()`

La fonction `print()` permet d'afficher une phrase ou la valeur d'un objet sur
la console.

## Exemple {num}`ex-io`

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
    a = a + 5
    print(a)
    ```

3.  Affichage d'une chaîne de caractère et de la valeur d'une variable. Il faut
    utiliser une virgule pour séparer les différents éléments.

    ```{exec} python
    :editor:
    prix_choco = 17.20
    print("Le prix de la boîte de chocolat est de", prix_choco, "CHF.")
    ```

## Exercice {num}`exo-py1`

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

## Exercice {num}`exo-py1`

1. Écrivez un programme qui affiche "Bonjour tout le monde!".
2. Écrivez un programme qui affiche "Je programme!".
3. Écrivez un programme qui affiche "Je programme! Je programme!".
4. Écrivez un programme qui affiche "Je programme! " 10 fois de suite sans
récrire 10 fois la même chose.
5. Ajoutez un commentaire qui explique ce que tu as fait au point précédent.

```{exec} python
:editor: 4d040bd2-fe01-409f-9b82-5edd968bd23d
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
print("Bonjour tout le monde!")
print("Je programme!")
print("Je programme! Je programme!")
# Pour répéter plusieurs fois une chaine de caractères, on peut utiliser *
print("Je programme! " * 10)
```
````

### Exercice {num}`exo-py1`

1.  Sans exécuter le programme ci-dessous, prédisez ce qu'il affichera.

```{exec} python
:linenos:
salutations = "Bonjour"
print(salutations)
print("salutations")
```

2.  Quel est l'impact des guillemets sur le mot `salutations`?

```{solution}
2.  Lorsque le mot `salutations` est écrit sans guillemets, il fait référence à
la variable. L'affichage substitue donc la variable par son contenu. Lorsque des
guillemets entourent `salutations`, alors le mot est considéré comme une chaîne
de type caractère et le mot est alors affiché tel quel.
```

## Exercice {num}`exo-py1`

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

## Exercice {num}`exo-py1`

Écrivez un programme qui permet d'afficher les calculs suivants, ainsi que la
réponse:

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

## Exercice {num}`exo-py1`

Écrivez un programme qui permet de résoudre l'exercice suivant (ne pas oublier
les phrases d'explication):

1.  Luc va faire des courses. Il achète deux livres à 9.30 CHF, un jeu vidéo à
    59 CHF et trois mangas à 13.50 CHF. Calculer le montant total des dépenses
    de Luc.
2.  Juliette achète un livre, deux jeux vidéo et deux mangas. Calculer le
    montant total des dépenses de Juliette.
3.  En période de soldes, les jeux vidéo sont à 50 %, les livres à 5 CHF et les
    mangas ont 6 CHF de rabais.

```{exec} python
:editor: 7b1c5323-09e9-4e1d-9f32-f28d9d5743d4
# Complétez le programme
prix_livre =
prix_jeu =
prix_manga =

print("Montant total des achats de Luc:", ... , "francs.")
print("Montant total des achats de Juliette:", ... , "francs.")

print("Après réduction")
prix_livre =
prix_jeu =
prix_manga =

print("Montant total des achats de Luc avec réduction:", ... , "francs.")
print("Montant total des achats de Juliette avec réductions:", ... , "francs.")
```

````{solution}
```{exec} python
:linenos:
prix_livre = 9.30
prix_jeu = 59
prix_manga = 13.50

print("Montant total des achats de Luc:",
      2 * prix_livre + 1 * prix_jeu + 3 * prix_manga, "francs.")
print("Montant total des achats de Juliette:",
      1 * prix_livre + 2 * prix_jeu + 2 * prix_manga, "francs.")

print("Après réduction")
prix_livre = 5
prix_jeu = prix_jeu * 50 / 100
prix_manga = prix_manga - 6

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

```{important}
L'utilisation de la fonction input sur ce site est différente de ce qui est
utilisé dans d'autre logiciel.\
`nom_variable = input("...")` -> version des autres logiciels\
`nom_variable = await input_line("...")` -> version pour ce site
```

## Exercice {num}`exo-py1`

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
nom = await input_line("Quel est ton nom? ")
prenom = await input_line("Quel est ton prénom? ")
lieu = await input_line("Où habites-tu? ")
print("Bonjour", prenom, nom, ", heureux de faire ta connaissance.")
print("Je vois que tu habites à", lieu)
```
````

## Exercice {num}`exo-py1`

Le programme ci-dessous contient une erreur par ligne. Trouvez et corrigez-les.

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

## Exercice {num}`exo-py1`

Le programme ci-dessous devrait permettre de calculer l'année de naissance de
l'utilisateur. Toutefois, celui-ci contient au moins une erreur par ligne.
Trouvez et corrigez-les.

```{exec} python
:editor:
age = input("Quel âge as-tu? ")
annee = input("En quelle année sommes-nous? ")
print("Vous êtes né.e en" annee - age "ou en" annee - age - 1)
```

````{solution}
```{exec} python
:linenos:
age = int(await input_line("Quel âge as-tu? "))
annee = int(await input_line("En quelle année sommes-nous? "))
print("Vous êtes né.e en", annee - age, "ou en", annee - age - 1)
```
````

## Exercice {num}`exo-py1`

Écrivez un programme qui convertit des mégaoctets en bits.\
Le programme affichera:

```{code-block} text
Nombre de mégaoctets:
{afficher le nombre de mégaoctets} Mo donnent {afficher le nombre de bits} bits.
```

```{exec} python
:editor: 159755bc-7e41-48c4-9f88-0cc605a1929a
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
nb_mo = float(await input_line("Nombre de mégaoctets: "))
# 1 octet = 8 bits
nb_bits = int(nb_mo * 8 * 1000000)
print(nb_mo, "Mo donnent", nb_bits, "bits.")
```
````

## Exercice {num}`exo-py1`

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
fahrenheit = float(await input_line("Température en °F: "))
celsius = (fahrenheit - 32) / 1.8
print("Merci,", fahrenheit, "°F équivaut à", celsius, "°C")
```
````
