% Copyright 2026 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
subject: "Informatique 2e année"
```

# Bases de données

## Données

- Connaître le vocabulaire propre aux données (dossier, fichier, données
  explicites et implicites, format non-structuré, ...)
- Connaître les trois manières d'enregistrer des données.


## Modèle relationnel

- Savoir ce qu'est une base de données et à quoi elle sert.
- Connaître le fonctionnement du modèle relationnel.
- Connaître la définition d'une clé primaire et d'une clé étrangère et leur
  fonctionnement.
- Savoir dessiner, en respectant les règles, un schéma du modèle relationnel
  correspondant à un énoncé.


## SQL

- Savoir ce qu'est le langage SQL et à quoi il sert.
- Savoir créer une table en
    - choisissant des noms de colonnes adéquats,
    - choisissant le type le plus appropriés,
    - déterminant la clé primaire,
    - empêchant les colonnes vides lorsque cela est nécessaire,
    - indiquant une valeur par défaut lorsque cela est nécessaire.
- Savoir insérer une nouvelle ligne dans une table en connaissant
    - la valeur de toutes les colonnes,
    - la valeur d'une partie des colonnes.
- Savoir modifier la valeur d'une cellule.
- Savoir supprimer une ligne.
- Savoir faire des jointures de tables.
- Sélectionner certaines/toutes les colonnes d'une ou plusieurs tables avec
    - des critères simples,
    - des critères composés (and, or),
    - des éléments similaires (like),
    - avec des filtres (between),
    - sans doublons (distinct),
    - en ordre croissant ou décroissant (order by).

## Documents à disposition pendant l'évaluation

### Liste des requêtes SQL

#### Modification de la base de données

| Mots réservés | Description |
| :------------ | :---------- |
| `create table` | Crée une table |
| `insert into ... values` | Insère un élément (une ligne à la table) |
| `update ... set` | Met à jour des valeurs |
| `delete` | Supprime un élément (supprime une ligne à la table) |
| `alter table` | Modifie la structure de la table (ajout de colonne, ...) |
| `drop table` | Supprime une table |
| `drop database` | Supprime une base de données |

#### Consultation de la base de données

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

#### Jointure

| Mots réservés | Description |
| :------------ | :---------- |
| `join ... on ... ` | Joint deux tables ensembles |

### Type de données

#### Types numériques

##### Nombres entiers

| Type | Description |
| :--- | :---------- |
| `tinyint` | -128 à 127 |
| `smallint` | -32'768 à 32'767 |
| **`int`** | -2'147'483'648 à 2'147'483'647 |
| `bigint` | -9'223'372'036'854'775'808 à 9'223'372'036'854'775'807 |

##### Nombres réels

| Type | Description |
| :--- | :---------- |
| **`decimal(taille,d)`** |  Nombre décimal <br> Le nombre de chiffre est précisé dans taille (max 65) et le nombre de décimales dans d (max 30) <br> `decimal(6,2)` &rarr; 1234.56 |
| `real` | Nombre réel (valeur approchée)|

#### Types textes ou chaînes de caractères

| Type | Description |
| :--- | :---------- |
| **`text`** | Chaîne de caractères de taille quelconque |
| `char(n)` | Chaîne de caractères de **taille fixe** n |
| `varchar(n)` | Chaîne de caractères de **taille variable** au maximum n |

#### Type des dates, durées et instants

| Type | Description |
| :--- | :---------- |
| `date` | Format: `AAAA-MM-JJ` |
| `datetime` | Format: `AAAA-MM-JJ hh:mm:ss` |
| `time` | Format: `hh:mm:ss` |
| `year` | Format: `AAAA` |

#### Valeur null

En SQL, il existe une valeur notée `null`. Elle représente une absence de
valeur. Elle peut remplacer une valeur quel que soit le type attendu.


