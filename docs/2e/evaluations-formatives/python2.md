% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
subject: "Informatique 2e année"
solution: dynamic
```

# Quiz: Programmation en Python 2

````{poll} 089837e8-9b28-46a7-b35f-af57b127696d
:number: none
L'instruction pour créer une liste vide est ...

-   ```{exec} python
    :when: never
    liste = 0
    ```
-   :
    ```{exec} python
    :when: never
    liste = []
    ```
-   ```{exec} python
    :when: never
    liste = [0]
    ```
````

````{poll} d6ad2426-f731-43a8-9047-efa4f23b2eff
:number: none
L'instruction pour afficher le premier élément d'une liste est ...

-   ```{exec} python
    :when: never
    print(liste[-1])
    ```
-   ```{exec} python
    :when: never
    print(liste[1])
    ```
-   :
    ```{exec} python
    :when: never
    print(liste[0])
    ```
````

````{poll} 9c79557f-30a6-48e6-9e4c-98ec3fb67f18
:mode: multi
:number: none
L'instruction pour afficher le dernier élément d'une liste est ...

-   :
    ```{exec} python
    :when: never
    print(liste[-1])
    ```
-   ```{exec} python
    :when: never
    print(liste[len(liste)])
    ```
-   :
    ```{exec} python
    :when: never
    print(liste[len(liste)-1])
    ```
````


````{poll} d3f1ee65-2aaf-4588-8f63-eaad91bf183e
:number: none
L'instruction suivante ...
```{exec} python
:when: never
notes.insert(4, 3)
```

-   insère la note `4` à l'index 3.
-   : insère la note `3` à l'index 4.
-   insère la note `4` à l'index 2.
````

````{poll} 9346c879-3a8a-4a23-bd46-e319a6417574
:number: none
L'instruction suivante ...
```{exec} python
:when: never
del notes[5]
```

-   :efface l'élément à l'index 5.
-   efface la première occurence de la note 5.
-   efface toutes les notes 5 de la liste.
````

````{poll} e1292f16-a3d2-4e88-8235-a9704ba55bb1
:number: none
Qu'affiche le programme suivant?
```{exec} python
:when: never
liste = [2, 1, 7, 3]
liste.sort()
```

-   [1, 2, 3, 7]
-   [2, 1, 7, 3]
-   :rien
````

````{poll} 8d7b302a-dca7-42bf-bb19-709b18a2576e
:number: none
Qu'affiche le programme suivant?
```{exec} python
:when: never
liste = [6, 2, 5, 3]
liste.reverse()
print(liste)
```

-   [6, 5, 3, 2]
-   :[3, 5, 2, 6]
-   [6, 2, 5, 3]
````

````{poll} e1857ad8-bb09-4684-8240-862502ba43cb
:number: none
Qu'affiche le programme suivant?
```{exec} python
:when: never
liste = [3, 2, 8, 7]
print(liste.sum())
```

-   4
-   20
-   :une erreur
````

````{poll} 0a8d842e-686b-4a88-8de0-95e7a34abc52
:number: none
Qu'affiche le programme suivant?
```{exec} python
:when: never
liste = [3, 2, 6, 7, 1, 3, 4, 8]
for nombre in liste:
  if nombre % 2 == 1:
    print(nombre)
```

-   :
    ```{code} text
    3
    7
    1
    3
    ```
-   ```{code} text
    2
    6
    4
    8
    ```
-   ```{code} text
    2 6 4 8
    ```
````

````{poll} c5b8da75-17ea-48a3-ba51-3b22646b7a5d
:number: none
Qu'affiche le programme suivant?
```{exec} python
:when: never
liste = [3, 2, 6, 7, 1, 3, 4, 8]
for n in range(5):
  if n in liste:
    print(n)
```

-   ```{code} text
    0
    1
    2
    3
    4
    ```
-   ```{code} text
    1
    2
    3
    4
    5
    ```
-   :
    ```{code} text
    1
    2
    3
    4
    ```
````


````{poll} e98776eb-27fe-40d4-9066-9e7853c6964b
:number: none
L'instruction pour générer un nombre entier aléatoire entre 3 inclu et 7 inclu
est ...

-   ```{exec} python
    :when: never
    from random import randint
    nombre = randint(2, 7)
    ```
-   :
    ```{exec} python
    :when: never
    from random import randint
    nombre = randint(3, 7)
    ```
-   ```{exec} python
    :when: never
    from random import randint
    nombre = randint(3, 8)
    ```
````


