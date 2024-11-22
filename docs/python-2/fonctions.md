% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Fonctions

```{metadata}
hide-solutions: true
```

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
    for i in range(1, 11):              # i prend les valeurs de 1 à 10
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

1. Déterminer ce que font les programmes suivants.
2. Corriger les erreurs.

```{exec} python
:linenos:
:editable:
def convertit_min_sec(min):
    return min * 60

convertit_min_sec(145)
print("145 minutes donnent", nb_sec, "secondes.")
```

```{exec} python
:linenos:
:editable:
def convertit_sec_min(sec):
    min = sec / 60

nb_minutes = convertit_sec_min(38700)
print("38700 secondes donnent", nb_minutes, "minutes.")
```

```{exec} python
:linenos:
:editable:
def calcule_double_moins_trois(x):
    x = 2 * x
    return x
    x = x - 3

print(calcule_double_moins_trois(4))
```

````{solution}
```{exec} python
:linenos:
def convertit_min_sec(min):
    return min * 60

nb_secondes = convertit_min_sec(145)
print("145 minutes donnent", nb_secondes, "secondes.")
```

```{exec} python
:linenos:
:editable:
def convertit_sec_min(sec):
    return sec / 60

nb_minutes = convertit_sec_min(38700)
print("38700 secondes donnent", nb_minutes, "minutes.")
```

```{exec} python
:linenos:
:editable:
def calcule_double_moins_trois(x):
    x = 2 * x
    x = x - 3
    return x

print(calcule_double_moins_trois(4))
```
````

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

## Exercice 2

Modifier le code de l'exemple 3, pour afficher le nombre de solutions de
l'équation.\
Rappel:
- si $\Delta < 0$, il n'y a pas de solution,
- si $\Delta = 0$, il y a une solution,
- si $\Delta > 0$, il y a 2 solutions.

```{exec} python
:linenos:
:editable:
# Écrire le programme ici
```

````{solution}
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

## Exercice 3

Compléter le code de l'exercice 1, pour calculer les solutions de l'équation.

````{tip}
Pour calculer la racine carrée d'un nombre, il faut utiliser la fonction
`sqrt()` qui se trouve dans le module math. Il est donc nécessaire d'importer ce
module:

```{exec} python
:linenos:
from math import sqrt

print(sqrt(54))
```
````

````{solution}
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

## Exercice 4

1. Écrire une fonction qui convertit des bits en octets.
2. Écrire une fonction qui convertit des octets en bits.
3. Convertir 3664000 bits en octets.
4. Convertir 512 octets en bits.

```{exec} python
:linenos:
:editable:
# Écrire le programme ici
```

````{solution}
```{exec} python
:linenos:
# Convertis des bits en octets
def conversion_bits_octets(a):
    return a / 8

# Convertis des bits en octets
def conversion_octets_bits(a):
    return a * 8

nb_octets = conversion_bits_octets(3664000)
print("La conversion de 3664000 bits en octets donne", nb_octets)

nb_bits = conversion_octets_bits(512)
print("La conversion de 512 octets en bits donne", nb_bits)

```
````

## Exercice 5

Pour calculer l'aire totale de la figure ci-dessous:

1. Écrire une fonction qui permet de calculer l'aire d'un rectangle en
connaissant la longueur et la largeur.
2. Calculer l'aire totale de la figure.

```{image} images/aire-rectangles.png
:alt: Aire totale
:width: 30%
:align: center
```

```{exec} python
:linenos:
:editable:
# Écrire le programme ici
```

````{solution}
```{exec} python
:linenos:
def calcule_aire_rectangle(longueur, largeur):
    return longueur * largeur

aire_rectangle_1 = calcule_aire_rectangle(7.5, 3.4)
aire_rectangle_2 = calcule_aire_rectangle(5.8, 3.4)
aire_totale = aire_rectangle_1 + aire_rectangle_2
print("Aire totale:", aire_totale)
```
````

## Exercice 6

Pour les prochaines vacances, tu décides de partir en vacances au Japon. Tu as
de l'argent sur ton compte épargne et l'argent que tu vas gagner en travaillant
cet été.

Écrire un programme qui permet de convertir en YEN les montants qui sont sur un
compte épargne et sur un compte courant afin de déterminer le montant que tu
auras à disposition.\
Le taux est de 1 CHF = 174 YEN.

```{exec} python
:linenos:
:editable:
# Compléter la fonction
def convertit_chf_en_yen(montant_chf):

compte_courant_chf = 1540
compte_epargne_chf = 2467

budget_yen =
print("Tu auras", budget_yen, "YEN.")
```

````{solution}
```{exec} python
:linenos:
# Compléter la fonction
def convertit_chf_en_yen(montant_chf):
    taux_conversion = 174
    return montant_chf * taux_conversion


compte_courant_chf = 1540
compte_epargne_chf = 2467

budget_yen = convertit_chf_en_yen(1540) + convertit_chf_en_yen(2467)
print("Tu auras", budget_yen, "YEN.")
```
````

## Exercice 7

Écrivez une fonction qui prend en paramètre un code de réduction et retourne le
pourcentage de rabais donné par ce code de réduction. Le code déjà donné utilise
cette fonction pour calculer le prix final d'un article après y avoir appliqué
la réduction. Les réductions sont les suivantes :
- 20% (0.2) pour le code SUN
- 35% (0.35) pour le code STX
- 50% (0.5) pour le code MAX
- 0% (0) pour les autres codes

```{exec} python
:linenos:
:editable:
# Compléter le programme
prix = float(await input_line("Quel est le prix de l'article ?"))
code = await input_line("Quel est le code de réduction ?")

reduction = calcule_reduction(code)
prix_final = prix * (1 - reduction)
print("Le prix final est de", prix_final, "CHF.")
```

````{solution}
```{exec} python
:linenos:
def calcule_reduction(code):
    if code == "SUN":
        return 0.2
    elif code == "STX":
        return 0.35
    elif code == "MAX":
        return 0.5
    else:
        return 0

prix = float(await input_line("Quel est le prix de l'article ?"))
code = await input_line("Quel est le code de réduction ?")

reduction = calcule_reduction(code)
prix_final = prix * (1 - reduction)
print("Le prix final est de", prix_final, "CHF.")
```
````

## Exercice 8

Pour calculer le prix de l'amende à payer en cas de dépassement de vitesse,
consulte le document suivant.
% Ajouter le lien sur le document

Ecrire une fonction qui retourne le prix de l'amende à payer en fonction de la
vitesse autorisée et la vitesse mesurée par le radar. Traiter seulement le cas
où le dépassement de vitesse a lieu sur l'autoroute et n'exède pas 20 km/h.

```{exec} python
:linenos:
:editable:
# Compléter le programme
def amende(vit_aut, vit_mes):
    pass

print(amende(120,140))
print(amende(120,145))
print(amende(120,120))
```

````{solution}
```{exec} python
:linenos:
def amende(vit_aut, vit_mes):
    depassement = vit_mes - vit_aut
    if depassement <= 0:
        return 0
    elif depassement <= 5:
        return 20
    elif depassement <= 10:
        return 60
    elif depassement <= 15:
        return 120
    elif depassement <= 20:
        return 180
    elif depassement <= 25:
        return 260
    else:
        return -100

print(amende(120,140))
print(amende(120,145))
print(amende(120,120))
```
````

## Exercice 9

La suite de Syracuse est une suite d'entiers naturels définie de la manière
suivante:

si le nombre est pair, on le divise par 2, sinon on le multiplie par 3 et on lui
ajoute 1.

Cette suite à la particularité de toujours terminé se terminer par 4, 2, 1.

Écrire un programme qui permet d'afficher la suite de nombre jusqu'à ce qu'on
arrive au nombre 1.

```{exec} python
:linenos:
:editable:
# Écrire le programme ici
```

````{solution}
```{exec} python
:linenos:
def syracuse(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

n = int(await input_line("Choisir un nombre entier plus grand que 0."))

while n != 1:
    n = syracuse(n)
    print(n)

```
````


