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

<table>
<tr>
    <th style="text-align: center">Programme</th>
    <th style="text-align: center">Ordinogramme</th>
</tr>
<tr><td width="50%"; valign="top">

```{exec} python
:linenos:
:editable:
for i in range(5):
    print(i)
```

</td><td>

```{figure} images/for.png
:alt: Ordinogramme boucle for
:align: center
```

</td></tr>
</table>

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

<table>
<tr>
    <th style="text-align: center">Programme</th>
    <th style="text-align: center">Ordinogramme</th>
</tr>
<tr><td width="50%"; valign="top">

```{exec} python
:linenos:
:editable:
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

</td></tr>
</table>

## Exercice 14
```{exec} python
:linenos:
:when: never
somme = 0
for nombre in range(6):
    somme += nombre
print("La somme est:", somme)
```

Quel est le résultat affiché par ce programme?

````{admonition} Solution
:class: note dropdown
Vérifie ta réponse en exécutant le code.
```{exec} python
:linenos:
somme = 0
for nombre in range(6):
    somme += nombre
print("La somme est:", somme)
```
````

## Exercice 15

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
:linenos:
:editable:
# Compléter le programme
n = int(await input_line("Entrer un nombre strictement positif: "))
print("Le nombre doit être strictement positif!")
print("Merci")
```

````{admonition} Solution
:class: note dropdown
```{exec} python
:linenos:
n = int(await input_line("Entrer un nombre strictement positif: "))
while n <= 0:
    print("Le nombre doit être strictement positif!")
    n = int(await input_line("Entrer un nombre strictement positif: "))
print("Merci")
```
````

## Exercice 16

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
:linenos:
:editable:
# écrire le programme ici
```

````{admonition} Solution
:class: note dropdown
```{exec} python
:linenos:
compte_a_rebours = 10
while compte_a_rebours > 0:
    print(compte_a_rebours)
    compte_a_rebours -= 1
print("BOOM")
```
````

## Exercice 17

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
:linenos:
:editable:
# écrire le programme ici
```

````{admonition} Solution
:class: note dropdown
```{exec} python
:linenos:
nb_cantons = int(await input_line("Combien y a-t-il de cantons en Suisse?"))
while nb_cantons != 26:
    nb_cantons = int(await input_line("Faux, essaie encore!"))
print("Bravo!")
```
````

## Bonus 1

Améliorer le programme de l'exercice précédent en indiquant à l'utilisateur
s'il y a plus ou moins de cantons en fonction de sa réponse.

