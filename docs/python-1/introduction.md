% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Introduction

## Qu'est-ce qu'un langage de programmation?

Un langage de programmation est une notation qui permet de communiquer avec
l'ordinateur.

Comme en français, il comprend:

- un alphabet (chiffres, lettres, ...)
- un vocabulaire (instructions, des mots réservés, ...)
- une syntaxe (ponctuation, indentation, ...)

Exemple:

```{exec} python
:when: never
:linenos:
prenom = input("Quel est ton prénom? ")
age = int(input("Quel est ton âge? "))
print("Salut", prenom, "!")
if age >= 18:
  print("Tu es majeur(e).")
else:
  print("Tu es mineur(e).")
```

## Type de langages

Il existe des langage de **bas niveau** et des langages de **haut niveau**.

Les langages de bas niveau, comme l'assembleur, sont très proches du code machine.

```{code-block}
:linenos:
.model small
.stack 100h

.data
msg db 'Hello world!$'

.code
start:
  mov ah, 09h     ; display the message
  lea dx, msg
  int 21h
  mov ax, 4C00h   ; terminate the executable
  int 21h
end start
```

Les langages de haut niveau, comme le python, sont très proches de l'anglais.

```{exec} python
:linenos:
print("Hello world!")
```

Il existe des centaines de langages de programmation qui ont des
caractéristiques différentes, il faut choisir son langage en fonction de ses
besoins:

- Haut ou bas niveau
- Facilité d'utilisation
- Sureté
- Rapidité
- Puissance
- ...

## Python

Le langage Python a été créé par [Guido Van Rossen](https://fr.wikipedia.org/wiki/Guido_van_Rossum)
en 1989. Il a écrit une première version pendant ses vacances de Noël. La
première version publique a été publiée en février 1991.

Il a décidé de baptiser ce projet Python, car il est fan de la série télévisée
***Monty Python's Flying Circus***.

## Pourquoi apprendre Python à l'école

- Syntaxe simple et facile à comprendre
- Langage très populaire et très utilisé
- Langage adapté à beaucoup de domaines:
    - développement
    - interface Web
    - analyse de données
    - intelligence artificielle
    - scripting
    - jeux
    - ...

