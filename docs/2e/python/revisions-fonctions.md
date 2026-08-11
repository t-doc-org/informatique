% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Révisions - Fonctions

En programmation, une fonction est un bloc de code (suite d'instructions) qui
réalise une tâche. Nous en avons déjà rencontré plusieurs:

`print(...)`
: affiche ce qui est entre parenthèses sur la console.

`input(...)`
: demande à l'utilisateur d'entrer une donnée.

`int(...)`
: convertit ce qui est entre parenthèses en nombre entier.

`float(...)`
: convertit ce qui est entre parenthèses en nombre à virgule.

`range(...)`
: renvoie une liste de nombre (de 0 à la valeur entre parenthèses -1).

Toutes les fonctions ci-dessus sont des fonctions intégrées, elles ont été
prédéfinies pour nous. Nous n'avons qu'à les utiliser, sans nous soucier de
comment elles ont été programmées.

Pour éviter de répéter du code et rendre le code plus lisible, il est utile de
pouvoir définir nos propres fonctions. La syntaxe est la suivante:

```{exec} python
:when: never
# Définition de la fonction
def nom_de_la_fonction(paramètres):
  instruction 1
  instruction 2
  ...

# Appel de la fonction dans le programme
nom_de_la_fonction(paramètres)
```

Un paramètre (nom donné aux éléments notés entre parenthèses dans la définition
de la fonction) permet de transmettre une valeur à une fonction afin de modifier
son comportement.

## Exercice {num2}`exercice-rev`

Une fonction nommée `salutations` a été définie ci-dessous. Appelez cette
fonction dans le programme.

```{exec} python
:editor:
def salutations():
  print("Bonjour, comment vas-tu?")

# Complétez l'appel de la fonction
...
```

````{solution}
```{exec} python
:linenos:
def salutations():
  print("Bonjour, comment vas-tu?")

# Appel de la fonction
salutations()
```
````

## Exercice {num2}`exercice-rev`

Une fonction nommée `affiche_somme` prend 2 paramètres numériques. Cette
fonction additionne les paramètres et affiche le résultat.

Appelez cette fonction 2 fois pour que le programme affiche le résultat de
4 + 9 et celui de de 3 + 7.

```{exec} python
:editor:
def affiche_somme(a, b):
  print(a + b)

# Complétez l'appel de la fonction 2 fois
...
```

````{solution}
```{exec} python
:linenos:
def affiche_somme(a, b):
  print(a + b)

# Appel de la fonction 2 fois
affiche_somme(4, 9)
affiche_somme(3, 7)
```
````

## Exercice {num2}`exercice-rev`

Que va afficher le programme?

Indiquez l'ordre d'exécution des lignes.

```{exec} python
:linenos:
def salutations(prenom):
  print("Bonjour", prenom)

def au_revoir():
  print("Au revoir à tous!")

salutations("Bob")
salutations("Alice")
au_revoir()
print("Fin du programme")
```

```{solution}
Python va lire les lignes 1 et 4 (les déclaration des définitions de fonctions
  sans s'occuper du corps de la fonction).

L'ordre d'exécution des lignes est le suivant:

7-2-8-2-9-5-10
```

## Exercice {num2}`exercice-rev:exo-1`

```{defaults} quiz-check
:randomize:
:class: grid-2
```

Qu'affiche le progamme suivant? Cochez la bonne réponse.
```{exec} python
:name: prog5.1
:when: never
:linenos:
def dessine_cochon():
  print(" ^---^")
  print("( 'o' )")
  print("( u u )")

def dessine_lapin():
  print("(\\ _ /)")
  print("( 'X' )")
  print("c(\")(\")")

def dessine_chat():
  print(" /\\_/\\")
  print("(=^.^=)")
  print("(\")(\")_/")

dessine_chat()
print()
dessine_lapin()
print()
dessine_cochon()
```
`````{quiz}
````{quiz-check}
- :
  ```{exec} python
  :after: prog5.1
  :when: load
  :class: hidden
  ```
- ```{exec} python
  :when: load
  :class: hidden
  def dessine_cochon():
    print(" ^---^")
    print("( 'o' )")
    print("( u u )")

  def dessine_lapin():
    print("(\\ _ /)")
    print("( 'X' )")
    print("c(\")(\")")

  def dessine_chat():
    print(" /\\_/\\")
    print("(=^.^=)")
    print("(\")(\")_/")

  dessine_cochon()
  print()
  dessine_lapin()
  print()
  dessine_chat()
  ```
- ```{exec} python
  :when: load
  :class: hidden
  print(" ^---^   (\\ _ /)   /\\_/\\")
  print("( 'o' )  ( 'X' )  (=^.^=)")
  print("( u u )  c(\")(\")  (\")(\")_/")
  ```
- ```{exec} python
  :when: load
  :class: hidden
  print(" /\\_/\\    (\\ _ /)   ^---^")
  print("(=^.^=)   ( 'X' )  ( 'o' )")
  print("(\")(\")_/  c(\")(\")  ( u u )")
  ```
````
`````

## Exercice {num2}`exercice-rev`

Créez un programme qui affiche un dessin choisi par l'utilisateur parmi trois
dessins prédéfinis.

{.lower-alpha-paren}
1.  Définissez au moins une fonction qui dessine un animal, un personnage,
    objet, ... Pour les deux autres, vous pouvez copiez les idées de l'{numref}`exercice %s<exercice-rev:exo-1>`.<br>
    Quelques idées ici: [https://www.momsarefrommars.com/cute-keyboard-characters.html](https://www.momsarefrommars.com/cute-keyboard-characters.html).
2.  Écrivez un programme qui demande à l'utilisateur de choisir entre trois
    possibilités et affichez le dessin correspondant. Demandez jusqu'à ce que la
    réponse de l'utilisateur soit valide.

````{tip}
:class: dropdown
Pour comparer des chaînes de caractères, il est préférable de convertir la
réponse en minuscule avant de la comparer, cela permet de réduire le nombre de
tests.

texte.lower()
: retourne une nouvelle chaîne de caractères écrite en minuscules.

```{exec} python
:editor:
reponse = input("Écrivez un mot avec des majuscules et des minuscules:")
print("La réponse donnée est:", reponse)
reponse_min = reponse.lower()
print("La réponse en minuscules est", reponse_min)
```
````

```{exec} python
:editor: c77dbb6e-922e-41a4-89be-09cedb1caf62
```

````{solution}
```{exec} python
:editor:
def dessine_cochon():
  print(" ^---^")
  print("( 'o' )")
  print("( u u )")

def dessine_lapin():
  print("(\\ _ /)")
  print("( 'X' )")
  print("c(\")(\")")

def dessine_chat():
  print(" /\\_/\\")
  print("(=^.^=)")
  print("(\")(\")_/")

choix = input("Quel animal voulez-vous dessinez entre chat, cochon et lapin?")
choix = choix.lower()
while choix != "chat" and choix != "cochon" and choix != "lapin":
  choix = input("Choisissez chat, cochon ou lapin")
  choix = choix.lower()
if choix == "chat":
  dessine_chat()
elif choix == "lapin":
  dessine_lapin()
elif choix == "cochon":
  dessine_cochon()
# Ce cas ne devrait jamais se produire, car la boucle while vérifie la réponse
else:
  print("Il n'y a pas de dessin correspondant.")
```
````
