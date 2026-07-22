% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Fonctions - Exercices supplémentaires

## Exercice {nump}`exercice`

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

## Exercice {nump}`exercice`

Pour les prochaines vacances, vous décidez de partir en vacances au Japon. Vous
avez de l'argent sur un compte épargne et de l'argent que vous avez gagné en
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

## Exercice {nump}`exercice`

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

## Exercice {nump}`exercice`

Pour calculer le prix de l'amende à payer en cas de dépassement de vitesse,
consultez le document suivant: [Liste sanctions](sanctions-vitesse.pdf)


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
    print("La sanction sera plus qu'une amende.")
    return -100

print(amende(120,140))
print(amende(120,145))
print(amende(120,120))
print(amende(120, 180))
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

## Exercice {nump}`exercice`

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
  if nb_diviseurs == 2:
    return True
  else:
    return False

n = int(input("Choisir un nombre entier strictement positif:"))
while n <= 0:
  n = int(input("Le nombre doit être strictement positif!"
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

## Exercice {nump}`exercice`

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
