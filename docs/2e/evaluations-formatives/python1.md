% Copyright 2026 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Python 1

```{include} /_include/entete-examen.export.md
```
```{class} align-center
**Détails des calculs obligatoires. Attention au soin. Calculatrice autorisée.**
```
---

## Question {nump}`question`{points}`2`

```{exec} python
:when:
:linenos:
print(19 % 3)
print(19 // 3)
print(4 ** 3)
print(16 / 3)
```

Qu'affiche le programme ci-dessus?
{vspace}`4lh`

````{solution}
Le programme va afficher:
```{code-block} text
1
6
64
5.333333333333333
```
````

## Question {nump}`question`{points}`3`

```{exec} python
:when:
:linenos:
x = 4
y = 1
if x < 0 and y < 0:
  x += 7
elif x < 5 and y < 0:
  x -= 3
elif x < 5 or y < 0:
  x *= 6
else:
  x = 100
y = 100
print("La valeur de x est", x, "et celle de y est", y, ".")
```

{.lower-alpha-paren}
1.  Qu'affiche le programme ci-dessus?
    {vspace}`5lh`
2.  Indiquez l'ordre dans lequel les instructions seront exécutées (numéros de
    lignes).
    {vspace}`2lh`

````{solution}
{.lower-alpha-paren}
1.  Le programme va afficher:
    ```{code-block} text
    La valeur de x est 24 et celle de y est 100.
    ```
2. Ordre d'exécution de lignes: 1-2-3-5-7-8-11-12
````

## Question {nump}`question`{points}`3`

```{exec} python
:when:
:linenos:
a = 5
b = 7
while a < 12:
  if a % 2 != 0:
    b -= 1
  else:
    b -= 2
  a += 3
  print(a, b)
a = b * 2
b = 1
print(a, b)
```

Qu'affiche le programme ci-dessus?
{vspace}`6lh`

````{solution}
Le programme va afficher:
```{code-block} text
8 6
11 4
14 3
6 1
```
````

## Question {nump}`question`{points}`3`

```{exec} python
:when:
:linenos:
resultat = 4
for i in range(6):
  print(i)
  resultat += i
print("Le résultat est de", resultat, ".")
```

Qu'affiche le programme ci-dessus?
{vspace}`8lh`

````{solution}
Le programme va afficher:
```{code-block} text
0
1
2
3
4
5
Le résultat est de 19
```
````

## Question {nump}`question`{points}`6`

Le programme suivant contient trois erreurs:

{.lower-alpha-paren}
1.  Pour chaque erreur, indiquez la ligne, son type et expliquez le problème.
2.  Corrigez les erreurs.

```{exec} python
:when:
:linenos:
age = input("Quel est ton âge?")
if age <= 18:
    print("Tu es mineur.")
else  age > 18:
    print("Tu es majeur.")
```

````{solution}
{.lower-alpha-paren}
1.  Ligne 1: erreur d'exécution. La variable `age` est un nombre entier et doit
    être castée avec `int(...)`.<br>
    Ligne 2: erreur de logique. À 18 ans, on est majeur et plus mineur.<br>
    Ligne 4: erreur de syntaxe. Il ne doit pas y avoir de condition après le
    else.
2.  ```{exec} python
    :when:
    :linenos:
    age = int(input("Quel est ton âge?"))
    if age < 18:
        print("Tu es mineur.")
    else:
        print("Tu es majeur.")
    ```
````

## Question {nump}`question`{points}`4`

Écrivez un programme qui demande à l'utilisateur un nombre entier entre 5 et 12
et affiche les 10 premiers multiples de ce nombre.

````{solution}
```{exec} python
:when: click
nombre = int(input("Choisir un nombre entre 5 et 12:"))
for i in range(1, 11):
  print(nombre * i)
```
````

## Question {nump}`question`{points}`5`

Écrivez un programme qui compte de 3 en 3 à partir de 5 et jusqu'à 25. Utilisez
des variables pour la valeur de départ (dans l'exemple le 5), la valeur
d'arrivée (25) et la valeur du pas (3).

Exemple d'exécution:
```{exec} python
:after: comptage
:when: load
:class: hidden
```

````{solution}
```{exec} python
:name: comptage
:when: click
depart = 5
arrivee = 25
saut = 3
while depart <= arrivee:
  print(depart)
  depart += saut
print("J'ai fini de compter!")
```
````

## Question {nump}`question`{points}`6`

Complétez le programme ci-dessous en écrivant:

{.lower-alpha-paren}
1.  une fonction depot qui prend en paramètre le solde et retourne le solde
    après le dépôt.<br>
    Cette fonction demande le montant à déposer à l'utilisateur et l'ajoute au
    solde.
2.  une fonction retrait qui prend en paramètre le solde et retourne le solde
    après le retrait.<br>
    Cette fonction:
      - demande le montant à retirer à l'utilisateur,
      - teste si le solde est suffisant avant de l'enlever au solde.
3. Faites ensuite un retrait de 80 CHF et suivi d'un dépôt de 145 CHF.

```{exec} python
:when:
:linenos:
def solde_suffisant(montant, solde):
    if montant <= solde:
        return True
    else:
        return False
########## Ne pas modifier le code ci-dessus ##########

def depot(solde):
    # compléter la fonction

def retrait(solde):
    # compléter la fonction

solde = 1000
                                                              # faite un retrait de 80 CHF
                                                              # faite un dépôt de 145 CHF
print("Le solde est de", solde, "CHF.")
```

````{solution}
```{exec} python
:when: click
def solde_suffisant(montant, solde):
    if montant <= solde:
        return True
    else:
        return False
########## Ne pas modifier le code ci-dessus ##########

def depot(solde):
  montant = float(input("Combien voulez-vous déposer?"))
  solde += montant
  print("Vous avez", solde, "CHF sur votre compte.")
  return solde

def retrait(solde):
  montant = float(input("Combien voulez-vous retirez?"))
  if solde_suffisant(montant, solde):
    solde -= montant
    print("Il vous reste", solde, "CHF sur votre compte.")
  else:
    print("Ce montant n'est pas disponible, vous avez", solde, "CHF sur votre compte.")
  return solde

solde = 1000
solde = retrait(solde)                          # faite un retrait de 80 CHF
solde = depot(solde)                            # faite un dépôt de 145 CHF
print("Le solde est de", solde, "CHF.")
```
````
