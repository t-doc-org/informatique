% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Erreurs

```{metadata}
hide-solutions: true
```

En appuyant sur le bouton {kbd}`Run`, Python va d'abord **compiler** le
programme et ensuite l'**exécuter**.

## Compilation

Lors de la compilation, Python
- lit le code,
- vérifie qu'il ne comprend pas d'erreur de syntaxe,
- transforme le code en un langage compréhensible pour l'ordinateur.

## Exécution

L'exécution sera effectuée seulement s'il n'y a pas eu de problème pendant
la compilation. Python va exécuter les instructions du programme, suivant un
ordre bien défini.

En programmation, il existe trois types d'erreurs:
1. Les erreurs de syntaxe
2. Les erreurs d'exécution
3. Les erreurs de logique

## Erreur de syntaxe

Les erreurs de syntaxe sont détectées lors de la compilation. Python vérifie que
la syntaxe est correcte:
- les `:` sont présents et au bon endroit -> Sinon `SyntaxError`
- une parenthèse ouverte est toujours fermée -> Sinon `SyntaxError`
- un guillemet ouvert est toujours fermé -> Sinon `SyntaxError`
- l'indentation est correcte -> Sinon `IndentationError`
- ...

Si Python trouve une erreur de syntaxe, le programme s'arrête, car il ne
comprend pas le programme et ne peut donc pas l'exécuter. L'erreur est affichée
sur la console.

Exemple:

```{exec} python
:linenos:
:editable:
n = 7
if n < 10
  print("n est plus petit que 10.)
else:
  print("n est plus grand ou égal à 10."
```

## Erreur d'exécution

Les erreurs d'exécution sont détectée pendant l'exécution. La syntaxe est
correcte, mais une instruction lui demande de faire quelque chose qu'"illégal",
par exemple:
- une division par zero -> `ZeroDivisionError`
- accéder à la valeur d'une variable qui n'existe pas -> `NameError`
- appeler une fonction avec un nombre de paramètres incorrect -> `TypeError`

Si Python trouve une erreur d'exécution, il "plante", c'est-à-dire qu'il
s'arrête de manière abrupte.

Exemple:

```{exec} python
:linenos:
:editable:
a = 7
b = 0
print(a / b)
print(c)
```

## Erreur de logique

Python ne détecte aucune erreur, le programme est compilé et exécuté, mais le
résultat n'est pas celui attendu.

Exemple:

```{exec} python
:linenos:
:editable:
def addition(a, b):
  return a - b

c = addition(15, 18)
print(c)
```

## Exercice {num}`py2-erreur`

Les programmes suivants contiennent tous une erreur.
- Trouver l'erreur, si possible sans exécuter le programme.
- Déterminer son type (syntaxe, exécution, logique).
- La corriger.

1.  ```{exec} python
    :linenos:
    :editable:
    def calcule_aire(longueur, largeur):
      return longueur * largeur

    long = 10
    aire = calcule_aire(long, larg)
    print(aire)
    ```

2.  ```{exec} python
    :linenos:
    :editable:
    n = 0
    while n < 10:
    print(n)
    n += 2
    ```

3.  ```{exec} python
    :linenos:
    :editable:
    for i in range(9 / 2):
      print(i * 5)
    ```

4.  ```{exec} python
    :linenos:
    :editable:
    for i in range(2)
      print(i)
    ```


```{solution}
1. Erreur d'exécution: la variable larg n'est pas définie.
2. Erreur de syntaxe: l'indentation n'est pas correcte.
3. Erreur d'exécution: la fonction `range(...)` attend un nombre entier comme
   paramètre, mais 9/2 = 4.5.
4. Erreur de syntaxe: il manque les :.
```

## Exercice {num}`py2-erreur`

Il est souvent difficile de débugger un code qui ne fonctionne pas. En s'aidant
des messages d'erreurs affichés, corriger le programme ci-dessous qui calcule
l'aire et le périmètre d'un triangle isocèle et rectangle dont l'hypoténuse est
connu.


```{exec} python
:linenos:
:editable:
from math import sqrt

def calcule_hypotenuse(cathete1, cathete2)
  hypotenuse = sqrt(cathete1**2 + cathete2**2)
  return hypotenuse

def calcule_aire(base, hauteur):
  return base * hauteur / 2

def calcule_perimetre(cote1, cote2, cote3):
  return cote1 + cote2 - cote3

base = 500
demi_base = base / 2
cote = calcule_hypotenuse(demi_base, demi_base)
aire = calcule_aire(hypotenuse, demi_base)
perimetre = calcule_perimetre(base, cote, cote)
print("L'aire vaut" aire "et le périmètre vaut" perimetre)
```

```{solution}
Erreurs de syntaxe:
1. Ligne 3: `SyntaxError: expected ':'` -> il manque les 2 points à la fin de la
ligne.
2. Ligne 18: `SyntaxError: invalid syntax. Perhaps you forgot a comma?` -> il
manque une virgule entre la chaîne de caractère et le variable `aire`.

Erreur d'exécution:
1. Ligne 16: `NameError: name 'hypotenuse' is not defined` -> nous avons appelé
l'hypoténuse du triangle de départ `base`.

Erreur de logique:
1. Le calcul du périmètre n'est pas correct, il faut additionner les trois côtés.

```
