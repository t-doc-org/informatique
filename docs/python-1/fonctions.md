% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Fonctions

## Introduction

En programmation, une **fonction** est un bloc de code (suite d'instructions)
permettant de réaliser une tâche donnée et auquel nous donnons un nom.

Nous en avons déjà rencontrées plusieurs:

- print(...): affiche sur la console ce qui est indiqué entre parenthèse
  ```{exec} python
  :when: never
  print("Hello world")
  ```
- input(...): demande à l'utilisateur d'entrer une donnée
  ```{exec} python
  :when: never
  prenom = input("Quel est ton prénom?")
  ```
- int(...): convertit ce qui est entre parenthèse en nombre entier
  ```{exec} python
  :when: never
  age = int(input("Quel est ton âge?))
  ```
- float(...): convertit ce qui est entre parenthèse en nombre à virgule
  ```{exec} python
  :when: never
  prix = float(input("Quel est le prix de l'article?""))
  ```
- range(...): renvoie une liste de nombres (de 0 à la valeur entre parenthèse - 1)
  ```{exec} python
  :when: never
  for _ in range(3):
    print("Bonjour!")
  ```

Toutes les fonctions ci-dessus sont des fonctions intégrées, elles ont été
prédéfinies pour nous. Nous pouvons les utilisez sans nous soucier de la manière
dont elles ont été implémentées.

## Modules

Un module est comme une boite à outils. Il contient plein de fonctions déjà
implémentées que nous pouvons utiliser. Par exemple, dans le module **math**, il
y a la fonction `sqrt(n)` qui permet de calculer la racine carré du nombre n,
ainsi que la constante &#960; notée `pi`. Dans le module **random**, la fonction
`randint(a, b)` permet de déterminer un nombre aléatoire entre a et b (inclus).

Avant de pouvoir utiliser une fonction d'un module, il faut l'importer ainsi:

```{exec} python
:when: never
from nom_du_module import nom_de_la_fonction
```

### Exemple {num}`ex-py1-fct`

```{exec} python
:editor:
# import des modules
from math import sqrt, pi
from random import randint

n = randint(1, 20)     # choisit un nombre aléatoire entre 1 et 20
print(n)
print(sqrt(40))        # calcule et affiche la racine carrée de 40
print(pi)              # affiche la valeur de la constante pi
```


## Définition et appel de fonctions

Comme vu dans l'introduction aux fonctions, il est possible de définir nos
propres fonctions. Cela permet notamment d'éviter les répétitions et de
découper un programme en plusieurs petites tâches plus faciles à résoudre. Ainsi
le code est plus lisible et plus facile à comprendre. Pour cela, il est
essentiel de choisir un nom de fonction qui explique ce qu'elle fait.

### Exemple {num}`ex-py1-fct`

```{exec} python
:editor:
# définition de la fonction
def calcule_et_affiche_aire_rectangle():
  cote_1 = 4
  cote_2 = 6
  aire = cote_1 * cote_2
  print(aire)

# appel de la fonction
calcule_et_affiche_aire_rectangle()
```

Cette fonction n'est pas très intéressante, car elle affiche toujours l'aire
d'un rectangle de côtés 4 et 6. Si je souhaite calculer l'aire d'un autre
rectangle, je dois définir une nouvelle fonction, ce qui n'est pas optimal.

Afin de modifier le comportement d'une fonction, nous pouvons utiliser des
paramètres (noms donnés aux éléments notés entre parenthèses dans la définition
de la fonction). Dans ce cours, l'appel de fonction se fera toujours avec le
même nombre d'arguments (valeurs des paramètres) et le même ordre que les
paramètres définis dans la fonction.

### Exemple {num}`ex-py1-fct`

```{exec} python
:editor:
# définition de la fonction
def calcule_et_affiche_aire_rectangle(cote_1, cote_2):
  aire = cote_1 * cote_2
  print(aire)

# appels de la fonction au moyen de valeurs numériques
calcule_et_affiche_aire_rectangle(10, 8)
calcule_et_affiche_aire_rectangle(2, 5.5)

largeur = 5
longueur = 12

# appel de la fonction au moyen des variables largeur et longueur
calcule_et_affiche_aire_rectangle(largeur, longueur)
```

De manière générale, la syntaxe de définition et d'appel de fonction est la
suivante:

```{exec} python
:when: never
# définition de la fonction
def nom_de_la_fonction(parametre_1, parametre_2, ...):
  # instruction 1
  # instruction 2
  # ...

# appel de la fonction
nom_de_la_fonction(valeur_du_parametre_1, valeur_du_parametre_2, ...)
```

```{tip}
Une fonction doit toujours être définie avant d'être appelée, c'est pourquoi il
est préférable de placer toutes les définitions de fonctions au début du
programme juste après les imports.
```

### Exercice {num}`exo-py1-fct`

1. Définissez une fonction `calcule_et_affiche_perimetre_carre()`.
2. Combien de paramètres sont-ils nécessaires?
3. Afficher le périmetre d'un carré de côté 7, de carré de côté 12, ainsi qu'en
   utilisant la variable `base`.

```{exec} python
:editor: 6871f44a-1dd8-4816-bb25-78b9e8e1e71b
# définition de la fonction
# complétez le code ici

base = 10

# appels de la fonction
# complétez le code ici
```


````{solution}
```{exec} python
# définition de la fonction
def calcule_et_affiche_perimetre_carre(cote):
  perimetre = 4 * cote
  print(perimetre)

base = float(input("Côté: "))

# appels de la fonction
calcule_et_affiche_perimetre_carre(7)
calcule_et_affiche_perimetre_carre(12)
calcule_et_affiche_perimetre_carre(base)
```
````

### Exercice {num}`exo-py1-fct`

Sans les exécutez, déterminer ce que vont afficher les programmes suivants.\
Font-ils ce qui est demandé?\
S'il y a une erreur, expliquez et corrigez le problème.

1.  Calculez l'aire d'un rectangle de côtés 20 et 100.

    ```{exec} python
    :editor:
    def calcule_et_affiche_aire_rectangle(largeur, longueur):
      aire = largeur * longueur
      print(aire)

    calcule_et_affiche_aire_rectangle(20, 100)
    ```

2.  Calculez l'aire d'un rectangle de côtés 40 et 15.

    ```{exec} python
    :editor:
    def calcule_et_affiche_aire_rectangle(largeur, longueur):
      aire = largeur * longueur
      print(aire)

    largeur = 40
    longueur = 15

    calcule_et_affiche_aire_rectangle(largeur, longueur)
    ```

3.  Calculez l'aire d'un rectangle de côtés 12 et 18.

    ```{exec} python
    :editor:
    def calcule_et_affiche_aire_rectangle(largeur, longueur):
      aire = largeur * longueur
      print(aire)

    base = 12
    hauteur = 18

    calcule_et_affiche_aire_rectangle(largeur, longueur)
    ```

4.  Calculez le prix d'un article qui coûte 35 CHF avec un rabais de 10%.

    ```{exec} python
    :editor:
    def calcule_et_affiche_pourcentage(prix, pourcentage):
      prix = (1 - pourcentage / 100) * prix
      print(prix)

    calcule_et_affiche_pourcentage(35, 10)
    ```

5.  Calculez le prix d'un article qui coûte 52 CHF avec un rabais de 15%.

    ```{exec} python
    :editor:
    def calcule_et_affiche_pourcentage(prix, pourcentage):
      prix = (1 - pourcentage / 100) * prix
      print(prix)

    calcule_et_affiche_pourcentage(15, 52)

6.  Calculez l'aire d'un carré de côté 9.

    ```{exec} python
    :editor:
    def calcule_et_affiche_aire_carre(cote):
      aire = cote ** 2
      print(aire)

    cote = 9
    calcule_et_affiche_aire_carre()
    ```

7.  Calculez l'aire d'un disque de rayon 4.

    ```{exec} python
    :editor:
    def calcule_et_affiche_aire_disque(rayon):
      aire = rayon ** 2 * pi
      print(aire)

    calcule_et_affiche_aire_disque(4)
    ```

````{solution}
1.  Correct.
2.  Correct.
3.  Pas correct. Les variables `largeur` et `longueur` ne sont pas définies dans
    le programme. Il faut modifier la ligne 8 par:
    ```{exec} python
    :when: never
    calcule_et_affiche_aire_rectangle(base, hauteur)
    ```
4.  Correct.
5.  Pas correct. Attention dans ce cas, l'ordre des paramètres a de
    l'importance. Il faut modifier la ligne 5 par:
    ```{exec} python
    :when: never
    calcule_et_affiche_pourcentage(52, 15)
    ```
6.  Pas correct. La fonction `calcule_et_affiche_aire_carre(cote)` a un
    paramètre. Lorsqu'on l'appelle, il est obligatoire de passer un argument. Il
    faut modifier la ligne 6 par:
    ```{exec} python
    :when: never
    calcule_et_affiche_aire_carre(cote)
    ```
7.  Pas correct. Il manque l'import de `pi` du module math. Il faut ajouter la
    ligne suivant au tout début de programme:
    ```{exec} python
    :when: never
    from math import pi
    ```
````

### Exercice {num}`exo-py1-fct`

Complétez les programmes suivants uniquement où il y a des `...`:

1.  Calculez le périmètre d'un rectangle de côtés 4 et 7.

    ```{exec} python
    :editor:
    def calcule_et_affiche_perimetre_rectangle(..., ...):
      perimetre = 2 * (longueur + largeur)
      print(perimetre)

    ... = 4
    ... = 7
    calcule_et_affiche_perimetre_rectangle(cote_1, cote_2)
    ```

2.  Calculez le périmètre d'un carré de côté 11.

    ```{exec} python
    :editor:
    def calcule_et_affiche_perimetre_carre(cote):
      perimetre = 4 * ...
      print(perimetre)

    c = 7
    calcule_et_affiche_perimetre_carre(11)
    ```

3.  Calculez le périmètre d'un cercle de rayon 5.

    ```{exec} python
    :editor:
    from math import *

    def calcule_et_affiche_perimetre_cercle(...):
      perimetre = 2 * r * pi
      print(perimetre)

    rayon = 5
    calcule_et_affiche_perimetre_cercle(...)
    ```

### Exercice {num}`exo-py1-fct`

Sans l'exécutez, déterminez ce que va afficher le programme suivant. Ensuite,
exécutez-le pour vérifier votre réponse.

```{exec} python
def mystery_1(z):
  z += 1
  print(z)

def mystery_2(x):
  x *= 2
  if x >= 0:
    mystery_1(x + 2)
  else:
    mystery_1(x)

y = 5
mystery_1(y)
mystery_2(y)
mystery_2(y - 10)
print(y)
```

### Exercice {num}`exo-py1-fct`

Sans l'exécutez, déterminez ce que va afficher le programme suivant. Ensuite,
exécutez-le pour vérifier votre réponse.

```{exec} python
def mystery_1(nombre):
    if nombre <= 4:
        print("A")
    if nombre >= 2:
        print("B")
    else:
        print("D")

def mystery_2(nombre):
    if nombre <= 4:
        print("A")
    elif nombre >= 2:
        print("B")
    else:
        print("D")

mystery_1(1)
mystery_2(1)
print("----")
mystery_1(3)
mystery_2(3)
print("----")
mystery_1(5)
mystery_2(5)
```

## Fonctions avec valeur de retour

Utiliser un `print()` dans une fonction n'est pas optimal, car il n'est ainsi
pas possible d'utiliser la valeur calculée. Il faudrait pouvoir "récupérer" la
valeur calculée. C'est ce que fait l'instruction `return` à la fin d'une
fonction.

### Exemple {num}`ex-py1-fct`

Nous souhaitons calculer l'aire totale de la figure grisée, en utilisant
s'inspirant de `calcule_et_affiche_aire_rectangle(largeur, longueur)`

```{image} images/rectangles.png
:alt: Aire de deux rectangles
:width: 30%
:align: center
```

```{exec} python
:editor:
def calcule_aire_rectangle(largeur, longueur):
  aire = largeur * longueur
  return aire                               # print(aire) -> return aire

aire_1 = calcule_aire_rectangle(2, 4)       # sauvegarder la valeur dans une variable
aire_2 = calcule_aire_rectangle(1, 3)       # sauvegarder la valeur dans une variable
print("L'aire totale vaut", aire_1 + aire_2)
```

### Exercice {num}`exo-py1-fct`

Sans l'exécutez, déterminez ce que va afficher le programme suivant. Ensuite,
exécutez-le pour vérifier votre réponse.

```{exec} python
:editor:
def mystery_1(z):
  z *= 2
  return z

def mystery_2(x):
  x -= 7
  if x < 0:
    return x
  else:
    return x % 2

y = 5
print(mystery_1(y))
print(mystery_2(y))
print(mystery_2(2 * y))
print(y // 2)
```

### Exercice {num}`exo-py1-fct`

Complétez le programme ci-dessous. Nous avons défini une fonction `majeur` pour
tester si une personne est majeur ou pas.

```{exec} python
:editor: d62933bb-5602-48e8-b92e-302c5857b135
def majeur(age):
  if ... :
    return True
  else:
    return False

# Demandez son âge à l'utiliateur
age = ...

if majeur(age):
  print("Tu as le droit de vote")
else:
  print("Tu pourras voter dans", ..., "ans.")
```

````{solution}
```{exec} python
def majeur(age):
  if age >= 18 :
    return True
  else:
    return False

# Demandez son âge à l'utiliateur
age = int(input("Quel âge as-tu?"))

if majeur(age):
  print("Tu as le droit de vote")
else:
  print("Tu pourras voter dans", 18 - age, "ans.")
```
````

### Exercice {num}`exo-py1-fct`

Écrivez un programme qui demande à l'utilisateur sa moyenne d'informatique tant
qu'elle n'est pas valide. Définissez une fonction pour tester si la note est valide,
c'est-à-dire si elle est comprise entre 1 et 6 inclus.\
Si la moyenne est inférieure à 4, affichez que la note est insuffisante.\
Si la moyenne est entre 4 et 4.8 (non inclus), affichez que la note est
suffisante, mais elle pourrait être meilleure.\
Si la moyenne est supérieure ou égale à 4.8 et inférieure à 5.5 (non inclus), affichez
que c'est du bon travail.\
Sinon affichez que c'est de l'excellent travail.

```{exec} python
:editor: a9063f2c-3b00-4f1b-aa04-1250ef31f054
# Écrivez le programme ici
```

````{solution}
```{exec} python
def note_valide(note):
  if 1 <= note <= 6 :
    return True
  else:
    return False

note = 0

while not(note_valide(note)):
  note = float(input("Moyenne d'informatique:"))

if note < 4:
  print("Note insuffisante.")
elif note < 4.8:
  print("Note suffisante, mais pourrait être meilleure.")
elif note < 5.5:
  print("Bon travail.")
else:
  print("Excellent travail!")
```
````

### Exercice {num}`exo-py1-fct`

Écrivez un programme qui permet de résoudre des équations du deuxième degré. Ce
programme doit afficher le nombre de solutions et les calculer.

```{exec} python
:editor: 71c23a46-21ab-4874-a8be-1928ea37c625
# Écrivez le programme ici
```

````{solution}
```{exec} python
from math import sqrt

def calcule_discriminant(a, b, c):
  return b ** 2 - 4 * a *c

# Demande à l'utilisateur les valeurs des coefficients a, b et c
a = float(input("Coefficient de x^2: "))
b = float(input("Coefficient de x: "))
c = float(input("Coefficient sans partie littérale: "))

if a == 0:
  print("Ce n'est pas une équation du deuxième degré.")
  print("La solution de l'équation est", -c / b)
else:
  delta = calcule_discriminant(a, b, c)

  if delta < 0:
    print("Cette équation n'a pas solution.")
  elif delta == 0:
    x = -b / (2 * a)
    print("Cette équation a une seule solution: x =", x)
  else:
    x_1 = (-b + sqrt(delta)) / (2 * a)
    x_2 = (-b - sqrt(delta)) / (2 * a)
    print("Cette équation a deux solutions: x_1 =", x_1, "et x_2 =", x_2)
```
````

### Exercice {num}`exo-py1-fct`

Écrivez un programme qui simule le fonctionnement d'un bancomat.
Vous devez créer 5 fonctions:

- `affiche_solde(solde)` qui affiche le solde qui se trouve sur le compte. Cette
fonction a un paramètre, le `solde` du compte.

- `solde_suffisant(montant, solde)` qui teste si le montant que l'utilisateur veut
retirer est suffisant sur le compte. Cette fonction a deux paramètres, le
`montant` que l'on veut débiter et le `solde` du compte. Elle doit renvoyer `True` ou
`False`.

- `retrait(solde)` qui effectue le retrait d'argent sur le compte. Cette fonction
a un paramètre, le `solde` du compte. Elle doit demander le `montant` à retirer à
l'utilisateur, tester si le solde est suffisant. Si c'est le cas, elle doit
créditer la somme sur le solde du compte. La fonction doit renvoyer le nouveau
`solde`.

- `depot(solde)` qui effectue le dépôt d'argent sur le compte. Cette fonction
a un paramètre, le `solde` du compte. Elle doit renvoyer le nouveau `solde`.

- `choix_options()` qui permet à l'utilisateur de choisir parmi les différentes
options. Cette fonction doit renvoyer un `choix` valide. Si le choix n'est pas
valide, redemandez à l'utilisateur.

Voici un exemple d'exécution:

```{code-block} text
Bancomat à votre disposition! Insérez votre carte.
Choisir parmi les options suivantes:
1 - Afficher le solde du compte
2 - Retirer de l'argent
3 - Déposer de l'argent
4 - Quitter
1
Le solde de votre compte est de 450.60 CHF.
Choisir parmi les options suivantes:
1 - Afficher le solde du compte
2 - Retirer de l'argent
3 - Déposer de l'argent
4 - Quitter
2
Combien voulez-vous retirez? 500
Ce montant n'est pas disponible, vous avez 450.60 CHF sur votre compte.
Choisir parmi les options suivantes:
1 - Afficher le solde du compte
2 - Retirer de l'argent
3 - Déposer de l'argent
4 - Quitter
2
Combien voulez-vous retirez? 100
Il vous reste 350.60 CHF sur votre compte.
Choisir parmi les options suivantes:
1 - Afficher le solde du compte
2 - Retirer de l'argent
3 - Déposer de l'argent
4 - Quitter
3
Combien voulez-vous déposer? 50
Vous avez 400.60 CHF sur votre compte.
Choisir parmi les options suivantes:
1 - Afficher le solde du compte
2 - Retirer de l'argent
3 - Déposer de l'argent
4 - Quitter
4
Au revoir!
```

```{exec} python
:editor: 3197cc87-208c-414f-a260-2f3761c69c9e
# Écrivez le programme ici
```

````{solution}
```{exec} python
from random import randint

def affiche_solde(solde):
  print("Le solde de votre compte est de", solde, "CHF.")

def solde_suffisant(montant, solde):
  if montant < solde:
    return True
  else:
    return False

def retrait(solde):
  montant = float(input("Combien voulez-vous retirez?"))
  if solde_suffisant(montant, solde):
    solde -= montant
    print("Il vous reste", solde, "CHF sur votre compte.")
  else:
    print("Ce montant n'est pas disponible, vous avez", solde, "CHF sur votre compte.")
  return solde

def depot(solde):
  montant = float(input("Combien voulez-vous déposer?"))
  solde += montant
  print("Vous avez", solde, "CHF sur votre compte.")
  return solde

def choix_options():
  print("Choisir parmi les options suivantes:")
  print("1 - Afficher le solde du compte")
  print("2 - Retirer de l'argent")
  print("3 - Déposer de l'argent")
  print("4 - Quitter")
  choix = int(input())
  while choix != 1 and choix != 2 and choix != 3 and choix != 4:
    choix = int(input("Le choix n'est pas valide. Choisissez entre 1, 2, 3 et 4."))
  return choix

print("Bancomat à votre disposition! Insérez votre carte.")
solde = randint(50, 600)
choix = 0
while choix != 4:
  choix = choix_options()
  if choix == 1:
    affiche_solde(solde)
  elif choix == 2:
    solde = retrait(solde)
  elif choix == 3:
    solde = depot(solde)
  print("-" * 30)
print("Au revoir!")
```
````

