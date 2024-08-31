<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# Liste des requêtes SQL

## Modification de la base de données

| Mots réservés | Description |
| :------------ | :---------- |
| `create table` | Crée une table |
| `insert into ... values` | Insère un élément (une ligne à la table) |
| `update ... set` | Met à jour des valeurs |
| `delete` | Supprime un élément (supprime une ligne à la table) |
| `alter table` | Modifie la structure de la table (ajout de colonne, ...) |
| `drop table` | Supprime une table |
| `drop database` | Supprime une base de données |

```{attention}
Avec SQLite, la requête `drop database` n'existe pas. Pour supprimer une base de
données, il suffit de supprimer le fichier qui correspond à cette base de
données.
```

## Consultation de la base de données

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


## Jointure

| Mots réservés | Description |
| :------------ | :---------- |
| `join ... on ... where` | Joint plusieurs tables ensembles |


