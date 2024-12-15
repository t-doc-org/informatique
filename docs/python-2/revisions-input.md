% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Révisions - Entrée/Sortie

## Sortie

L'instruction de sortie permet d'afficher des informations sur l'écran. En
Python, cela se fait au moyen de la fonction `print(...)`.

```{exec} python
:linenos:
prenom = "Bob"
print("Salut", prenom, "!")
```

## Entrée

Une instruction d'entrée donne la main à l'utilisateur pour saisir une donnée au
clavier. En Python, cela se fait au moyen de la fonction `input(...)`. La valeur
saisie doit être obligatoirement affectée à une variable, sinon elle sera
perdue. La valeur rentrée par l'utilisateur est stockée sous forme de chaîne de
caractères (de type `str`). Pour effectuer des calculs, il faut la convertir en `int`
ou en `float`.

```{important}
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
jusqu'à ce que l'utilisateur saisisse une réponse et appuye sur {kbd}`Enter`.

## Exercice {num}`exo-py2-rev`

Compléter ce programme permettant de calculer l'aire d'un rectangle.

```{code-block} text
Demander à l'utilisateur la largeur.
Demander à l'utilisateur la longueur.
Calculer l'aire.
Afficher l'aire.
```

```{exec} python
:editor:
# Compléter le programme
largeur = await input_line(...)
longueur = await input_line(...)
aire =
print("L'aire vaut")
```

Tester le code avec les valeurs 3.6 et 6.4.

````{solution}
```{exec} python
:linenos:
# Ne pas oublier de convertir les inputs en float
largeur = float(await input_line("Quelle est la largeur du rectangle"))
longueur = float(await input_line("Quelle est la longueur du rectangle"))

# Calcul de l'aire
aire = largeur * longueur

# Affichage de la réponse
print("L'aire vaut", aire)
```
````

## Exercice {num}`exo-py2-rev`

Le programme ci-dessous devrait permettre de calculer l'année de naissance de
l'utilisateur. Mais, il contient au moins une erreur par ligne.\
Trouver et corriger toutes les erreurs.

```{exec} python
:editor:
# Corriger le programme
age = await input_line("Quel âge as-tu?")
annee = await input_line("En quelle année sommes-nous?")
print("Tu es né.e en" annee - age "ou en" annee - age - 1)
```

```{solution}
Ligne 2: l'âge doit être un nombre entier.\
Ligne 3: l'année doit aussi être un nombre entier.\
Ligne 4: Il manque des virgules entre les chaînes de caractères et les nombres
dans la parenthèse de la fonction print.
```

## Exercice {num}`exo-py2-rev`

Il y a des erreurs dans les programmes suivants. Expliquer et corriger le
problème.

1.  ```{exec} python
    :editor:
    # Programme qui demande son prénom à l'utilisateur
    # et lui dit bonjour en citant son prénom
    await input_line("Comment t'appelles-tu?")
    print("Bonjour")
    ```

    ```{solution}
    Lorsqu'on utilise la fonction `input_line()`, il est impératif de stocker la
    valeur dans une variable, sinon le input ne sert à rien.
    ```

2.  ```{exec} python
    :editor:
    # Programme qui demande son âge à l'utilisateur
    # et calcule son âge dans 10 ans
    age = await input_line("Quel âge as-tu?")
    print("Dans 10 ans, tu auras", age + 10)
    ```

    ```{solution}
    Lorsqu'on pose une question à l'utilisateur, la valeur retournée est une
    chaîne de caractère. Pour pouvoir faire des opérations mathématiques avec
    cette valeur, il est nécessaire de la convertir en `int()` ou en `float()`.
    ```
