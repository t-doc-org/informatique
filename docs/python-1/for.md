% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Boucle for

```{metadata}
hide-solutions: true
```
## Répétition un bloc d'instructions

La boucle `for` permet de répéter un bloc d'instructions un nombre de fois connu
à l'avance.

```{exec} python
:when: never
for _ in range(nb_repetitions):
  instruction 1
  instruction 2
  ...
```

### Exemple {num}`ex-py1`

<table><tr style="text-align: center">
    <th style="width: 50%">Programme</th><th>Ordinogramme</th>
</tr><tr style="vertical-align: top"><td>

```{exec} python
:editor:
print("Voici ma punition:")
for _ in range(10):
  print("Je dois faire mes devoirs.")
print("J'ai fini.")
```

</td><td>

```{figure} images/boucle-for.png
:alt: Ordinogramme boucle for
:align: center
```

</td></tr></table>

### Exercice {num}`exo-py1`

Sans les exécuter, qu'afficheront les programmes suivants?

Ensuite, tester vos réponses en les exécutant.

1.  ```{exec} python
    :linenos:
    print("Lancer d'une pièce.")
    for _ in range(5):
      print("Pile")
    print("Fin du jeu")
    ```

2.  ```{exec} python
    :linenos:
    print("Lancer d'une pièce.")
    for _ in range(3):
      print("Pile")
      print("Face")
    print("Fin du jeu")
    ```

3.  ```{exec} python
    :linenos:
    print("Lancer d'une pièce.")
    for _ in range(2):
      print("Pile")
      print("Face")
      print("Pile")
    print("Fin du jeu")
    ```
3.  ```{exec} python
    :linenos:
    print("Lancer d'une pièce.")
    for _ in range(2):
      print("Pile")
      print("Face")
      print("Pile")
      print("Fin du jeu")
    ```

### Exercice {num}`exo-py1`

1. Que fait le programme suivant?
2. Modifiez-le pour qu'il affiche 9 fois "Salut".
3. Modifiez-le pour qu'il affiche:
    ```{code-block} text
    Salut
    Comment ça va?
    Salut
    Comment ça va?
    Salut
    Comment ça va?
    ```
4. Modifiez-le pour qu'à la fin du programme, il afficher "Au revoir!".

```{exec} python
:editor: cdf06593-2fc5-4f68-af74-2a6113bec6dc
for _ in range(6):
  print("Salut")
```

````{solution}
```{exec} python
:linenos:
for _ in range(3):
  print("Salut")
  print("Comment ça va?")
print("Au revoir!")
```
````

## Utilisation de la variable de la boucle`for

La boucle `for` fait plus que juste répéter x fois un bloc d'instructions: pour
chaque itération (passage de la boucle), la variable (dans l'exemple ci-dessous
nommée `i`) va prendre la valeur de l'ensemble `range(n)`, c'est-à-dire
l'ensemble des nombres entiers de $0$ à $n$ non compris $\{0; 1; 2; ...; n-1\}$.
Il est donc possible d'utiliser la valeur de cette variable dans la boucle.

```{important}
Dans `for _ in range(nb_repetitions):`, le `_` représente une variable que nous
pouvons appeler comme nous le souhaitons (en respectant les règles de nommage
des variables.)

Toutes ces notations sont correctes: `for _ in range(3):`,
`for nombre in range(3):`, `for i in range(3):`.

`for _ in range(3):` est utilisée seulement lorsque nous n'utilisons pas la
valeur de la variable dans la boucle.
```

### Exemple {num}`ex-py1`

Le programme suivant affiche les nombres de 0 à 9.

```{exec} python
:editor:
for i in range(10):
  print(i)
```

### Exercice {num}`exo-py1`

Écrivez un programme qui affiche les nombres entiers de 0 jusqu'à 17 et affiche
à la fin "J'ai fini de compter!".

```{exec} python
:editor: d9ce7741-30c3-4891-a481-0f84f99d4e9f
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
for nombre in range(18):
  print(nombre)
print("J'ai fini de compter!")
```
````

### Exercice {num}`exo-py1`

Modifiez le programme de l'exemple pour qu'il affiche les nombres entiers de 1 à
10.

```{exec} python
:editor: f0af01c7-fee8-47ef-bd3a-7ff011012f27
for i in range(10):
  print(i)
```

````{solution}
```{exec} python
:linenos:
for i in range(10):
  print(i + 1)
```

Python permet aussi de déterminer la valeur de départ et la valeur de fin (pas
comprise), en utilisant le construction suivante:
```{exec} python
:linenos:
for i in range(1, 11):
  print(i)
```
````

### Exercice {num}`exo-py1`

Écrivez un programme qui calcule et affiche la somme des dix premiers nombres
entiers.

```{exec} python
:editor: 861f4829-841e-48f7-8597-91d4153f3cde
# Écrivez le programme ici
```

````{solution}

Il y a plusieurs manières de faire.
1.  Comme ajouter 0 à une somme ne change rien, je peux effectuer le calcul
    suivant: $0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10$

    ```{exec} python
    :linenos:
    somme = 0
    for i in range(11):
      somme += i
    print(somme)
    ```

2.  Les deux programmes suivants font exactement ce qu'il faut:
    $1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10$

    ```{exec} python
    :linenos:
    somme = 0
    for i in range(10):
      somme += i + 1
    print(somme)
    ```

    ```{exec} python
    :linenos:
    somme = 0
    for i in range(1, 11):
      somme += i
    print(somme)
    ```
````

### Exercice {num}`exo-py1`

Écrivez un programme qui calcule et affiche le produit des cinq premiers nombres
entiers.

```{exec} python
:editor: 165c348a-10cd-4161-8ff4-d95acfbf7e25
# Écrivez le programme ici
```

````{solution}

```{exec} python
:linenos:
produit = 1
for i in range(5):
  produit *= i + 1
print(produit)
```

```{exec} python
:linenos:
produit = 1
for i in range(1, 6):
  produit *= i
print(produit)
```
````

### Exercice {num}`exo-py1`

Écrivez un programme qui demande à l'utilisateur un nombre entier et affiche les
10 premiers multiples de ce nombre.

```{exec} python
:editor: f935054b-3ed6-4a42-9e73-e6330a770f1d
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
nombre = int(await input_line("Choisissez un nombre: "))
for i in range(10):
  print(nombre * (i + 1))
```

```{exec} python
:linenos:
nombre = int(await input_line("Choisissez un nombre: "))
for i in range(1, 11):
  print(nombre * i)
```
````

### Exercice {num}`exo-py1`

Écrivez un programme qui affiche les nombres paires jusqu'à 20.

```{exec} python
:editor: c0a8317f-b8d9-465b-85f6-2865f32d4d6e
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
for i in range(20):
  if (i + 1) % 2 == 0:
    print(i + 1)
```

```{exec} python
:linenos:
for i in range(1, 21):
  if i % 2 == 0:
    print(i)
```
````

### Exercice {num}`exo-py1`

Écrivez un programme qui affiche le résultat des calculs suivants:

1. $1 + 2 + 3 + 4 + ... + 99 + 100$

    ```{exec} python
    :editor: f281c8dd-259a-431c-8a7b-f72732aee8db
    # Écrivez le programme ici
    ```

    ````{solution}
    ```{exec} python
    :linenos:
    somme = 0
    for i in range(100):
      somme += i + 1
    print(somme)
    ```

    ```{exec} python
    :linenos:
    somme = 0
    for i in range(1, 101):
      somme += i
    print(somme)
    ```
    ````

2. $1 + 3 + 5 + 7 + ... + 97 + 99$

    ```{exec} python
    :editor: 6d671b57-eff1-474e-8fed-4f8ddbb5595d
    # Écrivez le programme ici
    ```

    ````{solution}
    ```{exec} python
    :linenos:
    somme = 0
    for i in range(100):
      if (i + 1) % 2 == 1:
        somme += i + 1
    print(somme)
    ```

    ```{exec} python
    :linenos:
    somme = 0
    for i in range(1, 101):
      if i % 2 == 1:
        somme += i
    print(somme)
    ```
    ````

### Exercice {num}`exo-py1`

Bob souhaite construire une pyramide à base carrée comme sur la photo.

```{figure} images/pyramide.png
:alt: Pyramide
:width: 200px
:align: center
```

1. Écrivez un programme qui permet de calculer le nombre de billes nécessaires
  pour construire la pyramide de l'image (elle a 7 étages). Utiliser une boucle
  `for`.

    ```{exec} python
    :editor: e71a7353-1236-4047-8c5b-2dcd42017bfa
    # Écrivez le programme ici
    ```

    ````{solution}
    ```{exec} python
    :linenos:
    nb_billes = 0
    for i in range(7):
      nb_billes += (i + 1) ** 2
    print(nb_billes)
    ```

    ```{exec} python
    :linenos:
    nb_billes = 0
    for i in range(1, 8):
      nb_billes += i ** 2
    print(nb_billes)
    ```
    ````

2. Modifiez le programme précédent pour calculer le nombre de billes nécessaires
   pour construire une pyramide à 100 étages.

    ```{exec} python
    :editor: 277cfc59-fcf8-4667-a845-01585976347c
    # Écrivez le programme ici
    ```

    ````{solution}
    ```{exec} python
    :linenos:
    nb_billes = 0
    for i in range(100):
      nb_billes += (i + 1) ** 2
    print(nb_billes)
    ```

    ```{exec} python
    :linenos:
    nb_billes = 0
    for i in range(1, 101):
      nb_billes += i ** 2
    print(nb_billes)
    ```
    ````

3. Modifiez le programme pour que l'utilisateur puisse choisir le nombre
   d'étages.


    ```{exec} python
    :editor: 6c6da905-b3ad-4971-9ac0-705facf2a1e9
    # Écrivez le programme ici
    ```

    ````{solution}
    ```{exec} python
    :linenos:
    nb_etages = int(await input_line("Choisissez le nombre d'étages: "))
    nb_billes = 0
    for i in range(nb_etages):
      nb_billes += (i + 1) ** 2
    print(nb_billes)
    ```

    ```{exec} python
    :linenos:
    nb_etages = int(await input_line("Choisissez le nombre d'étages: "))
    nb_billes = 0
    for i in range(1, nb_etages + 1):
      nb_billes += i ** 2
    print(nb_billes)
    ```
    ````

### Exercice {num}`exo-py1`

Le 1{sup}`er` janvier, les parents de Chrystel ont déposé sur son livret
d'épargne 1500 CHF au taux de 2 %.

1. Écrivez un programme pour calculer le montant qu'elle aura après 1 an.

    ```{exec} python
    :editor: b0e0d36f-ab70-423e-bcaa-ed4c8007fad2
    # Écrivez le programme ici
    ```

    ````{solution}
    ```{exec} python
    :linenos:
    montant = 1500
    montant += 2 / 100 * montant
    print(montant)
    ```

    ```{exec} python
    :linenos:
    montant = 1500
    montant = 102 / 100 * montant
    print(montant)
    ```
    ````

2. Modifiez le programme précédent pour calculer le montant qu'elle aura dans 10
   ans. Utilisez une boucle `for`.

    ```{exec} python
    :editor: eb41dc15-477c-406c-80c9-9ec9a810f924
    # Écrivez le programme ici
    ```

    ````{solution}
    ```{exec} python
    :linenos:
    montant = 1500
    for _ in range(10):
      montant += 2 / 100 * montant
    print(montant)
    ```

    ```{exec} python
    :linenos:
    montant = 1500
    for _ in range(10):
      montant = 102 / 100 * montant
    print(montant)
    ```
    ````

3. Modifiez le programme pour que l'utilisateur puisse choisir la durée (le
   nombre d'années) et la montant initial.


    ```{exec} python
    :editor: 5fcdfd6a-df26-4601-841b-a827f878979f
    # Écrivez le programme ici
    ```

    ````{solution}
    ```{exec} python
    :linenos:
    montant = float(await input_line("Montant déposé: "))
    duree = int(await input_line("Durée du placement: "))
    for _ in range(duree):
      montant += 2 / 100 * montant
    print(montant)
    ```

    ```{exec} python
    :linenos:
    montant = float(await input_line("Montant déposé: "))
    duree = int(await input_line("Durée du placement: "))
    for _ in range(duree):
      montant = 102 / 100 * montant
    print(montant)
    ```
    ````

4. Modifiez le programme pour que l'utilisateur puisse aussi choisir le taux
   d'intérêt (en %).


    ```{exec} python
    :editor: 700fa29d-9736-4692-82b2-44ffce6c6d18
    # Écrivez le programme ici
    ```

    ````{solution}
    ```{exec} python
    :linenos:
    montant = float(await input_line("Montant déposé: "))
    duree = int(await input_line("Durée du placement: "))
    taux = int(await input_line("Taux d'intérêt en %: "))
    for _ in range(duree):
      montant += taux / 100 * montant
    print(montant)
    ```

    ```{exec} python
    :linenos:
    montant = float(await input_line("Montant déposé: "))
    duree = int(await input_line("Durée du placement: "))
    taux = int(await input_line("Taux d'intérêt en %: "))
    for _ in range(duree):
      montant = (taux + 100) / 100 * montant
    print(montant)
    ```
    ````
