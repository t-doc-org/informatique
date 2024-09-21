<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# Introduction

## Information versus données

Dans le langage courant, **information** et **données** sont souvent utilisés de
manière interchangeable. En informatique, les données sont la forme sous
laquelle l'information est représentée.

Un exmple d'information: "Il fait beau aujourd'hui!"

Les données qui représentent cette même information:\
01001001 01101100 00100000 01100110 01100001 01101001 01110100 00100000
01100010 01100101 01100001 01110101 00100000 01100001 01110101 01101010 01101111
01110101 01110010 01100100 00100111 01101000 01110101 01101001 00100001

## Trois défis

Lorsque nous représentons de l'information sur un support physique (disque dur,
clé USB, etc.), trois problèmes se posent:

1. La sécurité de l'information\
Dès que l'information est stockée ou transmise, elle peut tomber entre les
mains de n'importe qui. Comment puis-je la protéger?

2. La densité de l'information\
Il est nécessaire de trouver un moyen de stocker le maximum d'information en
utilisant le moins de place possible. Comment représenter et compresser des
données?

3. La durabilité de l'information\
Lors du stockage ou de la tansmission de données, des erreurs peuvent apparaître.
Comment détecter ou corriger ces erreurs?

En 1{sup}`ère` année, nous allons nous intéresser à la représentation de
l'information. Les autres défis seront abordés dans le cours de 2{sup}`e` année.

## Binaire

L'information traitée par un ordinateur (texte, image, son, vidéo) est sous
forme de données binaires, c'est-à-dire sous la forme d'une suite de 0 ou de 1.
Le **bit** vient de BInary digiT (b minuscule dans les notations) est l'unité la
plus simple en informatique, représenté par le chiffre 0 ou 1.

> **Pourquoi les ordinateurs fonctionnent-ils en binaire?**\
> Les ordinateurs sont composés de circuits électroniques qui laissent ou non
circuler l'électricité. Un circuit peut facilement représenter ces deux états:
allumé (1) ou éteint (0).

L'**octet** en anglais byte (o minuscule ou B majuscule dans les notations) est
une unité composée de 8 bits. Pour faciliter la lisibilité, nous regroupons en
général l'information par paquet de 8, 16, 32 ou 64 bits.

Voici les unités standardisées depuis 1998:

| Unité | Valeur en octets | Valeur en puissance de 10 |
|-------|------------------|---------------------------|
| Un **kilooctet** (ko ou kB) | 1 000 octets | $10^3$ octets |
| Un **Megaoctet** (Mo ou MB) | 1 000 ko | 1 000 000 octets = $10^6$ octets |
| Un **Gigaoctet** (Go ou GB) | 1 000 Mo | 1 000 000 000 octets = $10^9$ octets |
| Un **Téraoctet** (To ou TB) | 1 000 Go | 1 000 000 000 000 octets = $10^{12}$ octets |




