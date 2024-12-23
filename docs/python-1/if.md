% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Instructions conditionnelles

```{metadata}
hide-solutions: true
```

Une instruction conditionnelle est composée d'une **condition** puis d'un
**bloc d'instructions**. La condition est une expression ou une variable logique
évaluée par `True` ou `False`. Le bloc d'instructions s'exécute seulement si la
condition est vérifiée.

## Opérateurs de comparaison

Les opérateurs de comparaison permettent de comparer deux valeurs entre elles.
Le résultat de la comparaison est de type booléen: True ou False.

| Opérateur | Nom                  | Exemple | Résultat |
| :-------: | :------------------: | :-----: | :------: |
| ==        | égal à               | 3 == 7  | False    |
| !=        | différent de         | 3 != 7  | True     |
| >         | plus grand que       | 3 > 7   | False    |
| <         | plus petit que       | 3 < 7   | True     |
| >=        | plus grand ou égal à | 3 >= 7  | False    |
| <=        | plus petit ou égal à | 3 <= 7  | True     |

## Exercice {num}`exo-py1`

Est-ce que les expressions suivantes sont `True` (vrai) ou `False` (faux)?

1.    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("1 + 1 == 2")
      if resp.replace(" ", "").lower() == "true" or resp.replace(" ", "").lower() == "vrai": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

2.    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("2 * 3 == 3")
      if resp.replace(" ", "").lower() == "false" or resp.replace(" ", "").lower() == "faux": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```
3.    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("2 + 3 != 4")
      if resp.replace(" ", "").lower() == "true" or resp.replace(" ", "").lower() == "vrai": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

4.    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("14 >= 15")
      if resp.replace(" ", "").lower() == "false" or resp.replace(" ", "").lower() == "faux": break
      print("\x0cEssaie encore")
    print("\x0cBravo")

5.    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("2 ** 3 == 6")
      if resp.replace(" ", "").lower() == "false" or resp.replace(" ", "").lower() == "faux": break
      print("\x0cEssaie encore")
    print("\x0cBravo")

6.    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("13 >= 13")
      if resp.replace(" ", "").lower() == "true" or resp.replace(" ", "").lower() == "vrai": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

## Exemple avec if

Le bloc d'instructions ne sera exécuté que si la condition est vraie.

```{figure} images/if.png
:alt: Ordinogramme if
:width: 300px
:align: center
```

```{exec} python
:editor:
print("Début")
meteo = "soleil"
if meteo == "pluie":
  print("Je prends un parapluie.")
print("Fin")
```

Dans l'exemple ci-dessus, il ne se passe rien, la condition n'est pas vérifiée.\
Changez la valeur de la variable `meteo` en "pluie". Que se passe-t-il?

## Exemple avec if ... else

Le bloc d'instructions après le `if` sera exécuté si la condition est vraie,
sinon ce sera le bloc d'instructions du `else` qui sera exécuté.

```{figure} images/if-else.png
:alt: Ordinogramme if-else
:width: 500px
:align: center
```

```{exec} python
:editor:
moyenne = 5
if moyenne >= 4:
  print("Moyenne suffisante")
else:
  print("Moyenne insuffisante")
```

Dans l'exemple ci-dessus, soit la moyenne est suffisante (moyenne supérieure ou
égale à 4), soit elle est insuffisante (moyenne inférieure à 4). Il n'y a pas
d'autres possibilités. Changez la valeur de la variable `moyenne` en 3. Que se
passe-t-il?

## Exemple avec if ... elif ... else

Certaines situations nécessitent de distinguer plus qu'un ou deux cas.

```{figure} images/if-elif-else.png
:alt: Ordinogramme if-elif-else
:width: 100%
:align: center
```

```{exec} python
:editor:
type_film = "comédie"

if type_film == "action":
  print("Explosions et des cascades de folie!")
elif type_film == "comédie":
  print("Mort de rire!")
elif type_film == "horreur":
  print("Terrifiant!")
else:
  print("Je ne connais pas.")
```

Dans l'exemple ci-dessus, il y a le choix entre trois types de films (action,
comédie et horreur). Le branchement `else` gérera tous les autres cas. Remplacer
la valeur de la variable `type_film` par "action", "horreur" ou "drame". Que se
passe-t-il?


## Exercice {num}`exo-py1`

Écrivez l'algorithme suivant en Python:

```{code-block} text
Demander à l'utilisateur d'entrer un nombre positif
Sauvegarder la valeur dans la variable a
Si a est plus petit que 0 alors
  écrire "Ce nombre n’est pas positif."
```

```{exec} python
:editor: f0cd9039-aa2a-4a6e-a855-ad51d4cd557e
a = float(await input_line("Entrez un nombre positif: "))
# Complétez le programme ici
```

````{solution}
```{exec} python
:linenos:
a = float(await input_line("Entrez un nombre positif: "))
if a < 0:
  print("Ce nombre n'est pas positif.")
```
````

## Exercice {num}`exo-py1`

Écrivez l'algorithme suivant en Python:

```{code-block} text
Demander à l'utilisateur d'entrer la valeur de a
Sauvegarder la valeur dans la variable a
Demander à l'utilisateur d'entrer la valeur de b
Sauvegarder la valeur dans la variable b
Si a est plus petit que b alors
  écrire "a est plus petit que b"
Sinon
  écrire "a est plus grand que b"
```

```{exec} python
:editor: 3d40e18b-534c-48ae-a1a3-025ad03f9392
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
a = float(await input_line("Valeur de a: "))
b = float(await input_line("Valeur de b: "))
if a < b:
  print("a est plus petit que b.")
else:
  print("a est plus grand que b.")
```
````

## Exercice {num}`exo-py1`

Reprenons l'exercice précédent. Que se passe-t-il si a = 0?

Améliorez le programme précédent en traitant aussi le cas où a = 0.

```{exec} python
:editor: d5a6da62-0c1a-4ea7-a1b2-910848086c35
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
a = float(await input_line("Valeur de a: "))
b = float(await input_line("Valeur de b: "))
if a == b:
  print("a est égal à b.")
elif a < b:
  print("a est plus petit que b.")
else:
  print("a est plus grand que b.")
```
````

## Exercice {num}`exo-py1`

```{exec} python
:editor: 49f2047d-751c-42d6-8832-40953fa8db92
# Complétez le programme
a = ...
if ... :
  print("a est plus grand de 5.")
elif ... :
  print("a est égal à 5.")
else:
  print("a est ...")
```

Tester la justesse de votre code avec différentes valeurs de a.

````{solution}
```{exec} python
:editor:
a = ...                                 # choisir la valeur de a
if a > 5 :
  print("a est plus grand de 5.")
elif a == 5 :                           # a == 5 pour la comparaison
  print("a est égal à 5.")
else:
  print("a est plus petit que 5.")
```
````

## Exercice {num}`exo-py1`

```{exec} python
:name: python-buffer
:class: hidden
from io import StringIO
import sys

old_stdout = sys.stdout
sys.stdout = StringIO()
```

```{exec} python
:name: python-cond-valeur
:after: python-buffer
:when: never
:linenos:
x = 2
if x <= -1 :
  print(2 * x + 1)
elif x <=3 :
  print(-x + 2)
else :
  print(2 * x - 5)
```

```{exec} python
:linenos:
:after: python-cond-valeur
:when: load
:class: hidden
s = sys.stdout.getvalue().rstrip()
sys.stdout = old_stdout
while True:
  resp = await input_line("Que va afficher ce programme?")
  if resp == s: break
  if resp.replace(" ", "") == "-x+2":
    print("\x0cIl faut remplacer x par sa valeur.")
  else:
    print("\x0cEssaie encore.")
print("\x0cBravo!")
```

## Exercice {num}`exo-py1`

Écrivez un programme qui demande son âge à l'utilisateur et affiche s'il est
majeur ou s'il est mineur.

```{exec} python
:editor: c590c718-c33d-43da-a078-f7eb37502f9c
age = int(await input_line("Quel est ton âge?"))

# Complétez le programme ici
```

````{solution}
```{exec} python
age = int(await input_line("Quel est ton âge? "))

if age < 18:
  print("Tu es mineur.")
else:
  print("Tu es majeur.")
```
````

## Exercice {num}`exo-py1`

Que vont afficher les programmes suivants?

1.  ```{exec} python
    :when: never
    a = 2
    if a != 2:
      print("Rouge")
    elif a < 2:
      print("Bleu")
    else:
      print("Jaune")
    ```

    ````{solution}
    ```{exec} python
    a = 2
    if a != 2:
      print("Rouge")
    elif a < 2:
      print("Bleu")
    else:
      print("Jaune")
    ```
    ````

  2.  ```{exec} python
      :when: never
      y = 2
      if y <= -1:
        print(3 * y + 5)
      elif y <= 3:
        print(y + 4)
      else:
        print(y * y - 1)
      ```

      ````{solution}
      ```{exec} python
      y = 2
      if y <= -1:
        print(3 * y + 5)
      elif y < 2:
        print(y + 4)
      else:
        print(y * y - 1)
      ```
      ````

## Exercice {num}`exo-py1`

Le programme suivant est censé affiché le tarif appliqué en fonction de l'âge de
l'utilisateur. Mais il contient une erreur par ligne, touvez-les et corrigez-les.

```{exec} python
:editor: 55bcea11-979f-43f8-8d1c-46f102e56b2b
age = await input_line("Quel âge as-tu? ")
if age > 18:
print("Tu payes le tarif enfant.")
elif age < 65
  print( Tu payes le tarif adulte. )
else age >= 65:
  print "Tu payes le tarif retraité."
```

````{solution}
```{exec} python
age = int(await input_line("Quel âge as-tu? "))
if age < 18:
  print("Tu payes le tarif enfant.")
elif age < 65:
  print("Tu payes le tarif adulte.")
else:
  print("Tu payes le tarif retraité.")
```
````

## Exercice {num}`exo-py1`

Écrivez un algorithme qui:
- demande un nombre à l'utilisateur,
- soustrait 5,5 à ce nombre,
- si le résultat est négatif, lui ajoute 10,
- affiche le résultat obtenu.

```{exec} python
:editor: d17fb574-66ce-4774-83fa-279a38ff862d
# Écrivez le programme
```

````{solution}
```{exec} python
nombre = float(await input_line("Choisissez un nombre"))
nombre = nombre - 5.5
if nombre < 0:
  nombre = nombre + 10
print(nombre)
```
````

## Exercice {num}`exo-py1`

Voici trois programmes:

1. Quelles sont les différences?
2. Que vont-ils afficher?
3. Faites un ordinogramme pour chacun.

<table style="width: 100%"><tr style="text-align: center">
  <th>Programme 1</th><th>Programme 2</th><th>Programme 3</th>
</tr><tr style="vertical-align: top"><td>

```{exec} python
:linenos:
x = -4
if x < 0:
  x += 7
if x < 5:
  x *= 4
if x < 10:
  x -= 6
else:
  x = 1000
print(x)
```

</td><td style="padding-left: 1rem">

```{exec} python
:linenos:
x = -4
if x < 0:
  x += 7
elif x < 5:
  x *= 4
elif x < 10:
  x -= 6
else:
  x = 1000
print(x)
```

</td><td style="padding-left: 1rem">

```{exec} python
:linenos:
x = -4
if x < 0:
  x += 7
  if x < 5:
    x *= 4
    if x < 10:
      x -= 6
else:
  x = 1000
print(x)
```

</td></tr></table>

## Exercice {num}`exo-py2-rev`

Le programme suivant contient une erreur de logique. Testez le programme avec
différentes valeurs pour trouver et corriger l'erreur.

```{exec} python
:editor: 8f95d8ea-d2c0-4d56-a399-a58c54e99e6c
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
