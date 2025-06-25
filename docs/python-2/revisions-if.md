% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Révisions - Instructions conditionnelles

Une instruction conditionnelle est composée d'une **condition** puis d'un
**bloc d'instructions**. La condition est une expression ou une variable logique
évaluée par `True` ou `False`. Le bloc d'instructions s'exécute seulement si la
condition est vérifiée.

## Opérateurs logiques

Les opérateurs logiques permettent de combiner plusieurs conditions simples

| Opérateur | Description          |
| :-------: | :------------------: |
| and       | retourne True si les deux conditions sont vraies |
| or        | retourne True si une des conditions est vraie    |
| not       | inverse le résultat, renvoie True si le résultat est faux et vice-versa |

## Exemple avec if

Le bloc d'instructions ne sera exécuté que si la condition est vraie.

```{figure} images/if.png
:alt: Ordinogramme if
:width: 300px
:align: center
```

```{exec} python
:editor:
print("Début")
meteo = "soleil"
if meteo == "pluie":
  print("Je prends un parapluie.")
print("Fin")
```

Dans l'exemple ci-dessus, il ne se passe rien, la condition n'est pas vérifiée.\
Changez la météo en "pluie". Que se passe-t-il?

## Exemple avec if ... else

Le bloc d'instructions après le `if` sera exécuté si la condition est vraie,
sinon ce sera le bloc d'instructions du `else` qui sera exécuté.

```{figure} images/if-else.png
:alt: Ordinogramme if-else
:width: 500px
:align: center
```

```{exec} python
:editor:
moyenne = 5
if moyenne >= 4:
  print("Moyenne suffisante")
else:
  print("Moyenne insuffisante")
```

Dans l'exemple ci-dessus, soit la moyenne est suffisante (moyenne supérieure ou
égale à 4), soit elle est insuffisante (moyenne inférieure à 4). Il n'y a pas
d'autres possibilités.

## Exemple avec if ... elif ... else

Certaines situations nécessitent de distinguer plus qu'un ou deux cas.

```{figure} images/if-elif-else.png
:alt: Ordinogramme if-elif-else
:width: 100%
:align: center
```

```{exec} python
:editor:
type_film = "comédie"

if type_film == "action":
  print("Explosions et des cascades de folie!")
elif type_film == "comédie":
  print("Mort de rire!")
elif type_film == "horreur":
  print("Terrifiant!")
else:
  print("Je ne connais pas.")
```

Dans l'exemple ci-dessus, il y a le choix entre trois types de films (action,
comédie et horreur). Le branchement `else` gérera tous les autres cas.

## Exercice {num}`exo-py2-rev`

```{exec} python
:when: never
:linenos:
age = int(input("Quel âge as-tu? "))
if age >= 18:
  print("Tu es majeur.")
else:
  print("Tu es mineur.")
```

1. Quel message sera affiché si l'utilisateur entre 21?
2. Que se passe-t-il si l'utilisateur entre 16 ans?
3. Que se passe-t-il si l'utilisateur entre -10?
4. Que se passe-t-il si l'utilisateur entre 17.5?

````{solution}
Vérifie tes réponses en exécutant le code.
```{exec} python
:linenos:
age = int(input("Quel âge as-tu? "))
if age >= 18:
  print("Tu es majeur.")
else:
  print("Tu es mineur.")
```
````

## Exercice {num}`exo-py2-rev`

```{role} input(quiz-input)
:right: width: 10rem;
:check: json remove
```

````{quiz}
{input}`{"0": true, "-x+2": "Il faut remplacer x par sa valeur."}`
Que va afficher ce programme?

```{code-block} python
:linenos:
x = 2
if x <= -1:
  print(2 * x + 1)
elif x <= 3:
  print(-x + 2)
else:
  print(2 * x - 5)
```
````

## Exercice {num}`exo-py2-rev`

1.  ```{exec} python
    :editor:
    # Complétez le programme
    a = ...
    if ... :
      print("a est nul.")
    elif ... :
      print("a est plus petit que 0.")
    else:
      print("a est ...")
    ```

    Testez la justesse de votre code avec différentes valeurs de a.

    ````{solution}
    ```{exec} python
    :editor:
    a = ...                                 # choisir la valeur de a
    if a == 0 :                             # a == 0 pour la comparaison
      print("a est nul.")
    elif a < 0 :
      print("a est plus petit que 0.")
    else:
      print("a est plus grand que 0")
    ```
    ````

2.  ```{exec} python
    :editor:
    # Complétez le programme
    a = ...
    b = ...
    if ... :                                        # tester que b n'est pas nul
      print(a / b)
    else:
      print("La division par 0 est impossible.")
    ```

    Testez la justesse de votre code avec différentes valeurs de a et de b.

    ````{solution}
    ```{exec} python
    :editor:
    a = ...                                         # choisir la valeur de a
    b = ...                                         # choisir la valeur de b
    if b != 0 :                                     # tester que b n'est pas nul
      print(a / b)
    else:
      print("La division par 0 est impossible.")
    ```

## Exercice {num}`exo-py2-rev`

Nous souhaitons créer un programme qui calcule le prix à payer lors de l'achat de
canette de Red Bull dont le prix unitaire est de 1.50 CHF.

Écrivez un programme qui correspond à l'algorithme suivant:

```{code-block} text
Stocker le prix d'une canette de Red Bull dans la variable prix_unitaire
Demander à l'utilisateur combien de canettes il souhaite acheter et stocker cette valeur dans nb_canettes
Si le nb_canettes est plus petit que 0
    afficher "La quantité doit être un nombre positif."
Sinon
    calculer et afficher le prix à payer
```

```{exec} python
:editor: 62b603f8-6468-490d-ad94-a7afe58a5e14
# Modifiez et complétez le programme
prix_unitaire = ...
nb_canettes = int(input("Nombre de canettes de Red Bull à acheter?"))
```

````{solution}
```{exec} python
:linenos:
prix_unitaire = 1.5
nb_canettes = int(input("Nombre de canettes de Red Bull à acheter?"))
if nb_canettes < 0:
  print("La quantité doit être un nombre positif.")
else:
  print("Prix à payer:", nb_canettes * prix_unitaire, "CHF.")
```
````

## Exercice {num}`exo-py2-rev`

Écrivez un programme qui correspond à l'algorithme suivant:

```{code-block} text
Demander l'âge de l'utilisateur et le stocker dans la variable age
Si age est plus petit que 16
    afficher "Tu ne peux pas acheter d'alcool."
Sinon si age est plus petit que 18
    afficher "Tu peux acheter de la bière et du vin."
Sinon
    afficher "Tu peux acheter de l'alcool."
```

```{exec} python
:editor: 473120c2-5476-4dd2-abf5-eba9e1cb2f97
# Modifiez et complétez le programme
... input("Quel est votre âge?")
...
```

````{solution}
```{exec} python
:linenos:
age = int(input("Quel âge as-tu?"))
if  age < 16:
  print("Tu ne peux pas acheter d'alcool.")
elif age < 18:
  print("Tu peux acheter de la bière et du vin.")
else:
  print("Tu peux acheter de l'alcool.")
```
````

## Exercice {num}`exo-py2-rev`

Voici trois programmes:

1. Quelles sont les différences?
2. Que vont-ils afficher?
3. Faites un ordinogramme pour chacun.

<table style="width: 100%"><tr style="text-align: center">
  <th>Programme 1</th><th>Programme 2</th><th>Programme 3</th>
</tr><tr style="vertical-align: top"><td>

```{exec} python
:linenos:
x = -4
if x < 0:
  x += 7
if x < 5:
  x *= 4
if x < 10:
  x -= 6
else:
  x = 1000
print(x)
```

</td><td style="padding-left: 1rem">

```{exec} python
:linenos:
x = -4
if x < 0:
  x += 7
elif x < 5:
  x *= 4
elif x < 10:
  x -= 6
else:
  x = 1000
print(x)
```

</td><td style="padding-left: 1rem">

```{exec} python
:linenos:
x = -4
if x < 0:
  x += 7
  if x < 5:
    x *= 4
    if x < 10:
      x -= 6
else:
  x = 1000
print(x)
```

</td></tr></table>

## Exercice {num}`exo-py2-rev`

Que vont afficher chacun de ces programmes?

<table style="width: 100%"><tr style="text-align: center">
  <th style="width: 50%">Programme 1</th><th>Programme 2</th>
</tr><tr style="vertical-align: top"><td>

```{exec} python
:linenos:
a = 22
b = 5
c = 1
print((a > b) and (b <= c))
```

</td><td style="padding-left: 1rem">

```{exec} python
:linenos:
a = 11
b = 3
c = 0
print((a < b) or (c == 0))

```

</td></tr></table>

<table style="width: 100%"><tr style="text-align: center">
  <th style="width: 50%">Programme 3</th><th>Programme 4</th>
</tr><tr style="vertical-align: top"><td>

```{exec} python
:linenos:
a = 11
b = 3
c = 0
print((a < b) or (c != 0))

```

</td><td style="padding-left: 1rem">

```{exec} python
:linenos:
a = 1.5
b = 3.2
print(not(a <= b))
```

</td></tr></table>

## Exercice {num}`exo-py2-rev`

Le programme suivant contient une erreur de logique. Testez le programme avec
différentes valeurs pour la trouver et corrigez-la.

```{exec} python
:editor:
age = 18
if age >= 18:
  print("Tu payes le prix adulte.")
elif age >= 65:
  print("Tu payes le prix retraité")
else:
  print("Tu payes le prix enfant.")
```

```{solution}
Le `elif` ne sera jamais exécuté, car si l'âge est supérieur ou égal à 65, il
est aussi supérieur ou égal à 18. Donc la condition du `if` sera vérifiée.
```
