% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Programmation - Entrainement

```{metadata}
orphan:
```

Site d'entrainement d'écriture de programme en Python.

## Exercice 1

Écrivez un programme qui correspond à l'algorithme suivant, en définissant une
variable pour chaque donnée:

- La base d’un triangle vaut 7.6.
- La hauteur de ce triangle vaut 4.55.
- Calculez et affichez l’aire du triangle

```{exec} python
:editor: 4ecb5ecf-33a6-4d4d-b800-445e049bc6fd
# Écrivez le code ici...
```

````{solution}
```{exec} python
:linenos:
# Définition des données
base = 7.6
hauteur = 4.55

# Calcul de l'aire du triangle
aire = (base * hauteur) / 2

# Affichage du résultat
print("L'aire du triangle est :", aire)
```
````

## Exercice 2

Écrivez un programme qui correspond à l'algorithme suivant, en
définissant une variable pour chaque donnée:

- Le prix d’un article est de 654 CHF.
- La réduction est de 79 CHF (montant fixe).
- Calculez et affichez le prix après réduction.

```{exec} python
:editor: 436b7b77-c7d6-4d7a-84a3-726a80257f26
# Écrivez le code ici...
```

````{solution}
```{exec} python
:linenos:
# Définition des données
prix_initial = 654
reduction = 79

# Calcul du prix après réduction
prix_final = prix_initial - reduction

# Affichage du résultat
print("Le prix après réduction est :", prix_final)
```
````

## Exercice 3

Écrivez un programme qui correspond à l'algorithme suivant:

Demandez à l'utilisateur sa température corporelle. Si la température est
supérieure ou égale à 38, affichez qu'il a de la fièvre. Sinon, affichez que sa
température est normale.

```{exec} python
:editor: 535ee123-269c-4686-a94f-75c017c08342
# Écrivez le code ici...
```

````{solution}
```{exec} python
:linenos:
# Demander la température à l'utilisateur
temperature = float(await input_line("Entrez votre température corporelle : "))

# Vérifier si l'utilisateur a de la fièvre
if temperature >= 38:
    print("Vous avez de la fièvre.")
else:
    print("Votre température est normale.")
```
````

## Exercice 4

Écrivez un programme qui correspond à l'algorithme suivant:

Demandez à l'utilisateur d'entrer un nombre. Si ce nombre est égal à 0, affichez
"Le nombre est nul". Sinon, affichez "Le nombre est non nul".

```{exec} python
:editor: 4aac6856-855e-4072-a0d2-14d11d5d174a
# Écrivez le code ici...
```

````{solution}
```{exec} python
:linenos:
# Demander un nombre à l'utilisateur
nombre = float(await input_line("Entrez un nombre : "))

# Vérifier si le nombre est nul ou non
if nombre == 0:
    print("Le nombre est nul.")
else:
    print("Le nombre est non nul.")
```
````

## Exercice 5

Écrivez un programme qui correspond à l'algorithme suivant:

Demandez la vitesse (en km/h) à l'utilisateur. Si la vitesse est inférieure ou
égale à 50, affichez "Vous êtes en dessous de la limite de vitesse". Si la
vitesse est strictement supérieure à 50 et inférieure ou égale à 80, affichez
"Vous roulez à une vitesse raisonnable". Sinon, affichez "Vous dépassez la
limite de vitesse".

```{exec} python
:editor: 497db88e-edeb-400b-a0b7-3121d2e3ba66
# Écrivez le code ici...
```

````{solution}
```{exec} python
:linenos:
# Demander la vitesse à l'utilisateur
vitesse = float(await input_line("Entrez votre vitesse en km/h : "))

# Vérifier les différentes limites de vitesse
if vitesse <= 50:
    print("Vous êtes en dessous de la limite de vitesse.")
elif vitesse <= 80:
    print("Vous roulez à une vitesse raisonnable.")
else:
    print("Vous dépassez la limite de vitesse.")
```
````

## Exercice 6

Écrivez un programme qui correspond à l'algorithme suivant:

Demandez la température à l'utilisateur. Si la température est inférieure à 0,
affichez "Il fait très froid". Si la température est comprise entre 0 et 20
(inclus), affichez "Il fait frais". Sinon, affichez "Il fait chaud".

```{exec} python
:editor: 47ec7cb4-2863-4f03-a73d-882792a5d77d
# Écrivez le code ici...
```

````{solution}
```{exec} python
:linenos:
# Demander la température à l'utilisateur
temperature = float(await input_line("Entrez la température en degrés Celsius : "))

# Vérifier les différentes conditions de température
if temperature < 0:
    print("Il fait très froid.")
elif temperature <= 20:
    print("Il fait frais.")
else:
    print("Il fait chaud.")
```
````

## Exercice 7

Écrivez un programme qui correspond à l'algorithme suivant :

- Initialisez une variable i à 1.
- Tant que i est inférieur ou égal à 10, affichez la valeur de i.
- Ajoutez 2 à i à chaque itération.
- Affichez "Terminé" après la boucle.

```{exec} python
:editor: 15410054-aac5-472f-bf50-4a180f514719
# Écrivez le code ici...
```

````{solution}
```{exec} python
:linenos:
# Initialisation de la variable i
i = 1

# Tant que i est inférieur ou égal à 10
while i <= 10:
    # Affichage de la valeur actuelle de i
    print(i)

    # Ajout de 2 à i
    i += 2

# Affichage de "Terminé" après la boucle
print("Terminé")
```
````

## Exercice 8

Écrivez un programme qui correspond à l'algorithme suivant:

Une boutique a initialement 200 produits en stock. Chaque jour, 40 produits sont
vendus.
- Affichez le nombre de produits restants chaque jour.
- Affichez "Stock épuisé!" lorsque tous les produits ont été vendus.


```{exec} python
:editor: 2e37947f-c6f8-456e-915e-f8c30b3678c2
# Écrivez le code ici...
```

````{solution}
```{exec} python
:linenos:
# Initialisation du nombre de produits en stock
produits_en_stock = 200

# Tant qu'il y a des produits en stock
while produits_en_stock > 0:
    # Réduire le stock de 40 produits chaque jour
    produits_en_stock -= 40

    # Afficher le nombre de produits restants
    print(produits_en_stock)

# Afficher que le stock est épuisé une fois que la boucle est terminée
print("Stock épuisé!")
```
````

## Exercice 9

Écrivez un programme qui affiche les nombres de 5 à 43 (inclus).


```{exec} python
:editor: 9cd50b1e-fdb2-417d-b3c0-eac24389a7ba
# Écrivez le code ici...
```

````{solution}
Il y a deux solutions possibles:

```{exec} python
:linenos:
# Afficher les nombres de 5 à 43 (inclus)
for i in range(39):
    print(i + 5)
```

```{exec} python
:linenos:
# Afficher les nombres de 5 à 43 (inclus)
for i in range(5, 44):
    print(i)
```
````

## Exercice 10

Écrivez un programme qui affiche les nombres pairs de 0 à 30 (inclus).


```{exec} python
:editor: b40e8f5c-8dc4-4945-9dcc-86aa6cf6ec89
# Écrivez le code ici...
```

````{solution}
Il y a deux solutions possibles:

```{exec} python
:linenos:
# Il y a 15 nombres pairs
for i in range(15):
    print((i+1) * 2)
```

```{exec} python
:linenos:
# Il y a 15 nombres pairs
for i in range(1, 16):
    print(i * 2)
```
````
