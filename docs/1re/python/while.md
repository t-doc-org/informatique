% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Boucle while

## Répétition d'un bloc d'instructions

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
  ```
````

La boucle `while` peut être utilisée comme une boucle `for`. Pour cela, il faut
définir un compteur qui va "compter" le nombre de répétitions.

````{list-grid}
:style: grid-template-columns: 1fr 1fr;
- # Boucle for
  ```{exec} python
  :editor:
  for _ in range(10):
    print("Hello")
  ```
- # Boucle while
  ```{exec} python
  :editor:
  compteur = 0
  while compteur < 10:
    print("Hello")
    compteur += 1
  ```
````

```{important}
Il ne faut pas oublier d'incrémenter (augmenter) le compteur à chaque passage
dans la boucle, sinon la condition sera toujours vraie et la boucle ne
s'arrêtera jamais (boucle infinie). Cela fait "planter" le programme.
```

### Exercice {num2}`exercice`

Sans l'exécuter, qu'affiche ce programme?

Ensuite, exécutez le programme pour vérifier votre réponse.

```{exec} python
:editor:
i = 1
while i <= 10:
  print("7 *", i, "=", 7 * i)
  i = i + 1
```

```{solution}
Ce programme calcule et affiche le livret de 7 de 1 à 10.
```

### Exercice {num2}`exercice`

Sans l'exécuter, qu'affiche ce programme?

Ensuite, exécutez le programme pour vérifier votre réponse.

```{exec} python
:editor:
n = 2
while n <= 50:
  print(n)
  n = n + 2
```

```{solution}
Ce programme affiche les nombres paires de 2 à 50 compris.
```

### Exercice {num2}`exercice`

Sans exécuter le programme, faites un tableau d'états des variables de ce
programme.

Qu'affichera-t-il?

```{exec} python
:editor:
s = 0
i = 1
while i <= 5:
  s = s + i
  i = i + 1
print(s)
```

```{solution}
| ligne | condition (while) | s   | i   | print |
| :---: | :---------------: | :-: | :-: | :---: |
| 1 |              | 0   | ?   |  |
| 2 |              | 0   | 1   |  |
| 3 | 1 <= 5: Vrai | 0   | 1   |  |
| 4 |              | 1   | 1   |  |
| 5 |              | 1   | 2   |  |
| 3 | 2 <= 5: Vrai | 1   | 2   |  |
| 4 |              | 3   | 2   |  |
| 5 |              | 3   | 3   |  |
| 3 | 3 <= 5: Vrai | 3   | 3   |  |
| 4 |              | 6   | 3   |  |
| 5 |              | 6   | 4   |  |
| 3 | 4 <= 5: Vrai | 6   | 4   |  |
| 4 |              | 10  | 4   |  |
| 5 |              | 10  | 5   |  |
| 3 | 5 <= 5: Vrai | 10  | 5   |  |
| 4 |              | 15  | 5   |  |
| 5 |              | 15  | 6   |  |
| 3 | 6 <= 5: Faux | 15  | 6   |  |
| 6 |              | 15  | 6   | 15 |

Le programme affichera 15.
```

### Exercice {num2}`exercice`

En utilisant une boucle `while`, écrivez un programme qui:
- affiche tous les nombres entiers jusqu'à 15,
- à la fin, affiche "J'ai fini de compter!".

```{exec} python
:editor: ac83f5a3-c948-4491-b540-dc0d10402745
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
i = 1
while i <= 15:
  print(i)
  i += 1
print("J'ai fini de compter!")
```
````

### Exercice {num2}`exercice`

En utilisant une boucle `while`, écrivez un programme qui:
- demande un nombre entier à l'utilisateur,
- affiche les 5 premiers multiples de ce nombre.

```{exec} python
:editor: b5720432-d84a-4e5a-a1b6-121bdaea31a7
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
nombre = int(input("Choisissez un nombre: "))
i = 1
while i <= 5:
  print(i * nombre)
  i += 1
```
````

### Exercice {num2}`exercice:py1-boom`

Nous souhaitons créer un programme qui compte le temps avant qu'une bo
be explose. Pour cela, un compte à rebours commencera à 10 et ira jusqu'à 1, puis
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
:editor: fffa34af-43d1-40f0-ae0a-30c18ac2e5a0
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

### Exercice {num2}`exercice`

Complétez le programme pour qu'il demande à l'utilisateur la capitale de la
Suisse. Tant que la réponse n'est pas "Berne", le programme redemande une
nouvelle réponse.

Exemple d'exécution:

```{code-block} text
Quelle est la capitale de la Suisse?
Zurich
Faux, essaie encore!
Genève
Faux, essaie encore!
Berne
Bravo!
```

```{exec} python
:editor: c5bf6458-d3df-4458-bb42-6e6edeb8125c
capitale = input("Quelle est la capitale de la Suisse?")

# Complétez le programme ici
while ...:
  capitale = input("Faux, essaie encore!")
print("Bravo!")
```

````{solution}
```{exec} python
:linenos:
capitale = input("Quelle est la capitale de la Suisse?")

while capitale != "Berne":
  capitale = input("Faux, essaie encore!")
print("Bravo!")
```
````

### Exercice {num2}`exercice`

Tout d'abord, sans les exécuter, expliquez la différence entre les deux
programmes. Ensuite, testez-les pour vérifier votre réponse.

````{list-grid}
:style: grid-template-columns: 1fr 1fr;
- # Programme 1
  ```{exec} python
  :editor:
  n = 5
  if n < 10:
    n += 1
    print(n)
  ```
- # Programme 2
  ```{exec} python
  :editor:
  n = 5
  while n < 10:
    n += 1
    print(n)
  ```
````

```{solution}
Le programme 1 affichera:
6

Le programme 2 affichera:
6
7
8
9
10

Avec un `if` le condition est testée une seule fois, le bloc d'instructions est
lui aussi exécuté une seule fois, alors qu'avec le `while`, le bloc
d'intructions sera exécuté tant que la condition `n < 10` est vérifiée.
```

### Exercice {num2}`exercice`

Déterminez ce qu'affichera le programme en utilisant un
tableau d'états.

```{exec} python
:linenos:
x = 0
y = 20
while x < y:
  y -= x * 2
  x = x + 2
  print(x + y)
```

```{solution}
| ligne | condition (while) | x  | y  | print |
| :---: | :-------: | :-:| :-:| :---: |
| 1 |              | 0  | ?  |  |
| 2 |              | 0  | 20 |  |
| 3 | 0 < 20: vrai | 0  | 20 |  |
| 4 |              | 0  | 20 |  |
| 5 |              | 2  | 20 |  |
| 6 |              | 2  | 20 | 22 |
| 3 | 2 < 20: vrai | 0  | 20 |  |
| 4 |              | 2  | 16 |  |
| 5 |              | 4  | 16 |  |
| 6 |              | 4  | 16 | 20 |
| 3 | 4 < 16: vrai | 4  | 16 |  |
| 4 |              | 4  | 8  |  |
| 5 |              | 6  | 8  |  |
| 6 |              | 6  | 8 | 14 |
| 3 | 6 < 8: vrai  | 6  | 8  |  |
| 4 |              | 6  | -4 |  |
| 5 |              | 8  | -4 |  |
| 6 |              | 8  | -4 | 4 |
| 3 | 8 < -4: faux | 8  | -4 |  |
```

### Exercice {num2}`exercice`

Écrivez un programme dans lequel l'utilisateur peut consécutivement entrer les
notes qu'il a faites dans une branche. À la fin, le programme affichera le
nombre de notes insuffisantes qui ont été entrées. Les notes invalides seront
simplement ignorées. Pour terminer le programme, l'utilisateur entrera la note
`99`.

Exemple d'exécution:

```{code-block} text
Entrez une note: 4.5
Entrez une note: 3.4
Entrez une note: 6
Entrez une note: 3.9
Entrez une note: 5.1
Entrez une note: 99
Vous avez fait 2 notes insuffisantes
```

```{exec} python
:editor: 931d1c5b-562f-4541-b9f9-9507cb6e4ed1
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
nb_notes_insuf = 0
note = float(input("Entrez une note: "))
while note != 99:
    if note >= 1 and note < 4:
        nb_notes_insuf += 1
    note = float(input("Entrez une note: "))
print("Vous avez fait", nb_notes_insuf, "notes insuffisantes")
```
````

### Exercice {num2}`exercice`

Reprenez l'{numref}`exercice %s<exercice:py1-boom>` et modifiez-le pour qu'à
partir de 3, il affiche également "Fuyez!".

```{code-block} text
10
9
...
4
3 Fuyez!
2 Fuyez!
1 Fuyez!
BOOM
```

```{exec} python
:editor: 7ff640be-fd71-493b-bb0c-f7c495af9ac2
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
compte_a_rebours = 10
while compte_a_rebours > 0:
  if compte_a_rebours <= 3:
    print(compte_a_rebours, "Fuyez!")
  else:
    print(compte_a_rebours)
  compte_a_rebours -= 1
print("BOOM")
```
````

