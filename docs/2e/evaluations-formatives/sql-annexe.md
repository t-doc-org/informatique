% Copyright 2026 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# SQL - Annexes

## Liste des requêtes SQL

### Modification de la base de données

| Mots réservés | Description |
| :------------ | :---------- |
| `create table` | Crée une table |
| `insert into ... values` | Insère un élément (une ligne à la table) |
| `update ... set` | Met à jour des valeurs |
| `delete` | Supprime un élément (supprime une ligne à la table) |
| `alter table` | Modifie la structure de la table (ajout de colonne, ...) |
| `drop table` | Supprime une table |
| `drop database` | Supprime une base de données |

### Consultation de la base de données

| Mots réservés | Description |
| :------------ | :---------- |
| `select` | Sélectionne |
| `from` | Choisit les tables |
| `where` | Filtre le résultat avec des critères |
| `distinct` | Supprime les doublons |
| `order by ... asc` | Trie les résultats selon un attribut par ordre croissant |
| `order by ... desc` | Trie les résultats selon un attribut par ordre décroissant |
| `between ... and` | Filtre dans une plage de nombres |
| `like ...%` | Désigne une chaîne de caractères |
| `like ..._` | Représente un caractère |

### Jointure

| Mots réservés | Description |
| :------------ | :---------- |
| `join ... on ... ` | Joint deux tables ensembles |

## Type de données

### Types numériques

#### Nombres entiers

| Type | Description |
| :--- | :---------- |
| `tinyint` | -128 à 127 |
| `smallint` | -32'768 à 32'767 |
| **`int`** | -2'147'483'648 à 2'147'483'647 |
| `bigint` | -9'223'372'036'854'775'808 à 9'223'372'036'854'775'807 |

#### Nombres réels

| Type | Description |
| :--- | :---------- |
| **`decimal(taille,d)`** |  Nombre décimal <br> Le nombre de chiffre est précisé dans taille (max 65) et le nombre de décimales dans d (max 30) <br> `decimal(6,2)` &rarr; 1234.56 |
| `real` | Nombre réel (valeur approchée)|

### Types textes ou chaînes de caractères

| Type | Description |
| :--- | :---------- |
| **`text`** | Chaîne de caractères de taille quelconque |
| `char(n)` | Chaîne de caractères de **taille fixe** n |
| `varchar(n)` | Chaîne de caractères de **taille variable** au maximum n |

### Type des dates, durées et instants

| Type | Description |
| :--- | :---------- |
| `date` | Format: `AAAA-MM-JJ` |
| `datetime` | Format: `AAAA-MM-JJ hh:mm:ss` |
| `time` | Format: `hh:mm:ss` |
| `year` | Format: `AAAA` |

### Valeur null

En SQL, il existe une valeur notée `null`. Elle représente une absence de
valeur. Elle peut remplacer une valeur quel que soit le type attendu.

## Table **film** pour la question 2

| titre | producteur | genre | sortie | nb_entrees |
| :--: | :--: | :--: | :--: | :--: |
| No Time to Die | Barbara Broccoli | Espionnage | 2021 | 740 000 |
| Avatar | James Cameron | Science-fiction | 2009 | 1 180 000 |
| The Super Mario Bros. Movie | Chris Meledandri | Animation | 2023 | 580 000 |
| Top Gun: Maverick | Jerry Bruckheimer | Action | 2022 | 620 000 |
| Avengers: Endgame | Kevin Feige | Super-héros | 2019 | 640 000 |
| Barbie | Margot Robbie | Comédie | 2023 | 660 000 |
| Avatar : La Voie de l'eau | James Cameron | Science-fiction | 2022 | 1 012 000 |
| Moi, Moche et Méchant 4 | Chris Meledandri | Animation | 2024 | 420 000 |
| Skyfall | Barbara Broccoli | Espionnage | 2012 | 1 200 000 |
| Inside Out 2 | Mark Nielsen | Animation | 2024 | 550 000 |
| Spider-Man: No Way Home | Kevin Feige | Super-héros | 2021 | 510 000 |
| Pirates des Caraïbes 5 | Jerry Bruckheimer | Action | 2017 | 450 000 |

