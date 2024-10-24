<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# Révisions - Instructions conditionnelles

Une instruction conditionnelle est composée d'une **condition** puis d'un
**bloc d'instructions**. La condition est une expression ou une variable logique
évaluée par `True` ou `False`. Le bloc d'instructions s'exécute seulement si la
condition est vérifiée.

## Exemple avec if

Le bloc d'instructions ne sera exécuté que si la condition est vraie.


```{figure} images/if.png
:alt: Ordinogramme if
:width: 300px
:align: center
```

```{exec} python
:linenos:
:editable:
print("Début")
meteo = "soleil"
if meteo == "pluie":
    print("Je prends un parapluie.")
print("Fin")
```

Dans l'exemple ci-dessus, il ne se passe rien, la condition n'est pas vérifiée.\
Changer la météo en "pluie". Que se passe-t-il?


## Exemple avec if ... else

Le bloc d'instructions après le `if` sera exécuté si la condition est vraie,
sinon ce sera le bloc d'instructions du `else` qui sera exécuté.

```{figure} images/if-else.png
:alt: Ordinogramme if-else
:width: 500px
:align: center
```

```{exec} python
:linenos:
:editable:
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
:linenos:
:editable:
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

## Exercice 7

```{exec} python
:name: python-buffer
:class: hidden
from io import StringIO
import sys

old_stdout = sys.stdout
sys.stdout = StringIO()
```

```{exec} python
:name: python-cond-valeur
:after: python-buffer
:when: never
:linenos:
x = 2
if x <= -1 :
    print(2 * x + 1)
elif x <=3 :
    print(-x + 2)
else :
    print(2 * x - 5)
```

```{exec} python
:linenos:
:after: python-cond-valeur
:when: load
:class: hidden
s = sys.stdout.getvalue().rstrip()
sys.stdout = old_stdout
while True:
    resp = await input_line("Que va afficher ce programme?")
    if resp == s: break
    if resp.replace(" ", "") == "-x+2":
        print("\x0cIl faut remplacer x par sa valeur.")
    else:
        print("\x0cEssaie encore.")
print("\x0cBravo!")
```

## Exercice 8

1.
    ```{exec} python
    :linenos:
    :editable:
    # Compléter le programme
    a = ...
    if ... :
        print("a est nul.")
    elif ... :
        print("a est plus petit que 0.")
    else:
        print("a est ...")
    ```

    Tester la justesse de votre code avec différentes valeurs de a.

    ````{admonition} Solution
    :class: note dropdown
    ```{exec} python
    :editable:
    :linenos:
    a = ...                                 # choisir la valeur de a
    if a == 0 :                             # a == 0 pour la comparaison
        print("a est nul.")
    elif a < 0 :
        print("a est plus petit que 0.")
    else:
        print("a est plus grand que 0")
    ```
    ````

2.
    ```{exec} python
    :linenos:
    :editable:
    # Compléter le programme
    a = ...
    b = ...
    if ... :                                        # tester que b n'est pas nul
        print(a / b)
    else:
        print("La division par 0 est impossible.")
    ```

    Tester la justesse de votre code avec différentes valeurs de a et de b.

    ````{admonition} Solution
    :class: note dropdown
    ```{exec} python
    :linenos:
    :editable:
    a = ...                                         # choisir la valeur de a
    b = ...                                         # choisir la valeur de b
    if b != 0 :                                     # tester que b n'est pas nul
        print(a / b)
    else:
        print("La division par 0 est impossible.")
    ```

## Exercice 9

Nous souhaitons créer un programme qui calcule le prix à payer lors de l'achat de
canette de Red Bull dont le prix unitaire est de 1.50 CHF.

Écrire un programme qui correspond à l'algorithme suivant:

```{code-block} text
Stocker le prix d'une canette de Red Bull dans la variable prix_unitaire
Demander à l'utilisateur combien de canettes il souhaite acheter et stocker cette valeur dans nb_canettes
Si le nb_canettes est plus petit que 0
    afficher "La quantité doit être un nombre positif."
Sinon
    calculer et afficher le prix à payer
```

```{exec} python
:linenos:
:editable:
# Modifier et compléter le programme
prix_unitaire = ...
nb_canettes = int(await input_line("Nombre de canettes de Red Bull à acheter?"))
```

````{admonition} Solution
:class: note dropdown
```{exec} python
:linenos:
prix_unitaire = 1.5
nb_canettes = int(await input_line("Nombre de canettes de Red Bull à acheter?"))
if nb_canettes < 0:
    print("La quantité doit être un nombre positif.")
else:
    print("Prix à payer:", nb_canettes * prix_unitaire, "CHF.")
```
````

## Exercice 10

Écrire un programme qui correspond à l'algorithme suivant:

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
:linenos:
:editable:
# Modifier et compléter le programme
... await input_line("Quel est votre âge?")
...
```

````{admonition} Solution
:class: note dropdown
```{exec} python
:linenos:
age = int(await input_line("Quel âge as-tu?"))
if  age < 16:
    print("Tu ne peux pas acheter d'alcool.")
elif age < 18:
    print("Tu peux acheter de la bière et du vin.")
else:
    print("Tu peux acheter de l'alcool.")
```
````

## Exercice 11

Voici trois programmes:

1. Quelles sont les différences?
2. Que vont-ils afficher?
3. Faire un ordinogramme pour chacun.

<table width="100%">
<tr>
      <th style="text-align: center">Programme 1</th>
      <th style="text-align: center">Programme 2</th>
      <th style="text-align: center">Programme 3</th>
</tr>
<tr><td>

```{exec} python
:linenos:
:editable:
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

</td><td>

```{exec} python
:linenos:
:editable:
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

</td><td>

```{exec} python
:linenos:
:editable:
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

</td></tr>
</table>



