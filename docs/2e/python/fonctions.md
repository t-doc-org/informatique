% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
solutions: dynamic
```

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

Fonction qui affiche un conseil météo:

```{exec} python
:editor:
# définition des fonctions
def conseil_meteo():
  print("Mets tes lunettes de soleil et profite!")

# programme principal
print("=== Conseil météo ===")
# appel de la fonction
conseil_meteo()
```

Cette fonction affiche toujours le même conseil météo ce qui n'est pas très
intéressant, le conseil devrait s'adapter au temps qu'il fait.

## Fonctions avec paramètres

Un **paramètre d'une fonction** est une variable définie dans la fonction qui
recevra une valeur lors de chaque appel de la fonction. Ainsi le comportement
d'une fonction varie suivant les valeurs de ses paramètres.

### Exemple {num2}`exemple`

Fonction qui affiche un conseil météo en fonction de celle-ci

```{exec} python
:editor:
# définition des fonctions
def conseil_meteo(meteo):
  if meteo == "soleil":
    print("Mets tes lunettes de soleil et profite!")
  elif meteo == "pluie":
    print("Prends ton parapluie ou tu seras trempé(e)!")
  elif meteo == "neige":
    print("Enfile tes gants et va faire un bonhomme de neige!")
  else:
    print("Hmm... je ne sais pas quoi te conseiller pour cette météo!")


# programme principal
print("=== Conseil météo ===")

# demande la météo du jour à l'utilisateur
meteo_du_jour = input("Quel temps fait-il aujourd'hui? (soleil/pluie/neige/autre): ")

# appel de la fonction en fonction de la réponse de l'utilisateur
conseil_meteo(meteo_du_jour)
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


### Exemple {num2}`exemple`

```{exec} python
:editor:
# definition des fonctions
def prix_apres_reduction(prix, reduction_pourcent):
  reduction = prix * reduction_pourcent / 100
  prix_final = prix - reduction
  print(prix_final)

# programme principal

# demande à l'utilisateur le prix et le pourcentage de réduction
prix = float(input("Prix en CHF: "))
reduc = float(input("Réduction en %: "))

prix_apres_reduction(prix, reduc)
```

La fonction ainsi écrite affiche le prix après réduction, mais il n'est pas
possible d'utiliser la valeur.

## Fonctions avec valeur de retour

La commande `return` permet de retourner le résultat d'une fonction et ainsi de
pouvoir le réutiliser dans la suite du programme. Pour cela, il est nécessaire
de sauvegarder la valeur retournée dans une variable.

### Exemple {num2}`exemple:py2-delta2`

```{exec} python
:editor:
# definition des fonctions
def prix_apres_reduction(prix, reduction_pourcent):
  reduction = prix * reduction_pourcent / 100
  prix_final = prix - reduction
  return prix_final

# programme principal
print("=== Sortie shopping ===")

# demande à l'utilisateur le prix et le pourcentage de réduction
prix_pantalon = float(input("Prix du pantalon en CHF: "))
reduc_pantalon = float(input("Réduction du pantalon en %: "))
prix_veste = float(input("Prix de la veste en CHF: "))
reduc_veste = float(input("Réduction de la veste en %: "))

# sauvegarde les valeurs de retour dans des variables
prix_reduit_pantalon = prix_apres_reduction(prix_pantalon, reduc_pantalon)
prix_reduit_veste = prix_apres_reduction(prix_veste, reduc_veste)
print("Prix total des achats:", prix_reduit_pantalon + prix_reduit_veste, "CHF.")
```

### Exercice {num2}`exercice`

Déterminez ce que font les programmes suivants et corrigez les erreurs.

1.  ```{exec} python
    :editor:
    def convertit_min_sec(min):
      return min * 60

    convertit_min_sec(145)
    print("145 minutes donnent", nb_secondes, "secondes.")
    ```

2.  ```{exec} python
    :editor:
    def convertit_sec_min(sec):
      min = sec / 60

    nb_minutes = convertit_sec_min(38700)
    print("38700 secondes donnent", nb_minutes, "minutes.")
    ```

3.  ```{exec} python
    :editor:
    def calcule_double_moins_trois(x):
      x = 2 * x
      return x
      x = x - 3

    print(calcule_double_moins_trois(4))
    ```

````{solution}

 1. Il faut sauvegarder la valeur de retour dans la variable nb_secondes
    ```{exec} python
    :linenos:
    def convertit_min_sec(min):
      return min * 60

    nb_secondes = convertit_min_sec(145)
    print("145 minutes donnent", nb_secondes, "secondes.")
    ```

2.  Il manque le `return` dans la fonction. Dans ce cas, la valeur retournée est
    `None`.
    ```{exec} python
    :linenos:
    def convertit_sec_min(sec):
      return sec / 60

    nb_minutes = convertit_sec_min(38700)
    print("38700 secondes donnent", nb_minutes, "minutes.")
    ```

3.  Le `return` n'est pas à la bonne place.
    ```{exec} python
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

### Exercice {num2}`exercice`

Sans l'exécuter, déterminez ce que va afficher le programme suivant. Ensuite,
exécutez-le pour vérifier votre réponse.

```{exec} python
:editor:
def mystery_1(z):
  z *= 2
  return z

def mystery_2(x):
  x -= 7
  if x < 0:
    return x
  else:
    return x % 2

y = 5
print(mystery_1(y))
print(mystery_2(y))
print(mystery_2(2 * y))
print(y // 2)
```

### Exercice {num2}`exercice`

Complétez le programme ci-dessous. Nous avons défini une fonction `majeur` pour
tester si une personne est majeure ou pas.

```{exec} python
:editor: d62933bb-5602-48e8-b92e-302c5857b135
def majeur(age):
  if ... :
    return True
  else:
    return False

# Demandez son âge à l'utilisateur
age = ...

if majeur(age):
  print("Tu as le droit de vote")
else:
  print("Tu pourras voter dans", ..., "ans.")
```

````{solution}
```{exec} python
def majeur(age):
  if age >= 18 :
    return True
  else:
    return False

# Demandez son âge à l'utiliateur
age = int(input("Quel âge as-tu?"))

if majeur(age):
  print("Tu as le droit de vote")
else:
  print("Tu pourras voter dans", 18 - age, "ans.")
```
````

### Exercice {num2}`exercice`

1. Écrivez une fonction qui convertit des bits en octets.
2. Écrivez une fonction qui convertit des octets en bits.
3. Convertissez 3664000 bits en octets.
4. Convertissez 512 octets en bits.

```{tip}
Un octet contient 8 bits.
```

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

# ne pas modifier le code ci-dessous
prix = float(input("Quel est le prix de l'article? "))
code_reduc = input("Quel est le code de réduction? ")

reduction = calcule_reduction(code_reduc)
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
code_reduc = input("Quel est le code de réduction? ")

reduction = calcule_reduction(code_reduc)
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

# ne pas modifier le code ci-dessous
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


