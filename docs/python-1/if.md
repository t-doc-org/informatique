% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Instructions conditionnelles

```{metadata}
hide-solutions: true
scripts:
  - src: quizz-helpers.js
```

Une instruction conditionnelle est composée d'une **condition** puis d'un
**bloc d'instructions**. La condition est une expression ou une variable logique
évaluée par `True` ou `False`. Le bloc d'instructions s'exécute seulement si la
condition est vérifiée.

## Opérateurs de comparaison

Les opérateurs de comparaison permettent de comparer deux valeurs entre elles.
Le résultat de la comparaison est de type booléen: True ou False.

| Opérateur | Nom                  | Exemple | Résultat |
| :-------: | :------------------: | :-----: | :------: |
| ==        | égal à               | 3 == 7  | False    |
| !=        | différent de         | 3 != 7  | True     |
| >         | plus grand que       | 3 > 7   | False    |
| <         | plus petit que       | 3 < 7   | True     |
| >=        | plus grand ou égal à | 3 >= 7  | False    |
| <=        | plus petit ou égal à | 3 <= 7  | True     |

### Exercice {num}`exo-py1`

Est-ce que les expressions suivantes sont `True` (vrai) ou `False` (faux)?

1.  <script>tdoc.question("1 + 1 == 2", {'true': true, 'vrai': true});</script>
2.  <script>tdoc.question("2 * 3 == 3", {'false': true, 'faux': true});</script>
3.  <script>tdoc.question("2 + 3 != 4", {'true': true, 'vrai': true});</script>
4.  <script>tdoc.question("14 >= 15", {'false': true, 'faux': true});</script>
5.  <script>
    tdoc.question("2 ** 3 == 6", {'false': true, 'faux': true});
    </script>
6.  <script>tdoc.question("13 >= 13", {'true': true, 'vrai': true});</script>

## Exemple if {num}`ex-py1`

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
Changez la valeur de la variable `meteo` en "pluie". Que se passe-t-il?

## Exemple if ... else {num}`ex-py1`

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
d'autres possibilités. Changez la valeur de la variable `moyenne` en 3. Que se
passe-t-il?

## Exemple if ... elif ... else {num}`ex-py1`

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
comédie et horreur). Le branchement `else` gérera tous les autres cas. Remplacer
la valeur de la variable `type_film` par "action", "horreur" ou "drame". Que se
passe-t-il?

### Exercice {num}`exo-py1`

Écrivez l'algorithme suivant en Python:

```{code-block} text
Demander à l'utilisateur d'entrer un nombre positif
Sauvegarder la valeur dans la variable a
Si a est plus petit que 0 alors
  écrire "Ce nombre n'est pas positif."
```

```{exec} python
:editor: f0cd9039-aa2a-4a6e-a855-ad51d4cd557e
a = float(await input_line("Entrez un nombre positif: "))
# Complétez le programme ici
```

````{solution}
```{exec} python
:linenos:
a = float(await input_line("Entrez un nombre positif: "))
if a < 0:
  print("Ce nombre n'est pas positif.")
```
````

### Exercice {num}`exo-py1`

Écrivez l'algorithme suivant en Python:

```{code-block} text
Demander à l'utilisateur d'entrer la valeur de a
Sauvegarder la valeur dans la variable a
Demander à l'utilisateur d'entrer la valeur de b
Sauvegarder la valeur dans la variable b
Si a est plus petit que b alors
  écrire "a est plus petit que b"
Sinon
  écrire "a est plus grand que b"
```

```{exec} python
:editor: 3d40e18b-534c-48ae-a1a3-025ad03f9392
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
a = float(await input_line("Valeur de a: "))
b = float(await input_line("Valeur de b: "))
if a < b:
  print("a est plus petit que b.")
else:
  print("a est plus grand que b.")
```
````

### Exercice {num}`exo-py1`

Reprenons l'exercice précédent. Que se passe-t-il si a = 0?

Améliorez le programme précédent en traitant aussi le cas où a = 0.

```{exec} python
:editor: d5a6da62-0c1a-4ea7-a1b2-910848086c35
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
a = float(await input_line("Valeur de a: "))
b = float(await input_line("Valeur de b: "))
if a == b:
  print("a est égal à b.")
elif a < b:
  print("a est plus petit que b.")
else:
  print("a est plus grand que b.")
```
````

### Exercice {num}`exo-py1`

```{exec} python
:editor: 49f2047d-751c-42d6-8832-40953fa8db92
# Complétez le programme
a = ...
if ... :
  print("a est plus grand de 5.")
elif ... :
  print("a est égal à 5.")
else:
  print("a est ...")
```

Tester la justesse de votre code avec différentes valeurs de a.

````{solution}
```{exec} python
:editor:
a = ...                                 # choisir la valeur de a
if a > 5 :
  print("a est plus grand de 5.")
elif a == 5 :                           # a == 5 pour la comparaison
  print("a est égal à 5.")
else:
  print("a est plus petit que 5.")
```
````

### Exercice {num}`exo-py1`

```{code-block} python
:linenos:
x = 2
if x <= -1 :
  print(2 * x + 1)
elif x <=3 :
  print(-x + 2)
else :
  print(2 * x - 5)
```

<script>
tdoc.question("Que va afficher ce programme?", {
  '0': true, '-x+2': "Il faut remplacer x par sa valeur.",
});
</script>

### Exercice {num}`exo-py1`

Écrivez un programme qui demande son âge à l'utilisateur et affiche s'il est
majeur ou s'il est mineur.

```{exec} python
:editor: c590c718-c33d-43da-a078-f7eb37502f9c
age = int(await input_line("Quel est ton âge?"))

# Complétez le programme ici
```

````{solution}
```{exec} python
age = int(await input_line("Quel est ton âge? "))

if age < 18:
  print("Tu es mineur.")
else:
  print("Tu es majeur.")
```
````

### Exercice {num}`exo-py1`

Que vont afficher les programmes suivants?

1.  ```{exec} python
    :when: never
    a = 2
    if a != 2:
      print("Rouge")
    elif a < 2:
      print("Bleu")
    else:
      print("Jaune")
    ```

    ````{solution}
    ```{exec} python
    a = 2
    if a != 2:
      print("Rouge")
    elif a < 2:
      print("Bleu")
    else:
      print("Jaune")
    ```
    ````

  2.  ```{exec} python
      :when: never
      y = 2
      if y <= -1:
        print(3 * y + 5)
      elif y <= 3:
        print(y + 4)
      else:
        print(y * y - 1)
      ```

      ````{solution}
      ```{exec} python
      y = 2
      if y <= -1:
        print(3 * y + 5)
      elif y < 2:
        print(y + 4)
      else:
        print(y * y - 1)
      ```
      ````

### Exercice {num}`exo-py1`

Le programme suivant est censé affiché le tarif appliqué en fonction de l'âge de
l'utilisateur. Mais il contient une erreur par ligne, trouvez-les et corrigez-les.

```{exec} python
:editor: 55bcea11-979f-43f8-8d1c-46f102e56b2b
age = await input_line("Quel âge as-tu? ")
if age > 18:
print("Tu payes le tarif enfant.")
elif age < 65
  print("Tu payes le tarif adulte.")
else age >= 65:
  print ("Tu payes le tarif retraité.")
```

````{solution}
```{exec} python
age = int(await input_line("Quel âge as-tu? "))
if age < 18:
  print("Tu payes le tarif enfant.")
elif age < 65:
  print("Tu payes le tarif adulte.")
else:
  print("Tu payes le tarif retraité.")
```
````

### Exercice {num}`exo-py1`

Écrivez un algorithme qui:
- demande un nombre à l'utilisateur,
- soustrait 5,5 à ce nombre,
- si le résultat est négatif, lui ajoute 10,
- affiche le résultat obtenu.

```{exec} python
:editor: d17fb574-66ce-4774-83fa-279a38ff862d
# Écrivez le programme
```

````{solution}
```{exec} python
nombre = float(await input_line("Choisissez un nombre"))
nombre = nombre - 5.5
if nombre < 0:
  nombre = nombre + 10
print(nombre)
```
````

### Exercice {num}`exo-py1`

Voici trois programmes:

1. Quelles sont les différences?
2. Que vont-ils afficher?
3. Faites un ordinogramme pour chacun.

<table style="width: 100%"><tr style="text-align: center">
  <th>Programme 1</th><th>Programme 2</th><th>Programme 3</th>
</tr><tr style="vertical-align: top"><td>

```{exec} python
:linenos:
x = -1
if x < 0:
  x = x + 5
elif x < 5:
  x = x * 3
elif x < 10:
  x = x - 6
else:
  x = 1000
print(x)
```

</td><td style="padding-left: 1rem">

```{exec} python
:linenos:
x = -1
if x < 0:
  x = x + 5
if x < 5:
  x = x * 3
if x < 10:
  x = x - 6
else:
  x = 1000
print(x)
```

</td><td style="padding-left: 1rem">

```{exec} python
:linenos:
x = -1
if x < 0:
  x = x + 5
  if x < 5:
    x = x * 3
    if x < 10:
      x = x - 6
else:
  x = 1000
print(x)
```

</td></tr></table>

### Exercice {num}`exo-py1`

Le programme suivant contient une erreur de logique. Testez le programme avec
différentes valeurs pour trouver et corriger l'erreur.

```{exec} python
:editor: 8f95d8ea-d2c0-4d56-a399-a58c54e99e6c
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

Il faut donc tester les conditions par ordre croissant: enfant, adulte, retraité
ou par ordre décroissant: retraité, adulte, enfant.
```

### Exercice {num}`exo-py1`

Un zoo pratique les tarifs suivants:

- Les enfants jusqu'à 16 ans révolus payent 15 francs.
- Les jeunes entre 16 et 20 ans payent 22 francs.
- Les adultes à partir de 21 ans payent 28 francs.

Écrivez un programme qui demande l'âge de l'utilisateur et affiche le prix à
payer.

```{exec} python
:editor: a7451ba3-2bd7-46f5-a2c6-1ab83c16c970
# Écrivez le programme
```

````{solution}
```{exec} python
age = int(await input_line("Quel est ton âge?"))
if age < 16:
  prix = 15
elif age <= 20:
  prix = 22
else :
  prix = 28
print ("Pour une personne de", age, "ans, le prix à payer est de", prix, "francs.")
```
````

## Opérateurs logiques

Les opérateurs logiques permettent de combiner plusieurs conditions simples

| Opérateur | Description          |
| :-------: | :------------------: |
| and       | retourne True si les deux conditions sont vraies |
| or        | retourne True si une des conditions est vraie    |
| not       | inverse le résultat, renvoie True si le résultat est faux et vice-versa |

### Exemple {num}`ex-py1`

(5 < 3) and (2 < 6) retourne `False`, car 5 < 3 retourne `False`.

(5 < 3) or (2 < 6) retourne `True`, car 2 < 6 retourne `True`.

(2 < 3) and (2 < 6) retourne `True`, car 2 < 3 retourne `True` et 2 < 6 retourne
 `True`.

(2 > 3) or (2 > 6) retourne `False`, car 2 > 3 retourne `False` et 2 > 6 retourne
 `False`.

 not(4 == 4) retourne `False`, car 4 == 4 retourne `True`.

 not(3 == 4) retourne `True`, car 3 == 4 retourne `False`.

### Exercice {num}`exo-py1`

Une salle de trampoline pratique les tarifs suivants pour deux personnes:

- Si les deux personnes sont mineures, elles payent chacune 7 francs.
- Si une seule est mineure, elles payent un tarif de groupe de 18 francs.
- Si les deux personnes sont majeures, elles payent au total 25 francs.

Écrivez un programme qui demande l'âge des deux personnes et affiche le prix à
payer.

```{exec} python
:editor: b7334fbc-4c1d-42fe-bed2-d15582abd972
age_1 = int(await input_line("Quel est l'âge de la première personne? "))
age_2 = int(await input_line("Quel est l'âge de la deuxième personne? "))

# Complétez le programme ici
```

````{solution}
```{exec} python
age_1 = int(await input_line("Quel est l'âge de la première personne? "))
age_2 = int(await input_line("Quel est l'âge de la deuxième personne? "))

if age_1 < 18 and age_2 < 18:
  prix = 2 * 7
elif age_1 < 18 or age_2 < 18:
  prix = 18
else:
  prix = 25
print("Le prix total à payer est de", prix, "francs.")
```
````

### Exercice {num}`exo-py1`

Julien souhaite s'inscrire à des séances d'équitation. Le club propose deux type
de tarification:

- Tarif A: Avec un abonnement annuel de 185 francs, la séance coûte 11 francs.
- Tarif B: Sans abonnement, la séance coûte 17 francs.

Écrivez un programme qui demande à Julien le nombre de séance qu'il voudrait
suivre pendant l'année et afficher le tarif le plus avantageux dans ce cas.

```{exec} python
:editor: f5b7f840-9b9e-4f66-9502-36f2f995abcb
nb_seances = int(await input_line("Nombre de séances: "))

# Complétez le programme
prixA = ...
prixB =  ...

```

````{solution}
```{exec} python
nb_seances = int(await input_line("Nombre de séances: "))

prix_A = 11 * nb_seances + 185
prix_B = 17 * nb_seances
if prix_A < prix_B:
  print("Le tarif A est le plus avantageux.")
elif prix_B < prix_A:
  print("Le tarif B est le plus avantageux.")
else:
  print("Les deux tarifs sont équivalents.")
```
````

### Exercice {num}`exo-py1`

Écrivez un programme qui demande trois nombres à l'utilisateur et affiche le
maximum (le plus grand).

```{exec} python
:editor: c3d6fb9b-eb5f-4e83-b662-606ac68282cf
nombre_1 = int(await input_line("Choisir un premier nombre: "))
nombre_2 = int(await input_line("Choisir un deuxième nombre: "))
nombre_3 = int(await input_line("Choisir un troisième nombre: "))

# Complétez le programme ici
```

````{solution}
```{exec} python
nombre_1 = int(await input_line("Choisir un premier nombre: "))
nombre_2 = int(await input_line("Choisir un deuxième nombre: "))
nombre_3 = int(await input_line("Choisir un troisième nombre: "))
max = nombre_1
if nombre_2 > max :
  max = nombre_2
if nombre_3 > max :
  max = nombre_3
print("Le plus grand nombre est", max)

```
````

### Exercice {num}`exo-py1`

Écrivez un programme qui demande un nombre à l'utilisateur et affiche s'il est
pair ou impair.

````{tip}
:class: dropdown
Utilisez le modulo (reste de la division entière) pour déterminer si un nombre
est divisible par un autre nombre.

```{exec} python
:editor:
print(14 % 5)          # Tester avec d'autres valeurs
```
````

```{exec} python
:editor: 085b1907-ca58-4a00-aab4-bcde5e4092cd
# Écrivez le programme ici
```

````{solution}
```{exec} python
nombre = int(await input_line("Choisir un nombre: "))
if nombre % 2 == 0:
  print(nombre, "est pair.")
else:
  print(nombre, "est impair.")
```
````

### Exercice {num}`exo-py1`

Écrivez un programme qui demande un nombre à l'utilisateur et affiche s'il est
divisible par 3 et 13.

```{exec} python
:editor: 1f78a8da-5f0e-452d-b427-59943fea89f2
# Écrivez le programme ici
```

````{solution}
```{exec} python
nombre = int(await input_line("Choisir un nombre: "))
if nombre % 3 == 0 and nombre % 13 == 0:
  print(nombre, "est divisible par 3 et 13.")
elif nombre % 3 == 0:
  print(nombre, "est divisible par 3.")
elif nombre % 13 == 0:
  print(nombre, "est divisible par 13.")
else:
  print(nombre, "n'est divisible ni par 3, ni par 13.")
```
````
