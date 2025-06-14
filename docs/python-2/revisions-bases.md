% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Révisions - Bases

## Variable

Une **variable** permet de garder en mémoire des données (une valeur numérique,
une chaîne de caractères, etc.) pendant l'exécution du programme. Cela permet
de réutiliser facilement ces valeurs.

Quelques règles à respecter:

- Le nom de la variable doit correspondre à son contenu.\
  Exemple: age, hauteur
- Le caractère \_ permet de séparer les mots dans un nom de variable.\
  Exemple: cote_carre
- Le nom d'une variable ne doit pas contenir de caractère accentué.
- Le nom d'une variable doit commencer par une lettre ou le caractère de
  soulignement.
- Le nom d'une variable ne peut contenir que les caractères alphanumériques
  (A-z 0-9 et \_)
- Les majuscules et les minuscules font une différence.
  Exemple: mon\_age, mon\_Age, mon\_AGE sont trois variables différentes

L'**affectation** d'une variable se fait avec un nom de variable, suivi
du signe `=` et de la valeur:\
`age = 17`.

## Opérateurs mathématiques

Les opérateurs mathématiques permettent de faire des calculs simples avec les
nombres.

| Opérateur | Nom                                   | Exemple | Résultat |
| :-------: | :-----------------------------------: | :-----: | :------: |
| +         | Addition                              | 3 + 4   | 7        |
| -         | Soustraction                          | 9 - 12  | -3       |
| *         | Multiplication                        | 5 * 6   | 30       |
| /         | Division                              | 11 / 2  | 5.5      |
| **        | Puissance                             | 2 ** 3  | 8        |
| //        | Division entière                      | 26 // 6 | 4        |
| %         | Modulo (reste de la division entière) | 26 mod 6| 2        |

## Opérateurs de comparaison

Les opérateurs de comparaison permettent de comparer deux valeurs entre elles.
Le résultat de la comparaison est de type booléen: True ou False.

| Opérateur | Nom                  |
| :-------: | :------------------: |
| ==        | égal à               |
| !=        | différent de         |
| >         | plus grand que       |
| <         | plus petit que       |
| >=        | plus grand ou égal à |
| <=        | plus petit ou égal à |

## Opérateurs d'affectation

Les opérateurs d'affectation combinée permettent de modifier la valeur des
variables avec une notation simplifiée. Il existe pour tous les opérateurs
mathématiques, voici les principaux.

| Opérateur | Exemple | Équivalent à |
| :-------: | :-----: | :----------: |
| =         | x = 6   | x = 6        |
| +=        | x += 6  | x = x + 6    |
| -=        | x -= 6  | x = x - 6    |
| \*=       | x \*= 6 | x = x * 6    |
| /=        | x /= 6  | x = x / 6    |

## Types de données

Voici les principaux types de données que nous utiliserons.

| Type  | Nom       | Description                      | Exemple            |
|-------|--------   |----------------------------------|--------------------|
| int   | integer   | Nombres entiers                  | 4                  |
| float | flottant  | Nombres à virgules               | 4.125              |
| str   | string    | Chaînes de caractères            | "Bonjour"          |
| bool  | booléen   | Résultat d'un test: Vrai ou Faux | 2<1 renvoie False  |

Pour connaître le type d'une variable, nous pouvons utiliser la fonction `type()`.

## Commentaires

Le symbole **#** en Python permet d'ajouter des commentaires. Une ligne
commençant par # sera ignorée lors de l'exécution du programme.

## Exemples

1.  ```{exec} python
    :linenos:
    a = 8
    print(a)
    ```

2.  ```{exec} python
    :linenos:
    age = 17
    age = age + 10
    print("Dans 10 ans, tu auras", age, "ans.")
    ```

    Nous remplaçons la valeur qui est stockée dans la variable `age` par une
    nouvelle valeur. L'ancienne valeur est "perdue".

3.  ```{exec} python
    :linenos:
    a = 4
    b = 5
    c = a * b
    print(c)
    ```

4.  ```{exec} python
    :linenos:
    a = 4
    b = 5
    c = a * b
    a = 3
    print(c)
    ```

    Dans une variable, seul le résultat du calcul est stocké, par conséquent,
    même si la valeur de la variable `a` ou celle de `b` change, celle de `c` ne
    changera pas, tant que nous nous lui affectons pas une nouvelle valeur.

5.  ```{exec} python
    :linenos:
    a = 8 / 4 + 1
    print(a, type(a))
    ```

    Dès que la division est utilisée dans un calcul, le résultat sera de type
    `float`, même si le résultat de la division est un nombre entier.

## Exercice {num}`exo-py2-rev`

Quel est le résultat des expressions suivantes en Python?

```{role} input(quiz-input)
:right: width: 5rem;
:check: json trim
```

```{quiz}
:style: max-width: 30rem;
1.  {input}`{"4": true}`
    {quiz-hint}`Il faut effectuer la division entière de 23 par 5.`
    `23 // 5`
2.  {input}`{"3": true}`
    {quiz-hint}`% est le reste de la division entière.`
    `23 % 5`
3.  {input}`{"4.6": true,
             "4,6": "En Python, il faut utiliser un point pour les nombres à
                     virgule."}`
    {quiz-hint}`Il faut effectuer la division.`
    `23 / 5`
4.  {input}`{"0": true,
             "40": "En Python, l'ordre de priorité est le même qu'en maths."}`
    `10 - 2 * 5`
5.  {input}`{"48": true}`
    `(1 + 3 * 2) ** 2 - 1`
```

## Exercice {num}`exo-py2-rev`

De quel type sont les expressions suivantes?

```{role} select(quiz-select)
:right:
:options: |
: int
: float
: str
: bool
```

```{quiz}
:style: max-width: 20rem;
1.  {select}`str`   `"Salut"`
2.  {select}`float` `5.0`
3.  {select}`bool`  `5 > 7`
4.  {select}`int`   `120`
5.  {select}`int`   `9 // 2`
6.  {select}`float` `(3 + 7) / 2`
```

## Exercice {num}`exo-py2-rev`

Qu'affiche le programme suivant? Appuyez sur le bouton "play" pour vérifier
votre réponse.

```{exec} python
:linenos:
base = 10
hauteur = 5
aire = base * hauteur / 2
print("L'aire du triangle est de", aire)
```

## Exercice {num}`exo-py2-rev`

Qu'affiche le programme suivant? Faire un tableau d'états.\
Appuyez sur le bouton "play" pour vérifier votre réponse.

```{exec} python
:linenos:
a = 18
b = 2
a -= 8
b = a - 6
a += b
a = a * 2
print(a, b)
```

````{solution}
| Instruction | a | b |
| :---------- |:-:|:-:|
| a = 18      |18 |-  |
| b = 2       |18 |2  |
| a -= 8      |10 |2  |
| b = a - 6   |10 |4  |
| a += b      |14 |4  |
| a = a * 2   |28 |4  |
````

## Exercice {num}`exo-py2-rev`

En exécutant les programmes suivants, une erreur se produit. Corrigez le code à
l'aide du message d'erreur.

1.  ```{exec} python
    :editor:
    print("Bonjour)
    ```

2.  ```{exec} python
    :editor:
    print(hello)
    ```

3.  ```{exec} python
    :editor:
    age == 18
    print(age)
    ```

4.  ```{exec} python
    :editor:
    longueur = 7
    largeur = 12
    perimetre = 2 * (LONGUEUR + largeur)
    print(perimetre)
    ```

5.  ```{exec} python
    :editor:
    a = 10
    # afficher la valeur de a
    print("a")
    ```

6.  ```{exec} python
    :editor:
    a = 10
    b = 5
    print("La somme de a et b vaut" a + b)
    ```

## Exercice {num}`exo-py2-rev`

Faites le tableau d'états du programme suivant:

```{exec} python
:linenos:
a = 8
b = a / 2
a += 5
c =  a - b
d = b ** 2
c = a // 3
b *= 5
d = a % 3
e = a < b
print(a, b, c, d, e)
```

````{solution}
| Instruction | a   | b   | c   | d   | e   |
| :---------- |:---:|:---:|:---:|:---:|:---:|
| a = 8       | 8   | -   | -   | -   | -   |
| b = a / 2   | 8   | 4.0 | -   | -   | -   |
| a += 5      | 13  | 4.0 | -   | -   | -   |
| c = a - b   | 13  | 4.0 | 9.0 | -   | -   |
| d = b ** 2  | 13  | 4.0 | 9.0 | 16.0| -   |
| c = a // 3  | 13  | 4.0 | 4   | 16.0| -   |
| b *= 5      | 13  | 20.0| 4   | 16.0|-    |
| d = a % 3   | 13  | 20.0| 4   | 1   |-    |
| e = a < b   | 13  | 20.0| 4   | 1   | True|
````
