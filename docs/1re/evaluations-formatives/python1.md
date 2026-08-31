% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Python 1

```{include} /_include/entete-examen.export.md
```
```{class} align-center
**Attention au soin. Calculatrice autorisée.**
```
---

## Question {nump}`question`{points}`3`

En fonction du programme ci-dessous, complétez le type de variables:

```{exec} python
:when:
nom = input("Quel est ton nom")
nombre = 45 / 3
marie = False
```

`marie` est une variable de type: {leader}`.`

`nom` est une variable de type: {leader}`.`

`nombre` est une variable de type: {leader}`.`

```{solution}
`marie` est une variable de type: bool ou booléen\
`nom` est une variable de type: str ou string\
`nombre` est une variable de type: float ou flottant
```

## Question {nump}`question`{points}`3`

Complétez le tableau d'états pour le progamme suivant.

````{list-grid}
:style: grid-template-columns: 1fr 1fr;

-   ```{exec} python
    :when:
    :linenos:
    a = 7
    b = a / 2
    b += 3
    c = a < b
    d = 13 // 6
    a = 9 % 5
    d = a ** 2
    c = a < 4 or b > 3
    ```
-   ```{flex-table}
    :class: function-table align-center
    |ligne|$\quad a\quad$|$\quad b\quad$|$\quad c\quad$|$\quad d\quad$
    |1||||
    |2||||
    |3||||
    |4||||
    |5||||
    |6||||
    |7||||
    |8||||
    ```
````

````{solution}
```{flex-table}
:class: function-table align-center
|ligne|$\quad a\quad$|$\quad b\quad$|$\quad c\quad$|$\quad d\quad$
|1|7|?|?|?
|2|7|3.5|?|?
|3|7|6.5|?|?
|4|7|6.5|False|?
|5|7|6.5|False|2
|6|4|6.5|False|2
|7|4|6.5|False|16
|8|4|6.5|True|16
```
````

## Question {nump}`question`{points}`1`

```{exec} python
:when:
:linenos:
prenom = "Bob"
age = 15
print("prenom", prenom, age, "age")
```

Qu'affiche le programme ci-dessus?
{vspace}`5lh`

````{solution}
```{code-block} text
prenom Bob 15 age
```
````

## Question {nump}`question`{points}`2`

```{exec} python
:when:
:linenos:
x = 5
for _ in range(3):
    print(x)
    x *= 4
print(x)
```

{.lower-alpha-paren}
1.  Qu'affiche le programme ci-dessus?
    {vspace}`5lh`
2.  Indiquez l'ordre dans lequel les instructions seront exécutées (numéros de
    lignes).
    {vspace}`3lh`

````{solution}
{.lower-alpha-paren}
1.  Le programme va afficher:
    ```{code-block} text
    5
    20
    80
    320
    ```
2. Ordre d'exécution de lignes: 1-2-3-4-2-3-4-2-3-4-5
````

## Question {nump}`question`{points}`2`

```{exec} python
:when:
:linenos:
x = 0
if x <= -1:
  y = 2 * x + 1
elif x <= 3:
  y = -x + 2
else:
  y = 2 * x - 5
print(y, x)
```

{.lower-alpha-paren}
1.  Qu'affiche le programme ci-dessus?
    {vspace}`5lh`
2.  Indiquez l'ordre dans lequel les instructions seront exécutées (numéros de
    lignes).
    {vspace}`3lh`


````{solution}
{.lower-alpha-paren}
1.  Le programme va afficher:
    ```{code-block} text
    2 0
    ```
2. Ordre d'exécution de lignes: 1-2-4-5-8
````

## Question {nump}`question`{points}`16`

Partie **écriture de programmes** faite sur Exam.net:

Ex 1 (5 pts), Ex 2 (5 pts), Ex 3 (6 pts), Bonus (2 pts)
