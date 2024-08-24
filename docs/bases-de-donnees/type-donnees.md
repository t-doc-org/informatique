<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# Type de données

Lors de la création de tables en SQL, il faut déterminer le type des colonnes.
Il y a quelques années, il était important de choisir le type le mieux adapté
aux données afin d'optimiser l'espace de la mémoire utilisée. Actuellement, les
bases de données sont intelligentes et gèrent elles-mêmes l'espace-mémoire. Il
faut toutefois choisir le type correct et suivant le système de gestion de base
de données utilisées, il peut y avoir des différences.

Il existe plusieurs catégories de types de données:

1. types numériques
2. types textes
3. type des dates, durées et instants

## Types numériques

Les entiers

| Type | Description |
| :--- | :---------- |
| tinyint | -127 à 128 |
| smallint | -32'768 à 32'7676 |
| **int** | -2'147'483'648 à 2'147'483'647 |
| bigint | -9'223'372'036'854'775'808 à 9'223'372'036'854'775'807 |

Les nombres réels

| Type | Description |
| :--- | :---------- |
| **decimal(taille,d)** |  Nombre décimal <br> Le nombre de chiffre est précisé dans taille (max 65) et le nombre de décimales <br> dans d (max 30) <br> decimal(6,2) -> 2345.67 |
| real | Nombre réel (valeur approchée)|


## Types textes ou chaînes de caractères

| Type | Description |
| :--- | :---------- |
| **text** | Chaîne de caractères de taille quelconque |
| char(n) | Chaîne de caractères de **taille fixe** n |
| varchar(n) | Chaîne de caractères de **taille variable** au maximum n |


## Type des dates, durées et instants

| Type | Description |
| :--- | :---------- |
| date | Format: AAAA-MM-JJ |
| datetime | Format: AAAA-MM-JJ hh:mm:ss |
| time | Format: hh:mm:ss |
| year | Format: AAAA |

## Exercice

<!-- TODO: Remplacer le pdf par un pdf éditable avec ouverture directement dans
           le browser -->
Remplir le tableau dans le document joint [Exercice sur les types](./exercice-types.docx).

(null)=
## Valeur null

En SQL, il existe une valeur notée **null**. Elle représente une absence de
valeur. Elle peut remplacer une valeur quel que soit le type attendu.






