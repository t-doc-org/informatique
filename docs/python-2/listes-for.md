% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Listes - Boucles `for`

```{metadata}
hide-solutions: true
```

La boucle `for` permet d'accéder à tous les éléments d'une liste l'un après
l'autre.

## Par position

Dans ce cas, les éléments sont parcourus au moyen de leur index. Pour déterminer
l'index du dernier élément et éviter une erreur lors de l'exécution, nous
utilisons la fonction `len(liste)` qui retourne le nombre d'élément dans une
liste.

### Exemple {num}`ex-py2`

```{exec} python
:editor:
notes = [5, 5.5, 4, 5.5, 6]

# Cette boucle parcourt tous les index de la liste de 0 à la longueur de la liste - 1
for i in range(len(notes)):
  print(notes[i])
```

## Par élément

En Python, il est possible de parcourir directement les éléments d'une liste.

### Exemple {num}`ex-py2`

```{exec} python
:editor:
notes = [5, 5.5, 4, 5.5, 6]

# Cette boucle parcourt les éléments les uns après les autres
for note in notes:    # La variable note change de valeur à chaque itération
  print(note)
```

## Exercice {num}`exo-py2`

Avant de les exécuter, déterminez ce que font les programmes suivants.

1.  ```{exec} python
    :editor: 62c85fe3-5435-4c6e-8c68-c88763bc0f0e
    questions = ["Quelle est ta couleur préférée?",
                 "Quel est ton animal préféré?",
                 "Où étudies-tu?"]
    reponses = []

    for question in questions:
      print(question)
      reponse = await input_line("Réponse: ")
      reponses.append(reponse)

    print("Tes réponses: ", reponses)
    if reponses[2] == "STX":
      print("Tu es dans la meilleure école ;-)")
    ```

2.  ```{exec} python
    :editor: 7f08c47a-00a7-47f8-9ce1-305e46961f22
    notes = [5.5, 3.8, 6, 6, 3.5, 4,5]
    nb_notes_insuf = 0

    for note in notes:
      if note < 4:
        nb_notes_insuf += 1

    print("Tu as fait", nb_notes_insuf, "notes insuffisantes.")
    ```

## Exercice {num}`exo-py2`

1. Écrivez une programme qui génère une liste de 50 nombres entiers tirés au
hasard entre 1 et 1000.
2. Déterminez le maximum de la liste en définissant une fonction
`maximum(liste)`.
3. Déterminez le minimum de la liste en définissant une fonction
`minimum(liste)`.

```{exec} python
:editor: 51fa6ba6-954c-4728-ab9a-b264c595416f
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
from random import randint

def maximum(listes_nombres):
  max = 0
  for nombre in listes_nombres:
    if nombre > max:
      max = nombre
  return max

def minimum(listes_nombres):
  min = 1000
  for nombre in listes_nombres:
    if nombre < min:
      min = nombre
  return min


nombres = []

# Genère la liste de 50 nombres entiers
for _ in range(50):
  nombres.append(randint(1, 1000))

print("Le maximum est", maximum(nombres))
print("Le minimum est", minimum(nombres))
print(nombres)
```
````

## Exercice {num}`exo-py2`

Complétez le programme ci-dessous afin qu'il affiche correctement l'itinéraire
de la manière suivante:

```{code-block} text
Début de l'itinéraire
Vas à Bulle
Vas à Riaz
Vas à Marsens
Vas à Echarlens
Vas à Charmey
Tu es arrivé!
```

```{exec} python
:editor: dc635abe-c4ee-4beb-badd-02733dff234e
itineraire = ["Bulle", "Riaz", "Marsens", "Echarlens", "Charmey"]

# Complétez le programme à partir de là
```

````{solution}
```{exec} python
:linenos:
itineraire = ["Bulle", "Riaz", "Marsens", "Echarlens", "Charmey"]
print("Début de l'itinéraire")
for ville in itineraire:
    print("Vas à", ville)
print("Tu es arrivé!")
```
````

## Exercice {num}`exo-py2`

Une liste de notes a été donnée par un autre utilisateur et sauvegardée dans la
variable `notes`.

1. Calculez le nombre de notes insuffisantes.
2. Calculez la moyenne.
3. Déterminez la meilleure note obtenue.

Ne vous préoccupez pas de la première ligne, celle-ci permet juste de demander
une liste à l'utilisateur et d'enregistrer le résultat dans la variable `notes`.

```{exec} python
:name: python-liste-notes
:class: hidden
from random import uniform, randint

def genere_liste_notes(nb_notes):
  notes = []
  for _ in range(nb_notes):
    notes.append(round(uniform(2, 6), 1))
  return notes

notes = genere_liste_notes(randint(7, 15))
```

```{exec} python
:after: python-liste-notes
:editor: 7b52a83c-340a-4748-8f66-4b415d06aef6
print(notes)

# Complétez le progamme à partir de là
nb_notes_insuffisantes =

moyenne =

meilleure_note =

print("Il y a ", nb_notes_insuffisantes, "notes insuffisantes.")
print("La moyenne est de", moyenne)
print("La meilleure note obtenue est", meilleure_note)
```

````{solution}
```{exec} python
:linenos:
:after: python-liste-notes
print(notes)
nb_notes_insuffisantes = 0
for note in notes:
    if note < 4:
        nb_notes_insuffisantes += 1
print(nb_notes_insuffisantes)
moyenne = sum(notes) / len(notes)

meilleure_note = 0
for note in notes:
    if note > meilleure_note:
        meilleure_note = note

print("Il y a ", nb_notes_insuffisantes, "notes insuffisantes.")
print("La moyenne est de", moyenne)
print("La meilleure note obtenue est", meilleure_note)

```
````
