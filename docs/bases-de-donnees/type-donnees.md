<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# Type de données

Lors de la création de tables en SQL, il faut déterminer le type des attributs.
Il est important de choisir un type adapté aux données qui seront stockées afin
d'optimiser l'espace de la mémoire utilisée.

Par exemple, utiliser BIGINT pour stocker l'âge d'une personne est inutile.
TINYINT est largement suffisant.

Il existe plusieurs catégories de types de données:

1. types numériques
2. types textes
3. type des dates, durées et instants

## Types numériques

Les entiers

| Type | Description |
| :--- | :---------- |
| TINYINT | -127 à 128 |
| SMALLINT | -32'768 à 32'7676 |
| INT | -2'147'483'648 à 2'147'483'647 |
| BIGINT | -9'223'372'036'854'775'808 à 9'223'372'036'854'775'807 |

Les nombres réels

| Type | Description |
| :--- | :---------- |
| DECIMAL(taille,d) | Le nombre de chiffre est précisé dans taille (max 65) et le nombre de décimales <br> dans d (max 30) <br> DECIMAL(6,2) -> 2345.67 |


## Types textes ou chaînes de caractères

| Type | Description |
| :--- | :---------- |
| CHAR(n) | Chaîne de caractères de **taille fixe** n |
| VARCHAR(n) | Chaîne de caractères de **taille variable** au maximum n |
| TEXT | Chaîne de caractères de taille quelconque |

## Type des dates, durées et instants

| Type | Description |
| :--- | :---------- |
| DATE | Format: AAAA-MM-JJ |
| DATETIME | Format: AAAA-MM-JJ hh:mm:ss |
| TIME | Format: hh:mm:ss |
| YEAR | Format: AAAA |

## Exercice

Remplir le tableau dans le document joint [Exercice sur les types](./exercice-types.pdf).








