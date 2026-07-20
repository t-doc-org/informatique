% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
solutions: show
```

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
