% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
solutions: dynamic
```

# Listes - Élément appartenant à une liste

Il est possible de savoir si un élément appartient à une liste en utilisant
l'expression suivante `element in liste` qui revoie `True` si `element` est dans
`liste` et `False` sinon.

## Exemple {num2}`exemple`

```{exec} python
:editor:
notes = [5, 5.5, 4, 5.5, 6]

note = 5

if note in notes:
    print(note, "est dans la liste")
else:
    print(note, "n'est pas dans la liste")
```

## Exercice {num2}`exercice`

Le programme ci-dessous demande à l'utilisateur quel moyen de locomotion il
utilise pour se rendre au travail et affiche un message en conséquence.

- "C'est très écologique!" lorsque l'utilisateur entre la valeur "à pied",
"trottinette", "skateboard" ou "vélo"
- "C'est un bon geste!" lorsque l'utilisateur entre la valeur "bus", "train" ou
"tram"
- "C'est acceptable!" s'il entre la valeur "voiture", "moto", "scooter",
"sidecar" ou "vespa".
- "Sans commentaire." s'il entre la valeur "avion"
- "Sans avis." s'il entre une autre valeur

Utilisez pour cela la notation `if ... in ...` quand cela est nécessaire.

```{exec} python
:editor: 21b10226-a456-4ab1-b04d-df9cef3aaf81
locomotion = input("Quel moyen de locomotion utilises-tu pour te rendre au travail: ")

# Complétez le programme à partir de là
print("C'est très écologique!")
print("C'est un bon geste!")
print("C'est acceptable!")
print("Sans commentaire.")
print("Sans avis.")
```

````{solution}
```{exec} python
:linenos:
locomotion = input("Quel moyen de locomotion utilises-tu pour aller au travail: ")

if locomotion in ["à pied", "trottinette", "skateboard", "vélo"]:
    print("C'est très écologique!")
elif locomotion in ["bus", "train", "tram"]:
    print("C'est un bon geste!")
elif locomotion in ["voiture", "sidecar", "vespa", "moto", "scooter"]:
    print("C'est acceptable!")
elif locomotion == "avion":
    print("Sans commentaire.")
else:
    print("Sans avis.")
```
````

## Exercice {num2}`exercice`

Depuis la station de métro où l'utilisateur se trouve, il peut se rendre aux
arrêts qui se trouvent dans la liste `ligne_sud` et `ligne_nord`. Lorsque
celui-ci entre sa destination, affichez s'il doit prendre la ligne sud, la
ligne nord, ou s'il ne peut pas se rendre à sa destination.

```{exec} python
:editor: e77565d0-b927-412b-b3e5-e6e7e8a00c72
destination = input("Où veux-tu aller: ")

ligne_nord = ["Châtelet", "Opéra", "République", "Bastille"]
ligne_sud = ["Gare du Nord", "Gare de Lyon", "Saint-Michel Notre-Dame", "Auber", "Porte d'Italie"]

# Complétez le programme à partir de là
print("Prends la ligne nord.")
print("Prends la ligne sud.")
print("Tu ne peux pas te rendre à cet arrêt.")
```

````{solution}
```{exec} python
:linenos:
destination = input("Où veux-tu aller: ")

ligne_nord = ["Châtelet", "Opéra", "République", "Bastille"]
ligne_sud = ["Gare du Nord", "Gare de Lyon", "Saint-Michel Notre-Dame",
             "Auber", "Porte d'Italie"]

if destination in ligne_nord:
    print("Prends la ligne nord.")
elif destination in ligne_sud:
    print("Prends la ligne sud.")
else:
    print("Tu ne peux pas te rendre à cet arrêt.")
```
````

## Exercice {num2}`exercice`

Complétez le programme ci-dessous afin que l'utilisateur puisse petit à petit
créer une liste avec les codes postaux dans lesquels il souhaite se rendre.
Cette liste des codes postaux ne doit jamais contenir de doublons! Si
l'utilisateur essaie d'en entrer un, le programme affichera "Erreur, ce code
postal est déjà dans la liste" et continuera ensuite normalement. Le programme
s'arrête quand l'utilisateur entre un code postal négatif. À ce moment, la liste
des codes postaux est simplement affichée.

```{exec} python
:editor: 61ad2b94-75ec-449a-9bb9-a9f5691fe626
# Complétez le programme
codes_postaux = []

code_postal = int(input("Entre un code postal: "))

print("Erreur, ce code postal est déjà dans la liste.")

print(codes_postaux)
```

````{solution}
```{exec} python
:linenos:
codes_postaux = []
code_postal = int(input("Entre un code postal : "))
while code_postal >= 0:
    if code_postal in codes_postaux:
        print("Erreur, ce code postal est déjà dans la liste.")
    elif code_postal >= 0:
        codes_postaux.append(code_postal)
    code_postal = int(input("Entre un code postal : "))

print(codes_postaux)
```
````
