% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Fonctions

En programmation, une **fonction** est un bloc de code (suite d'instructions)
permettant de réaliser une tâche donnée et auquel nous donnons un nom. Cela
permet de découper un programme en plusieurs petites tâches plus faciles à
résoudre. Ainsi le code est plus lisible et plus facile à comprendre. Pour cela,
il est essentiel de choisir un nom de fonction qui explique ce qu'elle fait.

```{tip}
Une fonction doit toujours être définie avant d'être appelée, c'est pourquoi il
est préférable de placer toutes les définitions de fonctions au début du
programme (après les imports et les définitions de variables globales).
```

## Exemple {num2}`exemple`

Fonction qui affiche la table de multiplication de 5:

```{exec} python
:editor: 476b2fb3-f383-4b92-8545-785da279b0fb
# définition de la fonction
def table_multiplication_5():
  for i in range(1, 11):              # i prend les valeurs de 1 à 10
    print(5, "*", i, "=", 5 * i)

# appel de la fonction
table_multiplication_5()
```

Le problème de cette fonction est que pour afficher la table de  multiplication
de 6, il est nécessaire d'écrire une nouvelle fonction. Cela peut être amélioré
en utilisant des paramètres.

## Fonctions avec paramètres

Un **paramètre d'une fonction** est une variable définie dans la fonction qui
recevra une valeur lors de chaque appel de la fonction. Ainsi le comportement
d'une fonction varie suivant les valeurs de ses paramètres.

### Exemple {num2}`exemple`

Fonction qui affiche n'importe quelle table de multiplication:

```{exec} python
:editor: 66a281f9-5417-419d-978d-2602139544ac
def table_multiplication(n):
  for i in range(1, 11):
    print(n, "*", i, "=", n * i)

nombre = 6                      # changer la valeur du nombre ici
table_multiplication(nombre)
```

### Exemple {num2}`exemple`

```{exec} python
:editor: b280f69c-2547-4680-98c8-2cce587c9c74
# Calcule et affiche le discriminant dans la résolution d'équation du 2e degré
def discriminant(a, b, c):
  delta = b ** 2 - 4 * a * c
  print("Le discriminant est:", delta)

# Demande à l'utilisateur les valeurs des coefficients a, b et c
a = float(input("Coefficient de x^2: "))
b = float(input("Coefficient de x: "))
c = float(input("Coefficient sans partie littérale: "))

discriminant(a, b, c)
```

La fonction ainsi écrite affiche le discriminant, mais il n'est pas possible
d'utiliser la valeur, ce qui ne permet pas de calculer les solutions si elle(s)
existe(nt).

## Fonctions avec valeur de retour

La commande `return` permet de renvoyer le résultat d'une fonction et ainsi
pouvoir le réutiliser dans la suite du programme. Pour cela, il est nécessaire
de sauvegarder la valeur retournée dans une variable.

### Exemple {num2}`exemple:py2-delta2`

```{exec} python
:editor: dfb94893-8e1b-4a02-9eca-177f82e8be11
# Calcule et affiche le discriminant dans la résolution d'équation du 2e degré
def discriminant(a, b, c):
  delta = b ** 2 - 4 * a * c
  return delta

# Demande à l'utilisateur les valeurs des coefficients a, b et c
a = float(input("Coefficient de x^2: "))
b = float(input("Coefficient de x: "))
c = float(input("Coefficient sans partie littérale: "))

delta = discriminant(a, b, c)
print(delta)
```

### Exercice {num2}`exercice`

Déterminez ce que font les programmes suivants et corrigez les erreurs.

1.  ```{exec} python
    :editor: c0a8920d-43e3-4291-a431-6c1a7270a010
    def convertit_min_sec(min):
      return min * 60

    convertit_min_sec(145)
    print("145 minutes donnent", nb_sec, "secondes.")
    ```

2.  ```{exec} python
    :editor: 18de8ef0-7a6e-4b06-8302-ec701a785c9f
    def convertit_sec_min(sec):
      min = sec / 60

    nb_minutes = convertit_sec_min(38700)
    print("38700 secondes donnent", nb_minutes, "minutes.")
    ```

3.  ```{exec} python
    :editor: f9f4ceaf-ef89-4c7d-88e5-d1b34f3f0feb
    def calcule_double_moins_trois(x):
      x = 2 * x
      return x
      x = x - 3

    print(calcule_double_moins_trois(4))
    ```

````{solution}

 1. ```{exec} python
    :linenos:
    def convertit_min_sec(min):
      return min * 60

    nb_secondes = convertit_min_sec(145)
    print("145 minutes donnent", nb_secondes, "secondes.")
    ```

2.  ```{exec} python
    :linenos:
    def convertit_sec_min(sec):
      return sec / 60

    nb_minutes = convertit_sec_min(38700)
    print("38700 secondes donnent", nb_minutes, "minutes.")
    ```

3.  ```{exec} python
    :linenos:
    def calcule_double_moins_trois(x):
      x = 2 * x
      x = x - 3
      return x

    print(calcule_double_moins_trois(4))
    ```
````

````{important}
`return` interrompt la fonction. Tout ce qui se trouve dans la fonction, mais
après le `return` sera ignoré.

```{exec} python
:linenos:
def double(x):
  return 2*x
  print("Ce texte ne s'affichera pas.")

print(double(5))
print("Fin du programme")
```
````

### Exercice {num2}`exercice:py2-num1`

Modifiez le code de l'{numref}`exemple %s<exemple:py2-delta2>` pour que le
programme vérifie que le coefficient $a$ n'est pas nul. (Dans ce cas, ce n'est
pas une équation du deuxième degré et la résolution est différente.)

```{exec} python
:editor: d0ba1a78-33a3-41b2-8405-23d7b418e656
# Calcule et affiche le discriminant dans la résolution d'équation du 2e degré
def discriminant(a, b, c):
  delta = b ** 2 - 4 * a * c
  return delta

# Demande à l'utilisateur les valeurs des coefficients a, b et c
a = float(input("Coefficient de x^2: "))
b = float(input("Coefficient de x: "))
c = float(input("Coefficient sans partie littérale: "))

# Modifier le programme à partir d'ici

delta = discriminant(a, b, c)
print(delta)
```

````{solution}
```{exec} python
:linenos:
# Calcule et affiche le discriminant dans la résolution d'équation du 2e degré
def discriminant(a, b, c):
  delta = b ** 2 - 4 * a * c
  return delta

# Demande à l'utilisateur les valeurs des coefficients a, b et c
a = float(input("Coefficient de x^2: "))
b = float(input("Coefficient de x: "))
c = float(input("Coefficient sans partie littérale: "))

if a == 0:
  print("Ce n'est pas une équation du deuxième degré.")
else:
  delta = discriminant(a, b, c)
  print(delta)
```
````

### Exercice {num2}`exercice:py2-num2`

Modifiez le code de l'{numref}`exercice %1s<exercice:py2-num1>`, pour afficher
le nombre de solutions de l'équation.\
Rappel:
- si $\Delta < 0$, il n'y a pas de solution,
- si $\Delta = 0$, il y a une solution,
- si $\Delta > 0$, il y a 2 solutions.

```{exec} python
:editor: 2e646990-092f-4a85-b812-9490a09bf202
# Calcule le discriminant dans la résolution d'équation du 2e degré
def discriminant(a, b, c):
  return b ** 2 - 4 * a * c

# Demande à l'utilisateur les valeurs des coefficients a, b et c
a = float(input("Coefficient de x^2: "))
b = float(input("Coefficient de x: "))
c = float(input("Coefficient sans partie littérale: "))

# Complétez le programme à partir de là
```

````{solution}
```{exec} python
:editor: e9afc7bb-1e35-422a-a829-c457ff480002
# Calcule le discriminant dans la résolution d'équation du 2e degré
def discriminant(a, b, c):
  return b ** 2 - 4 * a * c

# Demande à l'utilisateur les valeurs des coefficients a, b et c
a = float(input("Coefficient de x^2: "))
b = float(input("Coefficient de x: "))
c = float(input("Coefficient sans partie littérale: "))

if a == 0:
  print("Ce n'est pas une équation du deuxième degré.")
else:
  delta = discriminant(a, b, c)
  if delta > 0:
    print("Cette équation a deux solutions.")
  elif delta == 0:
    print("Cette équation a une solution.")
  else:
    print("Cette équation n'a pas de solution.")
```
````

### Exercice {num2}`exercice:py2-num3`

Complétez le code de l'{numref}`exercice %s<exercice:py2-num2>`, pour calculer
les solutions de l'équation.

````{tip}
Pour calculer la racine carrée d'un nombre, il faut utiliser la fonction
`sqrt()` qui se trouve dans le module math. Il est donc nécessaire d'importer ce
module:

```{exec} python
:linenos:
from math import sqrt

print(sqrt(54))
```
````

```{exec} python
:editor: 77c5e3c2-e6de-492e-85d5-db3f440d5684
# Calcule le discriminant dans la résolution d'équation du 2e degré
def discriminant(a, b, c):
  return b ** 2 - 4 * a * c

# Demande à l'utilisateur les valeurs des coefficients a, b et c
a = float(input("Coefficient de x^2: "))
b = float(input("Coefficient de x: "))
c = float(input("Coefficient sans partie littérale: "))

# Complétez le programme à partir de là
```

````{solution}
```{exec} python
:linenos:
from math import sqrt

# Calcule le discriminant dans la résolution d'équation du 2e degré
def discriminant(a, b, c):
  return b ** 2 - 4 * a * c

# Demande à l'utilisateur les valeurs des coefficients a, b et c
a = float(input("Coefficient de x^2: "))
b = float(input("Coefficient de x: "))
c = float(input("Coefficient sans partie littérale: "))

if a == 0:
  print("Ce n'est pas une équation du deuxième degré.")
else:
  delta = discriminant(a, b, c)
  if delta > 0:
    x_1 = (-b + sqrt(delta)) / (2 * a)
    x_2 = (-b - sqrt(delta)) / (2 * a)
    print("Cette équation a deux solutions: x_1 =", x_1, "et x_2 =", x_2)
  elif delta == 0:
    x = -b / (2 * a)
    print("Cette équation a une solution: x =", x)
  else:
    print("Cette équation n'a pas de solution.")
```
````

### Exercice {num2}`exercice`

Complétez le programme de l'{numref}`exercice %s<exercice:py2-num3>`, pour
calculer aussi la solution si $a = 0$, c'est-à-dire que l'équation donnée est
une équation du premier degré.

```{exec} python
:editor: a0139bba-537f-419e-8187-76d78355d944
# Calcule le discriminant dans la résolution d'équation du 2e degré
def discriminant(a, b, c):
  return b ** 2 - 4 * a * c

# Demande à l'utilisateur les valeurs des coefficients a, b et c
a = float(input("Coefficient de x^2: "))
b = float(input("Coefficient de x: "))
c = float(input("Coefficient sans partie littérale: "))

# Complétez le programme à partir de là
```

````{solution}
```{exec} python
:linenos:
from math import sqrt

# Calcule le discriminant dans la résolution d'équation du 2e degré
def discriminant(a, b, c):
  return b ** 2 - 4 * a * c

# Demande à l'utilisateur les valeurs des coefficients a, b et c
a = float(input("Coefficient de x^2: "))
b = float(input("Coefficient de x: "))
c = float(input("Coefficient sans partie littérale: "))

if a == 0:
  x = -c / b
  print("Cette équation a une solution: x =", x)
else:
  delta = discriminant(a, b, c)
  if delta > 0:
    x_1 = (-b + sqrt(delta)) / (2 * a)
    x_2 = (-b - sqrt(delta)) / (2 * a)
    print("Cette équation a deux solutions: x_1 =", x_1, "et x_2 =", x_2)
  elif delta == 0:
    x = -b / (2 * a)
    print("Cette équation a une solution: x =", x)
  else:
    print("Cette équation n'a pas de solution.")
```
````

### Exercice {num2}`exercice`

1. Écrivez une fonction qui convertit des bits en octets.
2. Écrivez une fonction qui convertit des octets en bits.
3. Convertissez 3664000 bits en octets.
4. Convertissez 512 octets en bits.

```{exec} python
:editor: 6d5c5190-7949-4078-b22d-e2c84a39f4d4
# Écrire le programme ici
```

````{solution}
```{exec} python
:linenos:
# Convertit des bits en octets
def conversion_bits_octets(a):
  return a / 8

# Convertit des bits en octets
def conversion_octets_bits(a):
  return a * 8

nb_octets = conversion_bits_octets(3664000)
print("La conversion de 3664000 bits en octets donne", nb_octets)

nb_bits = conversion_octets_bits(512)
print("La conversion de 512 octets en bits donne", nb_bits)

```
````

### Exercice {num2}`exercice`

Pour calculer l'aire totale de la figure ci-dessous:

1. Écrivez une fonction qui permet de calculer l'aire d'un rectangle en
connaissant la longueur et la largeur.
2. Calculez l'aire totale de la figure.

```{image} images/aire-rectangles.png
:alt: Aire totale
:width: 30%
:align: center
```

```{exec} python
:editor: 72650926-c1a9-4096-88b6-3e07b7cc9ccf
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
def calcule_aire_rectangle(longueur, largeur):
  return longueur * largeur

aire_rectangle_1 = calcule_aire_rectangle(7.5, 3.4)
aire_rectangle_2 = calcule_aire_rectangle(5.8, 3.4)
aire_totale = aire_rectangle_1 + aire_rectangle_2
print("Aire totale:", aire_totale)
```
````

### Exercice {num2}`exercice`

Pour les prochaines vacances, vous décidez de partir en vacances au Japon. Vous
avez de l'argent sur un compte épargne et de l'argent que vous avez gagner en
travaillant cet été.

Écrivez un programme qui permet de convertir en YEN les montants qui sont sur un
compte épargne et sur un compte courant afin de déterminer le montant que vous
aurez à disposition.\
Le taux est de 1 CHF = 174 YEN.

```{exec} python
:editor: 5f6f63a3-ab47-43c5-9774-f50cabd75e94
def convertit_chf_en_yen(montant_chf):
  # à compléter

compte_courant_chf = 1540
compte_epargne_chf = 2467

# Complétez le programme
budget_yen =
print("Tu auras", budget_yen, "YEN.")
```

````{solution}
```{exec} python
:linenos:
# Compléter la fonction
def convertit_chf_en_yen(montant_chf):
  taux_conversion = 174
  return montant_chf * taux_conversion


compte_courant_chf = 1540
compte_epargne_chf = 2467

budget_yen = convertit_chf_en_yen(1540) + convertit_chf_en_yen(2467)
print("Tu auras", budget_yen, "YEN.")
```
````

### Exercice {num2}`exercice`

Écrivez une fonction qui prend en paramètre un code de réduction et retourne le
pourcentage de rabais donné par ce code de réduction. Le code déjà donné utilise
cette fonction pour calculer le prix final d'un article après y avoir appliqué
la réduction. Les réductions sont les suivantes :
- 20% (0.2) pour le code SUN
- 35% (0.35) pour le code STX
- 50% (0.5) pour le code MAX
- 0% (0) pour les autres codes

```{exec} python
:editor: 4cb99c2b-2ac8-4cf6-9263-4a21bb0e8c8a
def calcule_reduction(code):
 # à compléter

prix = float(input("Quel est le prix de l'article? "))
code = input("Quel est le code de réduction? ")

reduction = calcule_reduction(code)
prix_final = prix * (1 - reduction)
print("Le prix final est de", prix_final, "CHF.")
```

````{solution}
```{exec} python
:linenos:
def calcule_reduction(code):
  if code == "SUN":
    return 0.2
  elif code == "STX":
    return 0.35
  elif code == "MAX":
    return 0.5
  else:
    return 0

prix = float(input("Quel est le prix de l'article? "))
code = input("Quel est le code de réduction? ")

reduction = calcule_reduction(code)
prix_final = prix * (1 - reduction)
print("Le prix final est de", prix_final, "CHF.")
```
````

### Exercice {num2}`exercice`

Pour calculer le prix de l'amende à payer en cas de dépassement de vitesse,
consulter le document suivant: [Liste sanctions](sanctions-vitesse.pdf)


Écrivez une fonction qui retourne le prix de l'amende à payer en fonction de la
vitesse autorisée et la vitesse mesurée par le radar. Traitez seulement le cas
où le dépassement de vitesse a lieu sur l'autoroute et n'excède pas 25 km/h.

```{exec} python
:editor: 263a83cb-f587-44f0-bf7d-e5784f778e3f
def amende(vit_autorisee, vit_mesuree):
  # à compléter

print(amende(120,140))
print(amende(120,145))
print(amende(120,120))
```

````{solution}
```{exec} python
:linenos:
def amende(vit_autorisee, vit_mesuree):
  depassement = vit_mesuree - vit_autorisee
  if depassement <= 0:
    return 0
  elif depassement <= 5:
    return 20
  elif depassement <= 10:
    return 60
  elif depassement <= 15:
    return 120
  elif depassement <= 20:
    return 180
  elif depassement <= 25:
    return 260
  else:
    return -100

print(amende(120,140))
print(amende(120,145))
print(amende(120,120))
```
````

### Exercice {num2}`exercice`

La suite de Syracuse est une suite d'entiers naturels définie de la manière
suivante:
- si le nombre est pair, diviser par 2,
- sinon multiplier par 3 et ajouter 1.

Cette suite à la particularité de toujours se terminer par 4, 2, 1.

Écrivez un programme qui demande à l'utilisateur de choisir un nombre et affiche
la suite de Syracus (jusqu'à ce que la suite arrive à 1).

```{exec} python
:editor: bce7f53a-426f-4c3f-b967-c2e41783d2ff
def syracuse(n):
  # à compléter

n = int(input("Choisir un nombre entier plus grand que 0."))

# Complétez le programme

```

````{solution}
```{exec} python
:linenos:
def syracuse(n):
  if n % 2 == 0:
    return n // 2
  else:
    return 3 * n + 1

n = int(input("Choisir un nombre entier plus grand que 0."))

while n != 1:
  n = syracuse(n)
  print(n)
```
````

````{tip}
Pour faciliter la compréhension de code, il est courant de créer des fonctions
qui testent une certaine condition. Par exemple, la fonction `est_pair(n)`
retourne `True` si la nombre est pair et `False` sinon.

```{exec} python
:linenos:
def est_pair(nombre):
  if nombre % 2 == 0:
    return True
  else:
    return False

print(est_pair(107))
```
````

### Exercice {num2}`exercice`

Écrivez un programme qui demande à l'utilisateur un nombre entier strictement
positif et affiche tous ses diviseurs. Ce programme doit:
1. contenir un procédé qui vérifie que la réponse de l'utilisateur est bien un
nombre strictement positif. Si ce n'est pas le cas, lui demander un autre
nombre.
2. contenir une fonction `est_diviseur()` qui teste si un nombre est diviseur
d'un autre nombre.
3. contenir une fonction `est_premier()` qui teste si un nombre est premier.

```{exec} python
:editor: 91faf472-2b3d-4729-bc95-ce1c8c0d00a7
def est_diviseur(nombre, diviseur):
  # à compléter

def est_premier(nb_diviseurs):
  # à compléter

n = int(input("Choisir un nombre entier strictement positif:"))

# Complétez le programme
```

````{solution}
```{exec} python
:linenos:
def est_diviseur(nombre, diviseur):
  if nombre % diviseur == 0:
    return True
  else:
    return False

def est_premier(nb_diviseurs):
  if n == 2:
    return True
  else:
    return False

n = int(input("Choisir un nombre entier strictement positif:"))
while n <= 0:
  n = int(input("Le nombre doit être stritement positif!"
        "Choisir un nombre entier strictement positif:"))

nb_diviseurs = 0

for i in range(1, n + 1):
  if est_diviseur(n, i):
    print(i, "est diviseur de", n)
    nb_diviseurs += 1

if est_premier(nb_diviseurs):
  print(n, "est un nombre premier.")
else:
  print(n, "n'est pas un nombre premier.")

```
````

```{important}
L'ordre des paramètres lors de l'appel de la fonction doit être le même que lors
de la définition de la fonction.
```

### Exercice {num2}`exercice`

Créez une fonction `compteur()`...
1.  qui compte de 0 à un nombre donné appelé `stop`:

    ```{exec} python
    :editor: b5114e99-47c4-40d8-93e4-7bac649c10f2
    def compteur(stop):
      # à compléter

    compteur(11)
    ```

    ````{solution}
    Version avec une boucle while
      ```{exec} python
      :linenos:
      def compteur(stop):
        i = 0
        while i <= stop:
          print(i)
          i += 1

      compteur(11)
      ```

     Version avec une boucle for
      ```{exec} python
      :linenos:
      def compteur(stop):
        for i in range(stop + 1):
          print(i)

      compteur(11)
      ```
    ````

2.  qui compte de `start` à `stop` avec `start` < `stop`:

    ```{exec} python
    :editor: 4b3ebd3f-e3a6-4041-a51a-3362a1b299c3
    def compteur(start, stop):
      # à compléter

    compteur(4, 11)
    ```

    ````{solution}
    Version avec une boucle while
      ```{exec} python
      :linenos:
      def compteur(start, stop):
        i = start
        while i <= stop:
          print(i)
          i += 1

      compteur(4, 11)
      ```

     Version avec une boucle for
      ```{exec} python
      :linenos:
      def compteur(start, stop):
        for i in range(start, stop + 1):
          print(i)

      compteur(4, 11)
      ```
    ````

3.  qui compte de `start` à `stop` avec un pas donné `step` (de 2 en 2 ou
    de 3 en 3):

    ```{exec} python
    :editor: fd8b8f40-1de2-41ca-8868-6a29af56c20d
    def compteur(start, stop, step):
      # à compléter

    compteur(4, 11, 3)
    ```

    ````{solution}
    Version avec une boucle while
      ```{exec} python
      :linenos:
      def compteur(start, stop, step):
        i = start
        while i <= stop:
          print(i)
          i += step

      compteur(4, 11, 3)
      ```

     Version avec une boucle for
      ```{exec} python
      :linenos:
      def compteur(start, stop, step):
        for i in range(start, stop + 1, step):
          print(i)

      compteur(4, 11, 3)
      ```
    ````
