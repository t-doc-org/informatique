<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# Révisions - Fonctions

En programmation, une fonction est un bloc de code (suite d'instructions) qui
réalise une tâche. Nous en avons déjà rencontré plusieurs:

print(...)
: affiche ce qui est entre parenthèses sur la console

input(...)
: demande à l'utilisateur d'entrer une donnée

int(...)
: convertit ce qui est entre parenthèses en nombre entier

float(...)
: convertit ce qui est entre parenthèses en nombre à virgule

range(...)
: renvoie une liste de nombre (de 0 à la valeur entre parenthèses -1)

Toutes les fonctions ci-dessus sont des fonctions intégrées, elles ont été
prédéfinies pour nous. Nous n'avons qu'à les utiliser, sans nous soucier de
comment elles ont été programmées.

Pour éviter de répéter du code et de rendre le code plus lisible, il est utile
de pouvoir définir nos propres fonctions. La syntaxe est la suivante:

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

## Exercice 15

Une fonction nommée `salutations` a été définie ci-dessous. Appeler cette
fonction dans le programme.

```{exec} python
:linenos:
:editable:
def salutations():
    print("Bonjour, comment vas-tu?")

# Compléter l'appel de la fonction
...
```

````{admonition} Solution
:class: note dropdown
```{exec} python
:linenos:
def salutations():
    print("Bonjour, comment vas-tu?")

# Appel de la fonction
salutations()
```
````

## Exercice 16

Une fonction nommée `affiche_somme` prend 2 paramètres numériques. Cette
fonction additionne les paramètres et affiche le résultat.

Appeler cette fonction 2 fois pour que le programme affiche le résultat de
4 + 9 et celui de de 3 + 7.

```{exec} python
:linenos:
:editable:
def affiche_somme(a, b):
    print(a + b)

# Compléter l'appel de la fonction 2 fois
...
```

````{admonition} Solution
:class: note dropdown
```{exec} python
:linenos:
def affiche_somme(a, b):
    print(a + b)

# Appel de la fonction 2 fois
affiche_somme(4, 9)
affiche_somme(3, 7)
```
````

## Exercice 17

Au début du code donné ci-dessous, définir une fonction nommée `au_revoir`
permettant simplement d'afficher le texte "À bientôt!".

Le code donné doit ensuite pouvoir s'exécuter sans problème afin d'afficher
20 fois le message d'au revoir.

```{exec} python
:linenos:
:editable:
# Définitir la fonction au_revoir
...

i = 0
while i < 20:
    au_revoir()
    i += 1
```

````{admonition} Solution
:class: note dropdown
```{exec} python
:linenos:
# Définition de la fonction au_revoir
def au_revoir():
    print("À bientôt!")

i = 0
while i < 20:
    au_revoir()
    i += 1
```
````

## Exercice 18

Au dessus du code donné, définir une fonction nommée `affiche_prix_billet`
prenant en paramètre l'âge de l'utilisateur et affichant le prix du billet de
cinéma en fonction de cet âge.

Le prix du billet est de 10 CHF pour les moins de 12 ans, de 14 CHF pour les
65 ans et plus et de 16 CHF pour les autres. La fonction affiche uniquement le
prix.

Le code donné doit ensuite pouvoir s'exécuter sans erreur et afficher exactement
les prix des billets pour tous les âges de 1 à 70 ans.

```{exec} python
:linenos:
:editable:
# Définir la fonction affiche_prix_billet
...

for a in range(1, 71):
    affiche_prix_billet(a)
```

````{admonition} Solution
:class: note dropdown
```{exec} python
:linenos:
def affiche_prix_billet(age):
    if a < 12:
        print(10)
    elif a >= 65:
        print(14)
    else:
        print(16)

for a in range(1, 71):
    affiche_prix_billet(a)
```
````
