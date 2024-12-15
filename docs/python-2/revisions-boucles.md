% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Révisions - Boucles

En programmation, nous sommes souvent amenés à répéter des instructions plusieurs
fois. Pour cela nous pouvons utiliser des boucles.

## Boucle for

La boucle 'for' permet de répéter un bloc d'instructions un nombre de fois connu
à l'avance.

```{exec} python
:when: never
for _ in range(nb_repetitions):
  instruction 1
  instruction 2
  ...
```

<table><tr style="text-align: center">
    <th style="width: 50%">Programme</th><th>Ordinogramme</th>
</tr><tr style="vertical-align: top"><td>

```{exec} python
:editor:
for i in range(5):
  print(i)
```

</td><td>

```{figure} images/for.png
:alt: Ordinogramme boucle for
:align: center
```

</td></tr></table>

1. Quelles valeurs prend la variable i?
2. Changer le nombre de répétitions.
3. Modifier le code pour afficher les nombres de 1 à 10?

En réalité, la boucle `for` fait plus que juste répéter x fois: pour
chaque itération (passage de la boucle), la variable (ici nommée i) va prendre
la valeur d'un élément de l'ensemble range(n), c'est-à-dire l'ensemble des
nombres entiers de 0 à n non compris $\{0; 1; 2; ...; n-1\}$. Il est donc
possible d'utiliser la valeur de cette variable dans la boucle.

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

<table><tr style="text-align: center">
  <th style="width: 50%">Programme</th><th>Ordinogramme</th>
</tr><tr style="vertical-align: top"><td>

```{exec} python
:editor:
nb_points = 0
max = 10
while nb_points < max:
  print("Points:", nb_points)
  nb_points += 3
print("Bravo!")
```

</td><td>

```{figure} images/while.png
:alt: Ordinogramme boucle for
:align: center
```

</td></tr></table>

## Exercice {num}`exo-py2-rev`

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

## Exercice {num}`exo-py2-rev`

1. Écrire un programme en utilisant le boucle `for` qui affiche les nombres de 0
à 9.

```{exec} python
:editor:
# Écrire le programme ici
```

````{solution}
```{exec} python
:linenos:
for nombre in range(10):
  print(nombre)
```
````

2. Écrire un programme en utilisant le boucle `for` qui affiche les nombres de 1
à 10.

```{exec} python
:editor:
# Écrire le programme ici
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

3. Écrire un programme en utilisant le boucle `for` qui affiche les 12 premiers
multiples de 5.

```{exec} python
:editor:
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

## Exercice {num}`exo-py2-rev`

Indiquer l'ordre d'exécution des lignes et ce qu'affichera le programme.

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

## Exercice {num}`exo-py2-rev`

Nous voulons créer un programme qui demande à l'utilisateur un nombre
strictement positif. Tant que l'utilisateur entre un nombre plus petit ou égal à
0, alors le programme devra lui redemander d'entrer un nouveau nombre.

Écrire un programme qui correspond à l'algorithme suivant:

```{code-block} text
Demander un nombre strictement positif à l'utilisateur et le stocker dans la variable n
Tant que n est plus petit ou égal à 0
    Afficher "Le nombre doit être strictement positif!"
    Demander un nombre positif à l'utilisateur et le stocker dans n
Afficher "Merci"
```

```{exec} python
:editor:
# Compléter le programme
n = int(await input_line("Entrer un nombre strictement positif: "))
print("Le nombre doit être strictement positif!")
print("Merci")
```

````{solution}
```{exec} python
:linenos:
n = int(await input_line("Entrer un nombre strictement positif: "))
while n <= 0:
  print("Le nombre doit être strictement positif!")
  n = int(await input_line("Entrer un nombre strictement positif: "))
print("Merci")
```
````

## Exercice {num}`exo-py2-rev`

Nous souhaitons créer un programme qui compte le temps avant qu'une bombe
explose. Pour cela, un compte à rebours commencera à 10 et ira jusqu'à 1, puis
le programme affichera "BOOM".

Écrire un programme qui correspond à l'algorithme suivant:

```{code-block} text
Initialiser une variable compte_a_rebours à 10
Tant que compte_a_rebours est plus grand que 0
    Afficher La valeur de compte_a_rebours
    Retirer 1 à compte_a_rebours
Afficher "BOOM"
```

Ce programme doit alors afficher :

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
:editor:
# Écrire le programme ici
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

## Exercice {num}`exo-py2-rev`

Écrire un programme qui demande à l'utilisateur combien il y a de cantons en
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
:editor:
# Écrire le programme ici
```

````{solution}
```{exec} python
:linenos:
nb_cantons = int(await input_line("Combien y a-t-il de cantons en Suisse?"))
while nb_cantons != 26:
  nb_cantons = int(await input_line("Faux, essaie encore!"))
print("Bravo!")
```
````

## Bonus {num}`bon-py2-rev`

Améliorer le programme de l'exercice précédent en indiquant à l'utilisateur
s'il y a plus ou moins de cantons en fonction de sa réponse.

## Exercice {num}`exo-py2-rev`

Indiquer l'ordre d'exécution des lignes et faire le tableau d'états du programme
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
