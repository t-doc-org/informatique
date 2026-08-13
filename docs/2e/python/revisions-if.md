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
| or        | retourne True si au moins une des conditions est vraie    |
| not       | inverse le résultat, renvoie True si le résultat est faux et vice-versa |

## Exercice {num2}`exercice-rev`

Est-ce que les conditions suivantes sont `True` (vrai) ou `False` (faux)?

```{role} select(quiz-select)
:right:
:options: |
: True
: False
```

```{quiz}
:style: max-width: 25rem;
1.  {select}`True`  `1 + 1 == 2`
2.  {select}`False` `2 * 3 == 3`
3.  {select}`True`  `2 + 3 != 4`
4.  {select}`False` `14 >= 15`
5.  {select}`False` `2 ** 3 == 6`
6.  {select}`True`  `13 >= 13`
```

## Exercice {num2}`exercice-rev`

Est-ce que les conditions suivantes sont `True` (vrai) ou `False` (faux),
sachant que la variable `pays` contient la valeur `"Suisse"` et la variable
`temperature` la valeur `26.2`.

```{role} select(quiz-select)
:right:
:options: |
: True
: False
```

```{quiz}
:style: max-width: 25rem;
1.  {select}`True`  `pays == "Suisse"`
2.  {select}`True` `pays != "France"`
3.  {select}`True`  `temperature > 20`
4.  {select}`False` `temperature < 26.2`
5.  {select}`False` `temperature < 26`
6.  {select}`False`  `temperature != 26.2`
```

## Exercice {num2}`exercice-rev`

Que vont afficher chacun de ces programmes?

```{role} input(quiz-input)
:style: width: 100%;
```

````{list-grid}
:style: grid-template-columns: 1fr 1fr;
- # Programme 1
  Que va afficher ce programme?

  ```{exec} python
  :name: prog2.1
  :when:
  :linenos:
  a = 22
  b = 5
  c = 1
  print((a > b) and (b <= c))
  ```
  ```{quiz}
  {input}`False`
  ```
- # Programme 2
  Que va afficher ce programme?

  ```{exec} python
  :name: prog2.2
  :when:
  :linenos:
  a = 11
  b = 3
  c = 0
  print((a < b) or (c == 0))
  ```
  ```{quiz}
  {input}`True`
  ```
- # Programme 3
  Que va afficher ce programme?

  ```{exec} python
  :name: prog2.3
  :when:
  :linenos:
  a = 11
  b = 3
  c = 0
  print((a < b) or (c != 0))
  ```
  ```{quiz}
  {input}`False`
  ```
- # Programme 4
  Que va afficher ce programme?

  ```{exec} python
  :name: prog2.4
  :when:
  :linenos:
  a = 1.5
  b = 3.2
  print(not(a <= b))
  ```
  ```{quiz}
  {input}`False`
  ```
````

`````{solution}
````{list-grid}
:style: grid-template-columns: 1fr 1fr;
- # Programme 1
  ```{exec} python
  :after: prog2.1
  :when: load
  :class: hidden
  ```
- # Programme 2
  ```{exec} python
  :after: prog2.2
  :when: load
  :class: hidden
  ```
- # Programme 3
  ```{exec} python
  :after: prog2.3
  :when: load
  :class: hidden
  ```
- # Programme 4
  ```{exec} python
  :after: prog2.4
  :when: load
  :class: hidden
  ```
````
`````

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

## Exercice {num2}`exercice-rev`

```{exec} python
:when:
:linenos:
age = int(input("Quel âge as-tu? "))
if age >= 18:
  print("Tu es majeur.")
else:
  print("Tu es mineur.")
```

1. Quel message sera affiché si l'utilisateur répond 21?
2. Que se passe-t-il si l'utilisateur entre 16 ans?
3. Que se passe-t-il si l'utilisateur entre -10?
4. Que se passe-t-il si l'utilisateur entre 17.5?

````{solution}
Vérifiez vos réponses en exécutant le code.
```{exec} python
:linenos:
age = int(input("Quel âge as-tu? "))
if age >= 18:
  print("Tu es majeur.")
else:
  print("Tu es mineur.")
```
````

## Exercice {num2}`exercice-rev`

```{role} input(quiz-input)
:style: width: 100%;
:check: json remove
```

{.lower-alpha-paren .grid-2}
1.  Que va afficher ce programme?

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
    ```{quiz}
    {input}`{"0": true, "-x+2": "Il faut remplacer x par sa valeur."}`
    ```
2.  Que va afficher ce programme?

    ```{code-block} python
    :linenos:
    x = -4
    if x <= -1:
      print(2 * x + 1)
    elif x <= 3:
      print(-x + 2)
    else:
      print(2 * x - 5)
    ```
    ```{quiz}
    {input}`{"-7": true, "2*x+1": "Il faut remplacer x par sa valeur.", "9": "2 * (-4) = -8", "-9": "Il faut ajouter 1, pas enlever 1."}`
    ```
3.  Que va afficher ce programme?

    ```{code-block} python
    :linenos:
    x = 4
    if x <= -1:
      print(2 * x + 1)
    elif x <= 3:
      print(-x + 2)
    else:
      print(2 * x - 5)
    ```
    ```{quiz}
    {input}`{"3": true, "2*x-5": "Il faut remplacer x par sa valeur."}`
    ```
4.  Que va afficher ce programme?

    ```{code-block} python
    :linenos:
    x = 2
    if x <= 3:
      print(-x + 2)
    elif x <= -1:
      print(2 * x + 1)
    else:
      print(2 * x - 5)
    ```
    ```{quiz}
    {input}`{"0": true, "-x+2": "Il faut remplacer x par sa valeur."}`
    ```
5.  Que va afficher ce programme?

    ```{code-block} python
    :linenos:
    x = -4
    if x <= 3:
      print(-x + 2)
    elif x <= -1:
      print(2 * x + 1)
    else:
      print(2 * x - 5)
    ```
    ```{quiz}
    {input}`{"6": true, "-7": "Quelle est la première expression vraie?", "-1": "-(-4) = 4"}`
    ```
6.  Que va afficher ce programme?

    ```{code-block} python
    :linenos:
    x = 4
    if x <= -1:
      print(2 * x + 1)
    elif x <= 3:
      print(-x + 2)
    else:
      print(2 * x - 5)
    ```
    ```{quiz}
    {input}`{"3": true, "2*x-5": "Il faut remplacer x par sa valeur."}`
    ```

## Exercice {num2}`exercice-rev`

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

    Testez la justesse de votre code avec  a= -7, a = 0 et a = 11.

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

    Testez la justesse de votre code avec différentes valeurs de a et de b
    (a = 7, b = 2 / a = 15, b = -3 / a = 0 , b = 5 / a = 12 , b = 0).

    ````{solution}
    ```{exec} python
    :editor:
    a = 3                                           # choisir la valeur de a
    b = 4                                           # choisir la valeur de b
    if b != 0 :                                     # tester que b n'est pas nul
      print(a / b)
    else:
      print("La division par 0 est impossible.")
    ```

## Exercice {num2}`exercice-rev`

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

## Exercice {num2}`exercice-rev`

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

## Exercice {num2}`exercice-rev`

Le programme ci-dessous demande 3 notes à l'utilisateur. Complétez-le de
manière à ce qu'il:

1.  calcule et affiche la moyenne des 3 notes,
2.  affiche `Tu n'as aucune note insuffissante` seulement si ces 3 notes
    sont supérieures ou égales à 4.

```{exec} python
:editor: 57882fac-75bb-4b55-8397-fc19ed69d9b8
math = float(input("Quelle est ta note de math?"))
français = float(input("Quelle est ta note de français?"))
allemand = float(input("Quelle est ta note d'allemand?"))

# Complétez le code à partir de là
# Calculez et afficher la moyenne
print("La moyenne est de")

# Testez et affichez si toutes les notes sont suffisantes ou pas
print("Tu n'as aucune note insuffisante")

print("Tu as au moins 1 note insuffisante")
```

````{solution}
```{exec} python
:linenos:
math = float(input("Quelle est ta note de math?"))
francais = float(input("Quelle est ta note de français?"))
allemand = float(input("Quelle est ta note d'allemand?"))

# Calculez et afficher la moyenne
moyenne = (math + francais + allemand) / 3
print("La moyenne est de", moyenne)

# Testez et affichez si toutes les notes sont suffisantes ou pas
if math >= 4 and francais >= 4 and allemand >= 4:
  print("Tu n'as aucune note insuffisante")
else:
  print("Tu as au moins 1 note insuffisante")
```
````

## Exercice {num2}`exercice-rev`

Quelles sont les différences entre ces trois programmes?

```{role} input(quiz-input)
:style: width: 100%;
```

`````{list-grid}
:style: grid-template-columns: 1fr 1fr 1fr;
  - # Programme 1
    Que va afficher ce programme?

    ```{exec} python
    :when:
    :name: prog1.1
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
    ````{quiz}
    {input}`1000`
    ````
  - # Programme 2
    Que va afficher ce programme?

    ```{exec} python
    :when:
    :name: prog1.2
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
    ````{quiz}
    {input}`3`
    ````
  - # Programme 3
    Que va afficher ce programme?

    ```{exec} python
    :when:
    :name: prog1.3
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
    ````{quiz}
    {input}`12`
    ````
`````

`````{solution}
````{list-grid}
:style: grid-template-columns: 1fr 1fr 1fr;
- # Programme 1
  ```{exec} python
  :after: prog1.1
  :when: load
  :class: hidden
  ```
- # Programme 2
  ```{exec} python
  :after: prog1.2
  :when: load
  :class: hidden
  ```
- # Programme 3
  ```{exec} python
  :after: prog1.3
  :when: load
  :class: hidden
  ```
````
`````
