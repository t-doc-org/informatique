% Copyright 2026 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
solutions: show
```

# Boucle for

La boucle `for` permet de répéter un bloc d'instructions un nombre de fois connu
à l'avance.

```{exec} python
:when: never
for _ in range(nb_repetitions):
  instruction 1
  instruction 2
  ...
```

````{list-grid}
:style: grid-template-columns: 1fr 1fr;
- # Programme
  ```{exec} python
  :editor:
  for i in range(5):
    print(i)
  ```
- # Ordinogramme
  ```{figure} images/for.png
  :alt: Ordinogramme boucle for
  ```
````

1. Quelles valeurs prend la variable i?
2. Changez le nombre de répétitions.
3. Modifiez le code pour afficher les nombres de 1 à 10?

En réalité, la boucle `for` fait plus que juste répéter x fois: pour
chaque itération (passage de la boucle), la variable (ici nommée i) va prendre
la valeur d'un élément de l'ensemble range(n), c'est-à-dire l'ensemble des
nombres entiers de 0 à n non compris $\{0; 1; 2; ...; n-1\}$. Il est donc
possible d'utiliser la valeur de cette variable dans la boucle.


## Exercice {num2}`exercice`

```{exec} python
:linenos:
:when: never
somme = 0
for nombre in range(6):
  somme += nombre
print("La somme est:", somme)
```

Quel est le résultat affiché par ce programme?

````{solution}
Vérifie ta réponse en exécutant le code.
```{exec} python
:linenos:
somme = 0
for nombre in range(6):
  somme += nombre
print("La somme est:", somme)
```
````

## Exercice {num2}`exercice`

1. Écrivez un programme en utilisant la boucle `for` qui affiche les nombres de
    0 à 9.

```{exec} python
:editor: 67d073c3-f5ac-4eca-ab69-2aabc1a336ac
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
for nombre in range(10):
  print(nombre)
```
````

2. Écrivez un programme en utilisant la boucle `for` qui affiche les nombres de
    1 à 10.

```{exec} python
:editor: e68f0b0a-e62d-44f7-bbcf-87a264946a6d
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
for nombre in range(10):
  print(nombre + 1)
```

```{exec} python
:linenos:
for nombre in range(1, 11):
  print(nombre)
```
````

3. Écrivez un programme en utilisant la boucle `for` qui affiche les 12 premiers
    multiples de 5.

```{exec} python
:editor: dda1a5c9-c76c-428a-b544-641f3916aaff
# Écrire le programme ici
```

````{solution}
```{exec} python
:linenos:
for nombre in range(12):
  print((nombre + 1) * 5)
```

```{exec} python
:linenos:
for nombre in range(1, 13):
  print(nombre * 5)
```
````

## Exercice {num2}`exercice`

Indiquez l'ordre d'exécution des lignes et ce qu'affichera le programme.

```{exec} python
:linenos:
:when: never
a = 4
b = 1
for i in range (3):
  a += 5
  b *= 2
  print("i =", i)
print("a =", a, "b =", b)
```

````{solution}
L'ordre d'exécution des ligne est le suivant:

1-2-3-4-5-6-3-4-5-6-3-4-5-6-7

```{exec} python
:linenos:
a = 4
b = 1
for i in range (3):
  a += 5
  b *= 2
  print("i =", i)
print("a =", a, "b =", b)
```
````

