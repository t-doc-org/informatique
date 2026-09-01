% Copyright 2026 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# SQL

```{include} /_include/entete-examen.export.md
```
```{class} align-center
**Détails des calculs obligatoires. Attention au soin. Calculatrice autorisée.**
```
---

## Question {nump}`question`{points}`3`

Citez les trois manières d'enregistrer des données et expliquez en quoi cela
consiste.

```{solution}
Le stockage est l'enregistrement des fichiers sous forme de données binaires sur
un support physique (disque dur, clé USB, carte SSD, etc.).

La sauvegarde (backup en anglais) est une copie des données pertinentes à garder
sous la main pour une restauration (restore en anglais) rapide en cas de besoin.

L'archivage est l'enregistrement de fichiers pour des rétentions longues à
conserver, en général, pour des raisons légales.
```
## Question {nump}`question`{points}`3`

En utilisant la table `film` en annexe, indiquez ce qu'affichera les requêtes
suivantes:

{.lower-alpha-paren}
1.  ```{exec} sql
    :when:
    select titre from film where producteur = 'Kevin Feige';
    ```
2.  ```{exec} sql
    :when:
    select * from film where sortie = 2017;
    ```
3.  ```{exec} sql
    :when:
    select producteur from film where genre = 'Animation';
    ```

```{solution}
{.lower-alpha-paren}
1.  | titre |
    | :---: |
    | Avengers: Endgame |
    | Spider-Man: No Way Home |
2.  | titre | producteur | genre | sortie | nb_entrees |
    | :--: | :--: | :--: | :--: | :--: |
    | Pirates des Caraïbes 5 | Jerry Bruckheimer | Action | 2017 | 450 000 |
3.  | producteur |
    | :--: |
    | Chris Meledandri |
    | Chris Meledandri |
    | Mark Nielsen |
```

## Question {nump}`question`{points}`2`

Nous souhaitons créer une base de données relationnelle qui gère l'organisation
d'un meeting d'athlétisme. Les athlètes participent à des épreuves.

Dans le schéma relationnel suivant:

{.lower-alpha-paren}
1.  Indiquez les clés primaires et étrangères.
2.  Dessinez les relations entre les tables par des flèches.

```{graphviz}
digraph UML_Class_diagram {
  graph [
    label="Schéma relationnel: Meeting d'athlétisme"
    labelloc="t"
    fontname="Helvetica,Arial,sans-serif"
    fontsize="20pt"
    layout="circo"
    bgcolor="transparent"
  ]
  node [
    fontname="Helvetica,Arial,sans-serif"
    shape=record
    style=filled
    fillcolor=gray95
  ]
  edge [
    fontname="Helvetica,Arial,sans-serif"
    style=solid
    color=transparent
  ]

  Class2 -> Class1
  Class2 -> Class3

  Class1 [
    shape=plain
    label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
      <tr> <td> <b>athlete</b> </td> </tr>
      <tr> <td>
        <table border="0" cellborder="0" cellspacing="7" >
          <tr> <td align="left" port="u1">num_dossard</td> </tr>
          <tr> <td align="left" port="u2">nom</td> </tr>
          <tr> <td align="left" port="u3">prenom</td> </tr>
          <tr> <td align="left" port="u4">date_naissance</td> </tr>
          <tr> <td align="left" port="u5">categorie</td> </tr>
          <tr> <td align="left" port="u6">societe</td> </tr>
          <tr> <td align="left" port="u7">email</td> </tr>
        </table>
      </td> </tr>
    </table>>
  ]

  Class2 [
    shape=plain
    label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
      <tr> <td> <b>participe_a</b> </td> </tr>
      <tr> <td>
        <table border="0" cellborder="0" cellspacing="7" >
          <tr> <td align="left" port="l1">athlete</td> </tr>
          <tr> <td align="left" port="l2">epreuve</td> </tr>
          <tr> <td align="left" port="l3">resultat</td> </tr>
        </table>
      </td> </tr>
    </table>>
  ]

  Class3 [
    shape=plain
    label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
      <tr> <td> <b>epreuve</b> </td> </tr>
      <tr> <td>
        <table border="0" cellborder="0" cellspacing="7" >
          <tr> <td align="left" port="e1">id</td></tr>
          <tr> <td align="left" port="e2">nom</td></tr>
          <tr> <td align="left" port="e3">categorie</td></tr>
          <tr> <td align="left" port="e4">horaire</td></tr>
          <tr> <td align="left" port="e5">lieu</td></tr>
        </table>
      </td> </tr>
    </table>>
  ]
}
```

````{Solution}
```{graphviz}
digraph UML_Class_diagram {
  graph [
    label="Schéma relationnel: Meeting d'athlétisme"
    labelloc="t"
    fontname="Helvetica,Arial,sans-serif"
    fontsize="20pt"
    layout="circo"
    bgcolor="transparent"
  ]
  node [
    fontname="Helvetica,Arial,sans-serif"
    shape=record
    style=filled
    fillcolor=gray95
  ]
  edge [
    fontname="Helvetica,Arial,sans-serif"
    style=solid
  ]

  Class2:l1 -> Class1:u1
  Class2:l2 -> Class3:e1

  Class1 [
    shape=plain
    label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
      <tr> <td> <b>athlete</b> </td> </tr>
      <tr> <td>
        <table border="0" cellborder="0" cellspacing="7" >
          <tr> <td align="left" port="u1"><u>num_dossard</u></td> </tr>
          <tr> <td align="left" port="u2">nom</td> </tr>
          <tr> <td align="left" port="u3">prenom</td> </tr>
          <tr> <td align="left" port="u4">date_naissance</td> </tr>
          <tr> <td align="left" port="u5">categorie</td> </tr>
          <tr> <td align="left" port="u6">societe</td> </tr>
          <tr> <td align="left" port="u7">email</td> </tr>
        </table>
      </td> </tr>
    </table>>
  ]

  Class2 [
    shape=plain
    label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
      <tr> <td> <b>participe_a</b> </td> </tr>
      <tr> <td>
        <table border="0" cellborder="0" cellspacing="7" >
          <tr> <td align="left" port="l1"><u>#athlete</u></td> </tr>
          <tr> <td align="left" port="l2"><u>#epreuve</u></td> </tr>
          <tr> <td align="left" port="l3">resultat</td> </tr>
        </table>
      </td> </tr>
    </table>>
  ]

  Class3 [
    shape=plain
    label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
      <tr> <td> <b>epreuve</b> </td> </tr>
      <tr> <td>
        <table border="0" cellborder="0" cellspacing="7" >
          <tr> <td align="left" port="e1"><u>id</u></td></tr>
          <tr> <td align="left" port="e2">nom</td></tr>
          <tr> <td align="left" port="e3">categorie</td></tr>
          <tr> <td align="left" port="e4">horaire</td></tr>
          <tr> <td align="left" port="e5">lieu</td></tr>
        </table>
      </td> </tr>
    </table>>
  ]
}
```
````

## Question {nump}`question`{points}`2`

Écrivez la requête SQL qui permet de créer la table `athlete` avec tous les
attributs nécessaires (type, clé primaire etc.). Toutes les informations sont
obligatoires à l'exception de la société.

````{solution}
```{exec} sql
:when:
create table athlete (
    num_dossard int not null primary key,
    nom text not null,
    prenom text not null,
    date_naissance date not null,
    categorie text not null,
    societe text,
    email text not null
);
```
````

## Question {nump}`question`{points}`2`

Ajoutez dans la table `athlete` deux lignes avec les informations suivantes:

{.lower-alpha-paren}
1.  **Bob Dupont** a le dossard numéro **1**, sa date de naissance est le
    **1 avril 2009**. Il appartient donc à la catégorie **U18-M**. Il fait
    partie du **Club Athlétique de Belfaux**. Son email est
    **bob.dupont@gmail.com**.
2.  **Alice Martin** à le dossard numéro **7**, sa date de naissance est le
    **28 février 2010**. Elle appartient donc à la catégorie **U18-F**. Son
    email est **alice.martin@gmail.com**.

````{solution}
{.lower-alpha-paren}
1.  ```{exec} sql
    :when:
    insert into athlete values (1, 'Dupont', 'Bob', '2009-04-01', 'U18-M',
        'Club Athlétique de Belfaux', 'bob.dupont@gmail.com');
    ```
2.  ```{exec} sql
    :when:
    insert into athlete values (7, 'Martin', 'Alice', '2010-02-28', 'U18-F',
        null, 'alice.martin@gmail.com');
    ```

    ```{exec} sql
    :when:
    insert into athlete
        (num_dossard, nom, prenom, date_naissance, categorie, email)
        values (7, 'Martin', 'Alice', '2010-02-28', 'U18-F', 'alice.martin@gmail.com');
    ```
````

{.allow-break-inside}
## Question {nump}`question`{points}`16`

{.lower-alpha-paren}
1.  Écrivez une requête SQL qui retourne la liste de tous les athlètes avec
    leurs informations.
2.  Écrivez une requête SQL qui retourne le nom et le prénom des athlètes qui
    font partie du **Club athlétique Fribourg**.
3.  Écrivez une requête SQL qui retourne le nom de tous les clubs sans doublon.
4.  Écrivez une requête SQL qui affiche l'horaire et le lieu de l'épreuve du
    **100m** de la catégorie **U20-F**.
5.  Écrivez une requête SQL qui retourne la liste des épreuves des catégories
    **U18** (femme et homme) triée par ordre alphabétique des noms des épreuves.
6.  Écrivez une requête SQL qui retourne tous les résultats de l'athlète **Bob
    Dupont**.
7.  Écrivez une requête SQL qui retourne le nom et le prénom des athlètes qui
    participent à l'épreuve de **Saut en longueur**.
8.  Écrivez une requête qui retourne la liste de tous les résultats avec le nom
    de l'épreuve, ainsi que le nom et le prénom de l'athlète.

````{solution}
{.lower-alpha-paren}
1.  ```{exec} sql
    :when:
    select * from athlete;
    ```
2.  ```{exec} sql
    :when:
    select nom, prenom from athlete
    where societe = 'Club athlétique Fribourg';
    ```
3.  ```{exec} sql
    :when:
    select distinct societe from athlete;
    ```
4.  ```{exec} sql
    :when:
    select horaire, lieu from epreuve
    where nom = '100m' and categorie = 'U20-F';
    ```
5.  ```{exec} sql
    :when:
    select * from epreuve
    where categorie like 'U18%'
    order by nom;
    ```
6.  ```{exec} sql
    :when:
    select participe_a.resultat from participe_a
    join athlete
    on participe_a.athlete = athlete.num_dossard
    where athlete.nom = 'Dupont' and athlete.prenom = 'Bob';
    ```
7.  ```{exec} sql
    :when:
    select athlete.nom, athlete.prenom from athlete
    join participe_a on participe_a.athlete = athlete.num_dossard
    join epreuve on participe_a.epreuve = epreuve.id
    where epreuve.nom = 'Saut en longueur';
    ```
8.  ```{exec} sql
    :when:
    select participe_a.resultat, epreuve.nom, athlete.nom, athlete.prenom from athlete
    join participe_a on participe_a.athlete = athlete.num_dossard
    join epreuve on participe_a.epreuve = epreuve.id;
    ```
````
