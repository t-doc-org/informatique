% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Erreurs

En appuyant sur le bouton {kbd}`Run`, Python va d'abord **compiler** le
programme et ensuite l'**exécuter**.

## Compilation

Lors de la compilation, Python
1. lit le code,
2. vérifie qu'il ne comprend pas d'erreur de syntaxe,
3. transforme le code en un langage compréhensible par l'ordinateur.

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
- les `:` sont présents et au bon endroit &rarr; Sinon `SyntaxError`
- une parenthèse ouverte est toujours fermée &rarr; Sinon `SyntaxError`
- un guillemet ouvert est toujours fermé &rarr; Sinon `SyntaxError`
- l'indentation est correcte &rarr; Sinon `IndentationError`
- ...

Si Python trouve une erreur de syntaxe, le programme s'arrête, car il ne
comprend pas le programme et ne peut donc pas l'exécuter. L'erreur est affichée
sur la console.

### Exemple {num1}`exemple`

```{exec} python
:editor:
n = 7
if n < 10
  print("n est plus petit que 10.)
else:
  print("n est plus grand ou égal à 10."
```

## Erreur d'exécution

Les erreurs d'exécution sont détectée pendant l'exécution. La syntaxe est
correcte, mais une instruction lui demande de faire quelque chose d'"illégal",
par exemple:
- une division par zero &rarr; `ZeroDivisionError`
- accéder à la valeur d'une variable qui n'existe pas &rarr; `NameError`
- appeler une fonction avec un nombre de paramètres incorrect &rarr; `TypeError`

Si Python trouve une erreur d'exécution, il "plante", c'est-à-dire qu'il
s'arrête de manière abrupte.

### Exemple {num1}`exemple`

```{exec} python
:editor:
a = 7
b = 0
print(a / b)
print(c)
```

## Erreur de logique

Python ne détecte aucune erreur, le programme est compilé et exécuté, mais le
résultat n'est pas celui attendu.

### Exemple {num1}`exemple`

```{exec} python
:editor:
def affiche_somme(a, b):
  print("La somme de", a, "et", b, "donne", a - b)

affiche_somme(15, 18)
```

## Exercices

### Exercice {num1}`exercice`

Les programmes suivants contiennent tous une erreur.
- Trouvez l'erreur, si possible sans exécuter le programme.
- Déterminez son type (syntaxe, exécution, logique).
- Corrigez-la.

1.  ```{exec} python
    :editor: 70746cc6-1686-423d-8665-570905cfc918
    def affiche_aire(longueur, largeur):
      print(longueur * largeur)

    long = 10
    affiche_aire(long, larg)
    ```

2.  ```{exec} python
    :editor: bba5d2de-9a45-4200-bdd2-802d9ac2a449
    n = 0
    while n < 10:
    print(n)
    n += 2
    ```

3.  ```{exec} python
    :editor: dc86de5e-ba35-4f9d-ba0e-c98a0520d8d4
    for i in range(9 / 2):
      print(i * 5)
    ```

4.  ```{exec} python
    :editor: 6c00a493-81ee-4ff5-854b-d7d844238e6d
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

### Exercice {num1}`exercice`

Le programme suivant contient une erreur de logique. Testez le programme avec
différentes valeurs pour la trouver et corrigez-la.

```{exec} python
:editor:
age = 18
if age >= 18:
  print("Tu payes le prix adulte.")
elif age >= 65:
  print("Tu payes le prix retraité")
else:
  print("Tu payes le prix enfant.")
```

```{solution}
Le `elif` ne sera jamais exécuté, car si l'âge est supérieur ou égal à 65, il
est aussi supérieur ou égal à 18. Donc la condition du `if` sera vérifiée.
```

### Exercice {num1}`exercice`

Il est souvent difficile de débugger un code qui ne fonctionne pas. En s'aidant
des messages d'erreurs affichés, corrigez le programme ci-dessous qui calcule
l'aire et le périmètre d'un triangle isocèle et rectangle dont l'hypoténuse est
connu.

```{image} images/triangle_iso_rect.png
:alt: Triangle isocèle rectangle
:width: 50%
:align: center
```

```{exec} python
:editor: 36bcae3e-b90a-40b1-bac0-33bea021bc99
from math import sqrt

def affiche_aire(base, hauteur)
  aire_triangle = base * hauteur
  print("L'aire vaut", aire_triangle)

def affiche_perimetre(cote1, cote2, cote3):
  perimetre = cote1 + cote2 + cote3
  print("Le périmètre vaut" perimetre)

base = 500
cathete = base / 2
cote = sqrt(cathete**2 + cathete**2)
aire = affiche_aire(base, hauteur)
perimetre = affiche_perimetre(base, cote, cote)
```

```{solution}
Erreurs de syntaxe:
1.  Ligne 3: `SyntaxError: expected ':'` &rarr; il manque les 2 points à la fin
    de la ligne.
2.  Ligne 9: `SyntaxError: invalid syntax. Perhaps you forgot a comma?` &rarr;
    il manque une virgule entre la chaîne de caractère et le variable `perimetre`.

Erreur d'exécution:
1.  Ligne 14: `NameError: name 'hauteur' is not defined` &rarr; la variable
`hauteur` n'est pas définie, elle correspond à la variable `cathete`.

Erreur de logique:
1.  Le calcul d'aire n'est pas correct, pour un rectangle la formule est
    $\dfrac{base \cdot hauteur}{2}$.

Résultat correct:\
L'aire vaut 62500.0\
Le périmètre vaut 1207.1067811865476
```
