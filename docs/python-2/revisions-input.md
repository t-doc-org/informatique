<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# Révisions - Entrées/Sorties

## Sortie

L'instruction de sortie permet d'afficher des informations sur l'écran. En
Python, cela se fait au moyen de la fonction `print(...)`.

```{exec} python
:linenos:
prenom = "Bob"
print("Salut", prenom, "!")
```

## Entrées

Une instruction d'entrée donne la main à l'utilisateur pour saisir une donnée au
clavier. En Python, cela se fait au moyen de la fonction `input(...)`. La valeur
saisie doit être obligatoirement affectée à une variable, sinon elle sera
perdue. La valeur rentrée par l'utilisateur est stockée sous forme de chaîne de
caractères (de type `str`). Pour effectuer des calculs, il faut la convertir en `int`
ou en `float`.



```{Important}
L'utilisation de la fonction input sur ce site est différente de ce que vous
avez faite d'habitude.\
`nom_variable = await input_line("...")`
```

```{exec} python
:linenos:
age = int(await input_line("Quel âge as-tu?"))
print("Dans 10 ans, tu auras", age + 10, "ans.")
```

Lors de l'exécution de la ligne 1, la question est affichée. Le programme attend
jusqu'à ce que l'utilisateur saisisse une réponse et appuye sur {kbd}`enter`.

## Exercice 5

Compléter ce programme permettant de calculer le périmètre d'un rectangle.

```{code-block} text
Demander à l'utilisateur la largeur.
Demander à l'utilisateur la longueur.
Calculer le périmètre.
Afficher le périmètre.
```

```{exec} python
:editable:
:linenos:
# Compléter le programme
largeur = await input_line(...)
longueur = await input_line(...)
perimetre =
print("Le périmètre vaut")
```

Tester le code avec les valeurs 3.6 et 6.4.

````{admonition} Solution
:class: note dropdown
```{exec} python
:linenos:
# Ne pas oublier de convertir les inputs en float
largeur = float(await input_line("Quelle est la largeur du rectangle"))
longueur = float(await input_line("Quelle est la longueur du rectangle"))

# Calcul du périmètre
perimetre = (largeur + longueur) * 2

# Affichage de la réponse
print("Le périmètre vaut", perimetre)
```
````

## Exercice 6

Le programme ci-dessous devrait permettre de calculer l'année de naissance de
l'utilisateur. Mais, il contient au moins une erreur par ligne.\
Trouver et corriger toutes les erreurs.

```{exec} python
:editable:
:linenos:
# Corriger le programme
age = await input_line("Quel âge as-tu?")
annee = await input_line("En quelle année sommes-nous?")
print("Tu es né.e en" annee - age "ou en" annee - age - 1)
```


