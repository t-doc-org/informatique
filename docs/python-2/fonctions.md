% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Fonctions

En programmation, une **fonction** est une bloc de code (suite d'instructions)
permettant de réaliser une tâche donnée et auquel nous donnons un nom. Cela
permet de découper un programme en plusieurs petites tâches plus facile à
résoudre. Ainsi le code est plus lisible et plus facile à comprendre. Pour cela,
il est essentiel de choisir un nom de fonction qui explique ce qu'elle fait.

```{tip}
Une fonction doit toujours être définie avant d'être appelée, c'est pourquoi il
est préférable de placer toutes les définitions de fonctions au début du
programme (après les imports et les définitions de variables globales).
```

## Exemple 1

Fonction qui affiche la table de multiplication de 5:

```{exec} python
:linenos:
# définition de la fonction
def table_multiplication_5():
    for i in range(1, 11):
        print(5, "*", i, "=", 5 * i)

# appel de la fonction
table_multiplication_5()
```

Le problème de cette fonction est que pour afficher la table de  multiplication
de 6, il est nécessaire d'écrire une nouvelle fonction. Cela peut être amélioré
en utilisant des paramètres.

## Fonctions avec paramètres

Un **paramètre d'une fonction** est une variable définie dans la fonction qui
recevra une valeur lors de chaque appel de la fonction. Ainsi le comportement
d'une fonction varie suivant les valeurs de ses paramètres.

## Exemple 2

Fonction qui affiche n'importe quelle table de multiplication:

```{exec} python
:editable:
:linenos:
def table_multiplication(n):
    for i in range(1, 11):
        print(n, "*", i, "=", n * i)

nombre = 6                      # changer le valeur du nombre ici
table_multiplication(nombre)
```

## Exemple 3

```{exec} python
:linenos:
# Calcule et affiche le discriminant dans la résolution d'équation du 2e degré
def discriminant(a, b, c):
    delta = b ** 2 - 4 * a * c
    print("Le discriminant est:", delta)

# Demande à l'utilisateur les valeurs des coefficients a, b et c
a = float(await input_line("Coefficient de x^2: "))
b = float(await input_line("Coefficient de x: "))
c = float(await input_line("Coefficient sans partie littérale: "))

discriminant(a, b, c)
```

La fonction ainsi écrite affiche le discriminant, mais il n'est pas possible
d'utiliser la valeur. Ce qui pose problème pour calculer les solutions si
elle(s) existe(nt).

## Fonctions avec valeur de retour

La commande `return` permet de renvoyer le résultat d'une fonction et ainsi
pouvoir le réutiliser dans la suite du programme. Pour cela, il est nécessaire
de sauvegarder la valeur retournée dans une variable.

## Exercice 1

Modifier le code de l'exemple 3, pour afficher le nombre de solution de
l'équation. Rappel: si $\Delta < 0$, il n'y a pas de solution, si $\Delta = 0$,
il y a une solution et si $\Delta > 0$, il y a 2 solutions.

```{exec} python
:linenos:
:editable:
# écrire le programme ici
```

````{admonition} Solution
:class: note dropdown
```{exec} python
:linenos:
# Calcule le discriminant dans la résolution d'équation du 2e degré
def discriminant(a, b, c):
    return b ** 2 - 4 * a * c

# Demande à l'utilisateur les valeurs des coefficients a, b et c
a = float(await input_line("Coefficient de x^2: "))
b = float(await input_line("Coefficient de x: "))
c = float(await input_line("Coefficient sans partie littérale: "))

delta = discriminant(a, b, c)

if delta > 0:
    print("Cette équation a deux solutions.")
elif delta == 0:
    print("Cette équation a une solution.")
else:
    print("Cette équation n'a pas de solution.")
```
````

## Exercice 2

Compléter le code de l'exercice 1, pour calculer les solutions de l'équation.

````{tip}
Pour calculer la racine carrée d'un nombre, il faut utiliser la fonction
`sqrt()` qui se trouve dans le module math. Il est donc nécessaire d'importer ce
module:

```{exec} python
:linenos:
from math import sqrt
```
````

````{admonition} Solution
:class: note dropdown
```{exec} python
:linenos:
from math import sqrt

# Calcule le discriminant dans la résolution d'équation du 2e degré
def discriminant(a, b, c):
    return b ** 2 - 4 * a * c

# Demande à l'utilisateur les valeurs des coefficients a, b et c
a = float(await input_line("Coefficient de x^2: "))
b = float(await input_line("Coefficient de x: "))
c = float(await input_line("Coefficient sans partie littérale: "))

delta = discriminant(a, b, c)

if delta > 0:
    x_1 = (-b + sqrt(delta)) / (2 * a)
    x_2 = (-b - sqrt(delta)) / (2 * a)
    print("Cette équation a deux solutions: x_1 =", x_1, "et x_2 =", x_2)
elif delta == 0:
    x = -b / (2 * a)
    print("Cette équation a une solution: x =", x)
else:
    print("Cette équation n'a pas de solution.")
```
````

## Exercice 3

Écrire une fonction qui permet de convertir des bits en octets et une autre
fonction qui convertit des octets en bits.

```{exec} python
:linenos:
:editable:
# écrire le programme ici
```


````{important}
`return` interrompt la fonction. Tout ce qui se trouve dans la fonction, mais
après le `return` sera ignoré.

```{exec} python
:linenos:
def double(x):
    return 2*x
    print("Ce texte ne s'affichera pas.")

print(double(5))
print("Fin du programme")
```
````
