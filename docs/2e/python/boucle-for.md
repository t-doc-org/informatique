% Copyright 2026 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Boucle for

La boucle `for` permet de répéter un bloc d'instructions un nombre de fois connu
à l'avance. Mais elle permet de faire des choses beaucoup plus intéressantes,
tel que parcourir une [chaîne de caractères](#string) ou une
[liste](listes-for.md) un élément après l'autre.

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

Cochez la bonne réponse.

```{defaults} quiz-check
:randomize:
:class: grid-4
```

{.lower-alpha-paren}
1.  Qu'affiche le progamme suivant?

    ```{exec} python
    :name: prog6.1
    :when: never
    :linenos:
    for i in range(3):
      print("Hello")
    ```
    `````{quiz}
    ````{quiz-check}
    - :
      ```{exec} python
      :after: prog6.1
      :when: load
      :class: hidden
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      for i in range(3):
        print(i)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      for i in range(2):
        print("Hello")
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      for i in range(4):
        print("Hello")
      ```
    ````
2.  Qu'affiche le progamme suivant?

    ```{exec} python
    :name: prog6.2
    :when: never
    :linenos:
    for i in range(4):
      print(i)
    ```
    `````{quiz}
    ````{quiz-check}
    - :
      ```{exec} python
      :after: prog6.2
      :when: load
      :class: hidden
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      for i in range(4):
        print(i+1)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      for i in range(5):
        print(i)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      for i in range(4):
        print("4")
      ```
    ````
    `````
3.  Qu'affiche le progamme suivant?

    ```{exec} python
    :name: prog6.3
    :when: never
    :linenos:
    for i in range(2):
      print("i")
    ```
    `````{quiz}
    ````{quiz-check}
    - :
      ```{exec} python
      :after: prog6.3
      :when: load
      :class: hidden
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      for i in range(2):
        print(i)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      for i in range(3):
        print(i)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      for i in range(1):
        print(i)
      ```
    ````
    `````
4.  Qu'affiche le progamme suivant?

    ```{exec} python
    :name: prog6.4
    :when: never
    :linenos:
    for i in range(5):
      print(i+1)
    ```
    `````{quiz}
    ````{quiz-check}
    - :
      ```{exec} python
      :after: prog6.4
      :when: load
      :class: hidden
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      for i in range(4):
        print(i+1)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      for i in range(6):
        print(i+1)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      for i in range(5):
        print(i)
      ```
    ````
    `````
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

Que va afficher ce programme?
```{exec} python
:linenos:
:when: never
somme = 0
for nombre in range(6):
  somme += nombre
print("La somme est", somme)
```
```{role} input(quiz-input)
:style: width: 100%;
```

```{quiz}
{input}`La somme est 15`
{quiz-hint}`Calculez la valeur de la somme et affichez le texte complet avec la
majuscule.`
```

````{solution}
```{exec} python
:editor:
somme = 0
for nombre in range(6):
  somme += nombre
print("La somme est", somme)
```
````

## Exercice {num2}`exercice`

Écrivez un programme qui affiche le produit de tous les nombres de 1 à 10.
```{exec} python
:editor: 1141ad86-d9e5-40b0-83bd-a11c7ca9e9a4
```

````{solution}
```{exec} python
:editor:
produit = 1
for nombre in range(1, 11):
  produit *= nombre
print("Le produit de tous les nombres de 1 à 10 est", produit)
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
for i in range(3):
  a += 5
  b *= 2
  print("i =", i)
print("a =", a, "b =", b)
```
````

## Exercice {num2}`exercice`

Il est toujours possible de convertir une boucle `for` en boucle `while`, par
contre il n'est pas toujours possible de convertir une boucle `while` en boucle
`for`, notamment si on ne sait pas à l'avance le nombre d'itérations.

```{defaults} quiz-check
:randomize:
:multi:
:class: grid-2
```

{.lower-alpha-paren}
1.  Quel(s) code(s) correspond(ent) à la boucle `for` ci-dessous?

    ```{exec} python
    :when: never
    :linenos:
    for i in range(5):
      print(i)
    ```
    `````{quiz}
    ````{quiz-check}
    - :
      ```{exec} python
      :when: never
      :linenos:
      x = 0
      while x < 5:
        print(x)
        x += 1
      ```
    - ```{exec} python
      :when: never
      :linenos:
      while x < 5:
        print(x)
      ```
    - ```{exec} python
      :when: never
      x = 0
      while x < 6:
        print(x)
        x += 1
      ```
    - ```{exec} python
      :when: never
      :linenos:
      x = 0
      while x < 5:
        x += 1
        print(x)
      ```
    ````
    ``````
2.  Quel(s) code(s) correspond(ent) à la boucle `for` ci-dessous?

    ```{exec} python
    :when: never
    :linenos:
    for i in range(4):
      print(i + 1)
    ```
    `````{quiz}
    ````{quiz-check}
    - :
      ```{exec} python
      :when: never
      :linenos:
      x = 1
      while x < 5:
        print(x)
        x += 1
      ```
    - :
      ```{exec} python
      :when: never
      :linenos:
      x = 0
      while x < 4:
        x += 1
        print(x)
      ```
    - ```{exec} python
      :when: never
      x = 0
      while x < 5:
        print(x+1)
        x += 1
      ```
    - ```{exec} python
      :when: never
      :linenos:
      x = 1
      while x < 5:
        print(x+1)
        x += 1
      ```
    ````
    `````
3.  Quel(s) code(s) correspond(ent) à la boucle `while` ci-dessous?

    ```{exec} python
    :when: never
    :linenos:
    x = 4
    while x < 7:
      print(x)
      x += 1
    ```
    `````{quiz}
    ````{quiz-check}
    - :
      ```{exec} python
      :when: never
      :linenos:
      for i in range(4, 7):
        print(i)
      ```
    - :
      ```{exec} python
      :when: never
      :linenos:
      for i in range(3):
        print(i + 4)
      ```
    - ```{exec} python
      :when: never
      for i in range(3, 7):
        print(i)
      ```
    - ```{exec} python
      :when: never
      :linenos:
      for i in range(4, 8):
        print(i)
      ```
    ````
    `````
4.  Quel(s) code(s) correspond(ent) à la boucle `while` ci-dessous?

    ```{exec} python
    :when: never
    :linenos:
    x = 2
    while x <= 5:
      print(x)
      x += 1
    ```
    `````{quiz}
    ````{quiz-check}
    - :
      ```{exec} python
      :when: never
      :linenos:
      for i in range(2, 6):
        print(i)
      ```
    - :
      ```{exec} python
      :when: never
      :linenos:
      for i in range(1, 5):
        print(i + 1)
      ```
    - ```{exec} python
      :when: never
      :linenos:
      for i in range(5):
        print(i)
      ```
    - ```{exec} python
      :when: never
      :linenos:
      for i in range(2, 5):
        print(i)
      ```
    ````
    `````
5.  Cochez les boucles `while` qui ne peuvent pas être transformées en boucle
    `for`.

    `````{quiz}
    ````{quiz-check}
    :class: grid-1
    - :
      ```{exec} python
      :when: never
      :linenos:
      n = int(input("Entrer un nombre strictement positif: "))
      while n <= 0:
        print("Le nombre doit être strictement positif!")
        n = int(input("Entrer un nombre strictement positif: "))
      print("Merci")
      ```
    - :
      ```{exec} python
      :when: never
      :linenos:
      mot_de_passe = ""
      while mot_de_passe != "secret123":
          mot_de_passe = input("Entrez le mot de passe: ")
      print("Accès autorisé!")
      ```
    - ```{exec} python
      :when: never
      :linenos:
      compte_a_rebours = 5
      while compte_a_rebours > 0:
        print(compte_a_rebours)
        compte_a_rebours -= 1
      print("Bonne année!")
      ```
    - :
      ```{exec} python
      :when: never
      :linenos:
      nb_cantons = int(input("Combien y a-t-il de cantons en Suisse?"))
      while nb_cantons != 26:
        if nb_cantons < 26:
          nb_cantons = int(input("Faux, il y en a plus! Essaie encore."))
        else:
          nb_cantons = int(input("Faux, il y en a moins! Essaie encore."))
      print("Bravo!")
      ```
    - ```{exec} python
      :when: never
      :linenos:
      x = 1
      n = 4
      while x <= 5:
        print(" _ " * n)
        print("|_|" * n)
        x += 1
      ```
    ````
    `````
