% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Révisions - Boucle while

## Boucle while

La boucle while (qui signifie "tant que" en anglais) permet de répéter un bloc
d'instructions tant qu'une condition est vraie.

```{exec} python
:when: never
while condition:
  instruction 1
  instruction 2
  ...
```

````{list-grid}
:style: grid-template-columns: 1fr 1fr;
- # Programme
  ```{exec} python
  :editor:
  nb_points = 0
  max = 10
  while nb_points < max:
    print("Points:", nb_points)
    nb_points += 3
  print("Bravo!")
  ```
- # Ordinogramme
  ```{figure} images/while.png
  :alt: Ordinogramme boucle for
  :align: center
  ```
````

## Exercice {num2}`exercice`

Cochez la bonne réponse.

```{defaults} quiz-check
:randomize:
:class: columns-4
```

{.lower-alpha-paren}
1.  `````{quiz}
    Qu'affiche le progamme suivant?

    ```{exec} python
    :name: prog3.1
    :when: never
    :linenos:
    x = 0
    while x < 4:
      print(x)
      x += 1
    ```

    ````{quiz-check}
    - :
      ```{exec} python
      :after: prog3.1
      :when: load
      :class: hidden
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 1
      while x < 4:
        print(x)
        x += 1
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 0
      while x <= 4:
        print(x)
        x += 1
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 1
      while x <= 4:
        print(x)
        x += 1
      ```
    ````
    `````
2.  `````{quiz}
    Qu'affiche le progamme suivant?

    ```{exec} python
    :name: prog3.2
    :when: never
    :linenos:
    x = 0
    while x < 4:
      x += 1
      print(x)
    ```

    ````{quiz-check}
    - :
      ```{exec} python
      :after: prog3.2
      :when: load
      :class: hidden
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 1
      while x < 4:
        x += 1
        print(x)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 0
      while x <= 4:
        x += 1
        print(x)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 1
      while x <= 4:
        x += 1
        print(x)
      ```
    ````
    `````
3.  `````{quiz}
    Qu'affiche le progamme suivant?

    ```{exec} python
    :name: prog3.3
    :when: never
    :linenos:
    x = 0
    while x <= 6:
      print(x)
      x += 2
    ```

    ````{quiz-check}
    - :
      ```{exec} python
      :after: prog3.3
      :when: load
      :class: hidden
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 1
      while x < 6:
        print(x)
        x += 2
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 0
      while x < 6:
        print(x)
        x += 1
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 1
      while x <= 6:
        print(x)
        x += 2
      ```
    ````
    `````
4.  `````{quiz}
    Qu'affiche le progamme suivant?

    ```{exec} python
    :name: prog3.4
    :when: never
    :linenos:
    x = 1
    while x < 6:
      x += 3
      print(x)
    ```

    ````{quiz-check}
    - :
      ```{exec} python
      :after: prog3.4
      :when: load
      :class: hidden
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 0
      while x < 6:
        x += 3
        print(x)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 0
      while x <= 6:
        x += 3
        print(x)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 1
      while x <= 6:
        x += 3
        print(x)
      ```
    ````
    `````
5.  `````{quiz}
    Qu'affiche le progamme suivant?

    ```{exec} python
    :name: prog3.5
    :when: never
    :linenos:
    x = 10
    while x >= 4:
      x -= 2
      print(x)
    ```

    ````{quiz-check}
    - :
      ```{exec} python
      :after: prog3.5
      :when: load
      :class: hidden
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 10
      while x > 4:
        x -= 1
        print(x)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 10
      while x > 4:
        x -= 2
        print(x)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 11
      while x >= 4:
        x -= 2
        print(x)
      ```
    ````
    `````

## Exercice {num2}`exercice`

1. Écrivez un programme en utilisant la boucle `while` qui affiche les nombres de
    0 à 9.

```{exec} python
:editor: 4256d682-b6eb-4cd6-b02d-2cdfe6c48a78
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
x = 0
while x < 10:
  print(x)
  x += 1
```
````

2. Écrivez un programme en utilisant la boucle `while` qui affiche les nombres de
    1 à 10.

```{exec} python
:editor: 47920c08-e53b-4efa-a8db-485299344105
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
x = 1
while x <= 10:
  print(x)
  x += 1
```
````

5. Écrivez un programme en utilisant la boucle `while` qui affiche les nombres
    de 1 à 20 en comptant de 4 en 4.

```{exec} python
:editor: 5f9fccff-539a-4224-940a-79a66f0dded4
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
x = 1
while x <= 20:
  print(x)
  x += 4
```
````

4. Écrivez un programme en utilisant la boucle `while` qui affiche les 12 premiers
    multiples de 5.

```{exec} python
:editor: 323de3c0-6733-4c79-a58b-ab55d76a0052
# Écrire le programme ici
```

````{solution}
```{exec} python
:linenos:
x = 1
while x <= 12:
  print(x * 5)
  x += 1
```
````

````{tip}
Il est possible de répétez les caractères en utilisant `*`.

```{exec} python
:editor:
print("@" * 6)  # répète 6 fois le caractère @
```
````


## Exercice {num2}`exercice`

Cochez la bonne réponse.

```{defaults} quiz-check
:randomize:
:class: columns-4
```

{.lower-alpha-paren}
1.  `````{quiz}
    Qu'affiche le progamme suivant?

    ```{exec} python
    :name: prog4.1
    :when: never
    :linenos:
    x = 1
    while x < 6:
      print("^" * x)
      x += 1
    ```

    ````{quiz-check}
    - :
      ```{exec} python
      :after: prog4.1
      :when: load
      :class: hidden
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 1
      while x < 5:
        print("^" * x)
        x += 1
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 1
      while x < 6:
        print("x" * x)
        x += 1
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 1
      while x < 5:
        print("x" * x)
        x += 1
      ```
    ````
    `````
2.  `````{quiz}
    Qu'affiche le progamme suivant?

    ```{exec} python
    :name: prog4.4
    :when: never
    :linenos:
    x = 1
    n = 5
    while x <= 4:
      print(" _ " * n)
      print("|_|" * n)
      x += 1
    ```

    ````{quiz-check}
    - :
      ```{exec} python
      :after: prog4.4
      :when: load
      :class: hidden
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 1
      n = 4
      while x <= 5:
        print(" _ " * n)
        print("|_|" * n)
        x += 1
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 1
      n = 5
      while x <= 4:
        print("|_|" * n)
        print(" _ " * n)
        x += 1
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 1
      n = 4
      while x <= 5:
        print("|_|" * n)
        print(" _ " * n)
        x += 1
      ```
    ````
    `````

3.  `````{quiz}
    Qu'affiche le progamme suivant?

    ```{exec} python
    :name: prog4.2
    :when: never
    :linenos:
    x = 1
    while x <= 4:
      print(" " * (4-x) + "^" * x)
      x += 1
    ```

    ````{quiz-check}
    - :
      ```{exec} python
      :after: prog4.2
      :when: load
      :class: hidden
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 1
      while x <= 8:
        print(" " * x + "^" * x)
        x += 2
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 1
      n = 4
      while x <= 9:
        print(" " * n + "^" * x)
        x += 2
        n -= 1
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 1
      while x <= 4:
        print("^" * x)
        x += 1
      ```
    ````
    `````
4.  `````{quiz}
    Qu'affiche le progamme suivant?

    ```{exec} python
    :name: prog4.3
    :when: never
    :linenos:
    x = 1
    n = 4
    while x <= 9:
      print(" " * n + "^" * x)
      x += 2
      n -= 1
      print(" " * 3 + "|" * 2)
    ```

    ````{quiz-check}
    - :
      ```{exec} python
      :after: prog4.3
      :when: load
      :class: hidden
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 1
      n = 4
      while x <= 9:
        print(" " * n + "^" * x)
        x += 2
        n -= 1
      print(" " * 3 + "| |")
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 1
      n = 4
      while x <= 9:
        print(" " * n + "^" * x)
        x += 2
        n -= 1
      print("|" * 2)
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 1
      while x <= 4:
        print("^" * x)
        x += 1
        print("|" * 2)
      ```
    ````
    `````
    ```{defaults} quiz-check
    :randomize:
    :class: columns-2
    ```
5.  `````{quiz}
    Qu'affiche le progamme suivant?

    ```{exec} python
    :name: prog4.5
    :when: never
    :linenos:
    x = 4
    print("~" * 24)
    while x > 1:
      x -= 1
      print("<°)))>< " * x)
    print("~" * 24)
    ```

    ````{quiz-check}
    - :
      ```{exec} python
      :after: prog4.5
      :when: load
      :class: hidden
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 4
      while x > 1:
        print("<°)))>< " * x)
        print("~" * 24)
        x -= 1
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 4
      while x > 1:
        print("~" * 24)
        print("<°)))>< " * x)
        x -= 1
      ```
    - ```{exec} python
      :when: load
      :class: hidden
      x = 4
      while x > 1:
        x -= 1
        print("~" * 24)
        print("<°)))>< " * x)
      ```
    ````
    `````




## Exercice {num2}`exercice-rev`

Nous voulons créer un programme qui demande à l'utilisateur un nombre
strictement positif. Tant que l'utilisateur entre un nombre plus petit ou égal à
0, alors le programme devra lui redemander d'entrer un nouveau nombre.

Écrivez un programme qui correspond à l'algorithme suivant:

```{code-block} text
Demander un nombre strictement positif à l'utilisateur et le stocker dans la variable n
Tant que n est plus petit ou égal à 0
    Afficher "Le nombre doit être strictement positif!"
    Demander un nombre positif à l'utilisateur et le stocker dans n
Afficher "Merci"
```

```{exec} python
:editor: d8324808-567b-4ff5-84a3-7968443ba125
# Complétez le programme
n = int(input("Entrer un nombre strictement positif: "))
print("Le nombre doit être strictement positif!")
print("Merci")
```

````{solution}
```{exec} python
:linenos:
n = int(input("Entrer un nombre strictement positif: "))
while n <= 0:
  print("Le nombre doit être strictement positif!")
  n = int(input("Entrer un nombre strictement positif: "))
print("Merci")
```
````

## Exercice {num2}`exercice-rev`

Nous souhaitons créer un programme qui compte le temps avant qu'une bombe
explose. Pour cela, un compte à rebours commencera à 10 et ira jusqu'à 1, puis
le programme affichera "BOOM".

Écrivez un programme qui correspond à l'algorithme suivant:

```{code-block} text
Initialiser une variable compte_a_rebours à 10
Tant que compte_a_rebours est plus grand que 0
    Afficher La valeur de compte_a_rebours
    Retirer 1 à compte_a_rebours
Afficher "BOOM"
```

Ce programme doit alors afficher:

```{code-block} text
10
9
8
7
6
5
4
3
2
1
BOOM
```

```{exec} python
:editor: 8dea2b74-1c80-4068-9508-2d2dadc0730b
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
compte_a_rebours = 10
while compte_a_rebours > 0:
  print(compte_a_rebours)
  compte_a_rebours -= 1
print("BOOM")
```
````

## Exercice {num2}`exercice-rev`

Écrivez un programme qui demande à l'utilisateur combien il y a de cantons en
Suisse. Tant que la réponse n'est pas 26, le programme redemande une nouvelle
réponse.

Exemple d'exécution:

```{code-block} text
Combien y a-t-il de cantons en Suisse?
16
Faux, essaie encore!
27
Faux, essaie encore!
26
Bravo!
```

```{exec} python
:editor: bb46d9c0-3297-42d5-9ea6-f631893bb839
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
nb_cantons = int(input("Combien y a-t-il de cantons en Suisse?"))
while nb_cantons != 26:
  nb_cantons = int(input("Faux, essaie encore!"))
print("Bravo!")
```
````

## Bonus {num2}`bonus-rev`

Améliorez le programme de l'exercice précédent en indiquant à l'utilisateur
s'il y a plus ou moins de cantons en fonction de sa réponse.

## Exercice {num2}`exercice-rev`

Indiquez l'ordre d'exécution des lignes et faites le tableau d'états du programme
suivant:

```{exec} python
:linenos:
a = 0
b = 1
while a < 5:
  a += 1
  if a % 2 == 0:
    b *= 2
a = 1
print(a, b)
```

```{solution}
L'ordre d'exécution des ligne est le suivant:

1-2-3-4-5-3-4-5-6-3-4-5-3-4-5-6-3-4-5-3-7-8

| Instruction | a   | b   |
| :---------- |:---:|:---:|
| a = 0       | 0   | -   |
| b = 1       | 0   | 1   |
| a += 1      | 1   | 1   |
| a += 1      | 2   | 1   |
| b *= 2      | 2   | 2   |
| a += 1      | 3   | 2   |
| a += 1      | 4   | 2   |
| b *= 2      | 4   | 4   |
| a += 1      | 5   | 4   |
| a = 1       | 1   | 4   |
```
