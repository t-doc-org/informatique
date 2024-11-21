% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Nombres entiers signés

## Introduction

Pour encoder des nombres entiers relatifs (appelés entiers signés), l'idée
principale est d'utiliser le bit de poids fort (le chiffre qui se trouve le plus
à gauche) pour représenter le signe: 0 si le nombre est positif et 1 si le
nombre est négatif.

Cette représentation possède deux inconvénients:

- le nombre 0 a deux présentations différents: 00000000 et 10000000
- les opérations arithmétiques sont plus compliquées. Il faut notamment
différencier le cas où les deux nombres sont de même signe du cas où ils sont de
signes différents.


## Complément à 2

La notation en complément à 2 permet de remédier à ces problèmes. Les nombres
entiers relatifs positifs sont représentés comme des entiers positifs avec le
bit de poids fort qui est à zéro (bit de signe) et les entiers relatifs négatifs
sont obtenus selon le tableau ci-dessous:

| Écriture | Entiers non signés (valeur décimale) | Entiers signés (valeur décimale) |
|:--------:|:-----------------------------------:|:--------------------------------:|
| 4 bits   | tous les bits sont utilisés pour définir le nombre | le bit de poids fort est utilisé pour le signe |
| 0000     | 0                                   | 0                                |
| 0001     | 1                                   | 1                                |
| 0010     | 2                                   | 2                                |
| 0011     | 3                                   | 3                                |
| 0100     | 4                                   | 4                                |
| 0101     | 5                                   | 5                                |
| 0110     | 6                                   | 6                                |
| 0111     | 7                                   | 7                                |
| 1000     | 8                                   | -8                               |
| 1001     | 9                                   | -7                               |
| 1010     | 10                                  | -6                               |
| 1011     | 11                                  | -5                               |
| 1100     | 12                                  | -4                               |
| 1101     | 13                                  | -3                               |
| 1110     | 14                                  | -2                               |
| 1111     | 15                                  | -1                               |

### Remarques

| Entiers non signés sur 4 bits | Entiers signés sur 4 bits |
|:------------------:|:--------------:|
| La valeur minimale est 0 | La valeur minimale est $-2^{4-1} = -8$ |
| La valeur maximale est $2^4-1 = 15$ | La valeur maximale est $2^{4-1}-1 = 7$ |

## Opposé d'un nombre

Pour déterminer l'opposé d'un nombre, il faut:
1. Inverser tous les bits (0 $\rightarrow$ 1 et 1 $\rightarrow$ 0);
2. Additionner 1.

L'opposé de $0101_2$ est $1011_2$. En effet,
```{code-block} text
  1 0 1 0     (inverser chaque bit)
+       1     (ajouter 1)
----------
  1 0 1 1
```

Vérification: l'addition d'un nombre et de son opposé doit donner 0.
```{code-block} text
  1 1 1 1      (retenues)
    0 1 0 1
+   1 0 1 1
------------
  1 0 0 0 0    (sans tenir compte de la retenue finale)
```

## Exercice {num}`exo-info`

Déterminer l'opposé des nombres suivants en binaire, ainsi que la valeur
décimale de celui-ci.

1. $0111_2$

    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Opposé:")
      if resp.replace(" ", "") == "1001": break
      print("\x0cEssaie encore")
    print("\x0cL'opposé est correct.")
    while True:
      resp = await input_line("Valeur décimale:")
      if resp.replace(" ", "") == "-7": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

2. $0101\,1010_2$

    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Opposé:")
      if resp.replace(" ", "") == "10100110": break
      print("\x0cEssaie encore")
    print("\x0cL'opposé est correct.")
    while True:
      resp = await input_line("Valeur décimale:")
      if resp.replace(" ", "") == "-90": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

3. $1111_2$

    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Opposé:")
      if resp.replace(" ", "") == "0001": break
      print("\x0cEssaie encore")
    print("\x0cL'opposé est correct.")
    while True:
      resp = await input_line("Valeur décimale:")
      if resp.replace(" ", "") == "1": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

4. $1101\,0001_2$

    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Opposé:")
      if resp.replace(" ", "") == "00101111": break
      print("\x0cEssaie encore")
    print("\x0cL'opposé est correct.")
    while True:
      resp = await input_line("Valeur décimale:")
      if resp.replace(" ", "") == "47": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

## Exercice {num}`exo-info`

Répondre aux questions suivantes:

1. Quel est le plus grand nombre entier non signé que nous pouvons écrire sur 4
bits?

    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Réponse en décimal:")
      if resp.replace(" ", "") == "15": break
      print("\x0cEssaie encore")
    print("\x0cQu'est-ce que cela donne en binaire?")
    while True:
      resp = await input_line("Réponse en binaire:")
      if resp.replace(" ", "") == "1111": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

    Et sur 8 bits?


    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Réponse en décimal:")
      if resp.replace(" ", "") == "255": break
      print("\x0cEssaie encore")
    print("\x0cQu'est-ce que cela donne en binaire?")
    while True:
      resp = await input_line("Réponse en binaire:")
      if resp.replace(" ", "") == "11111111": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

    Et sur n bits?


    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Réponse:")
      if resp.replace(" ", "") == "2^n-1": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

2. Quel est le plus petit nombre entier non signé que nous pouvons écrire sur 4
bits?


    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Réponse en décimal:")
      if resp.replace(" ", "") == "0": break
      print("\x0cEssaie encore")
    print("\x0cQu'est-ce que cela donne en binaire?")
    while True:
      resp = await input_line("Réponse en binaire:")
      if resp.replace(" ", "") == "0000": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

    Et sur 8 bits?


    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Réponse:")
      if resp.replace(" ", "") == "0": break
      print("\x0cEssaie encore")
    print("\x0cQu'est-ce que cela donne en binaire?")
    while True:
      resp = await input_line("Réponse en binaire:")
      if resp.replace(" ", "") == "00000000": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

    Et sur n bits?


    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Réponse:")
      if resp.replace(" ", "") == "0": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

3. Quel est le plus grand nombre entier signé que nous pouvons écrire sur 4
bits?

    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Réponse en décimal:")
      if resp.replace(" ", "") == "7": break
      print("\x0cEssaie encore")
    print("\x0cQu'est-ce que cela donne en binaire?")
    while True:
      resp = await input_line("Réponse en binaire:")
      if resp.replace(" ", "") == "0111": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

    Et sur 8 bits?


    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Réponse en décimal:")
      if resp.replace(" ", "") == "127": break
      print("\x0cEssaie encore")
    print("\x0cQu'est-ce que cela donne en binaire?")
    while True:
      resp = await input_line("Réponse en binaire:")
      if resp.replace(" ", "") == "01111111": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

    Et sur n bits?


    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Réponse:")
      if resp.replace(" ", "") == "2^(n-1)-1": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

4. Quel est le plus petit nombre entier signé que nous pouvons écrire sur 4
bits?

    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Réponse en décimal:")
      if resp.replace(" ", "") == "-8": break
      print("\x0cEssaie encore")
    print("\x0cQu'est-ce que cela donne en binaire?")
    while True:
      resp = await input_line("Réponse en binaire:")
      if resp.replace(" ", "") == "1000": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

    Et sur 8 bits?


    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Réponse en décimal:")
      if resp.replace(" ", "") == "-128": break
      print("\x0cEssaie encore")
    print("\x0cQu'est-ce que cela donne en binaire?")
    while True:
      resp = await input_line("Réponse en binaire:")
      if resp.replace(" ", "") == "10000000": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

    Et sur n bits?


    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Réponse:")
      if resp.replace(" ", "") == "-2^(n-1)": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

