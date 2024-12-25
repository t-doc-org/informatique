% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Boucle for

```{metadata}
hide-solutions: true
```

La boucle `for` permet de répéter un bloc d'instructions un nombre de fois connu
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

## Exercice {num}`exo-py1`

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

## Exercice {num}`exo-py1`

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
