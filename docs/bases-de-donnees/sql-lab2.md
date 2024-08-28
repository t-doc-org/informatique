<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# BD Lab 2

Le but de cette section est d'entraîner les concepts vus dans les sections
[](./bd-relationnelle.md) et [](./sql2.md).

## Exercice 1

Nous souhaitons créer une base de données pour une bibliothèque communale. Pour
emprunter un livre, Bob doit scanner son code-barre personnel et celui du livre.
Lors de l'emprunt, la date de retour est fixée.
1. Déterminer les différentes tables nécessaires.
2. Déterminer les colonnes de chaque table.
3. Déterminer les clés primaires et étrangères.
4. Dessiner le schéma relationnel.


<!-- TODO:  Remettre les solutions. -->

<!-- ````{admonition} Solution
:class: note dropdown
```{graphviz}
:align: center
digraph UML_Class_diagram {
  graph [
    label="Schéma relationnel: Bibliothèque"
    labelloc="t"
    fontname="Helvetica,Arial,sans-serif"
    fontsize="20pt"
    layout="circo"
  ]
  node [
    fontname="Helvetica,Arial,sans-serif"
    shape=record
    style=filled
    fillcolor=gray95
  ]
  edge [fontname="Helvetica,Arial,sans-serif"]
  edge [style=solid]
  Class3:e1 -> Class1:u7
  Class3:e2 -> Class2:l4
  Class5:ad1 -> Class4:a1
  Class5:ad2 -> Class2:l4

  Class1 [
    shape=plain
    label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
      <tr> <td> <b>usager</b> </td> </tr>
      <tr> <td>
        <table border="0" cellborder="0" cellspacing="7" >
          <tr> <td align="left" port="u1">nom</td> </tr>
          <tr> <td align="left" port="u2">prenom</td> </tr>
          <tr> <td align="left" port="u3">adress</td> </tr>
          <tr> <td align="left" port="u4">code_postal</td> </tr>
          <tr> <td align="left" port="u5">ville</td> </tr>
          <tr> <td align="left" port="u6">email</td> </tr>
          <tr> <td align="left" port="u7"><u>code_barre</u></td> </tr>
        </table>
      </td> </tr>
    </table>>
  ]

  Class2 [
    shape=plain
    label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
      <tr> <td> <b>livre</b> </td> </tr>
      <tr> <td>
        <table border="0" cellborder="0" cellspacing="7" >
          <tr> <td align="left" port="l1">titre</td> </tr>
          <tr> <td align="left" port="l2">editeur</td> </tr>
          <tr> <td align="left" port="l3">annee</td> </tr>
          <tr> <td align="left" port="l4"><u>isbn</u></td> </tr>
        </table>
      </td> </tr>
    </table>>
  ]

  Class3 [
    shape=plain
    label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
      <tr> <td> <b>emprunt</b> </td> </tr>
      <tr> <td>
        <table border="0" cellborder="0" cellspacing="7" >
          <tr> <td align="left" port="e1"><u># code_barre</u></td> </tr>
          <tr> <td align="left" port="e2"><u># isbn</u></td> </tr>
          <tr> <td align="left" port="e3">retour</td> </tr>
        </table>
      </td> </tr>
    </table>>
  ]

  Class4 [
    shape=plain
    label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
      <tr> <td> <b>auteur</b> </td> </tr>
      <tr> <td>
        <table border="0" cellborder="0" cellspacing="7" >
          <tr> <td align="left" port="a1"><u>a_id</u></td> </tr>
          <tr> <td align="left" port="a2">nom</td> </tr>
          <tr> <td align="left" port="a3">prenom</td> </tr>
        </table>
      </td> </tr>
    </table>>
  ]

  Class5 [
    shape=plain
    label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
      <tr> <td> <b>auteur_de</b> </td> </tr>
      <tr> <td>
        <table border="0" cellborder="0" cellspacing="7" >
          <tr> <td align="left" port="ad1"><u># a_id</u></td> </tr>
          <tr> <td align="left" port="ad2"><u># isbn</u></td> </tr>
        </table>
      </td> </tr>
    </table>>
  ]

}
```
```` -->

## Exercice 2

[Créer](#creation) une nouvelle base de données.

Écrire les requêtes SQL qui permettent de créer cette base de données. Ne
pas oublier d'indiquer le type et les attributs (`primary key`, `not null`,
etc.) quand c'est nécessaire.

<!-- ````{admonition} Solution
:class: note dropdown
```{code-block} sql
create table usager (
    nom text not null,
    prenom text not null,
    adresse text,
    code_postal char(4),
    ville text,
    email text not null,
    code_barre char(15) primary key not null
);

create table livre (
    titre text not null,
    editeur text,
    annee int,
    isbn char(14) primary key not null
);

create table auteur (
    a_id int primary key not null,
    nom text not null,
    prenom text not null
);

create table auteur_de (
    a_id int not null,
    isbn char(14) not null,
    primary key (a_id, isbn)
);

create table emprunt (
    code_barre char(15) not null,
    isbn char(14) primary key not null,
    retour date not null
);
```
```` -->

## Exercice 3

Toutes les requêtes de cet exercice se font dans une seule table.

0. [Importer](#import) la requête [biblio-insertion.sql](./biblio-insertion.sql) dans
VSCode pour insérer les éléments dans la base de données.

1. Écrire une requête SQL qui affiche tous les livres.

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select * from livre;
    ```
    ```` -->
2. Écrire une requête SQL qui affiche tous les noms des usagers.

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select nom from usager;
    ```
    ```` -->

3. Écrire une requête SQL qui affiche tous les éditeurs sans doublons.

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select distinct editeur from livre;
    ```
    ```` -->

4. Écrire une requête SQL qui affiche le titre et l'année des livres publiés
avant 1980.

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select titre from livre where annee < 1980;
    ```
    ```` -->

5. Écrire une requête SQL qui affiche le titre des livres dont le titre
contient le mot "Astérix".

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select titre from livre where titre like '%Astérix%';
    ```
    ```` -->

6. Écrire une requête SQL qui affiche l'isbn des livres à rendre avant le 31
décembre 2024.

    ```{tip}
    Les dates se notent entre guillemets simples.
    ```

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select isbn from emprunt where date < '2024-12-31';
    ```
    ```` -->

7. Écrire une requête SQL qui affiche le nom et le prénom de tous les auteurs
triés par ordre alphabétique.

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select nom, prenom from auteur order by nom asc;
    ```
    ```` -->

8. Écrire une requête SQL qui affiche le nom et l'adresse des usagers vivant à
Fribourg.

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select nom, adresse from usager where ville = 'Fribourg';
    ```
    ```` -->

9. Écrire une requête SQL qui affiche l'année et le titre des livres publiés
entre 2005 et 2015.

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select annee, titre from livre where annee between 2005 and 2015;
    ```
    ```` -->

## Exercice 4

Formuler en français ce que nous cherchons avec les requêtes suivantes:

1.  ```{code-block} sql
    select * from livre where titre like '%Robot%';
    ```

    <!-- ````{admonition} Solution
    :class: note dropdown
    Affiche tous les livres dont le titre contient "Robot".
    ``` -->

2.
    ```{code-block} sql
    select nom, prenom from usager where ville = 'Granges-Paccots';
    ```

    <!-- ````{admonition} Solution
    :class: note dropdown
    Affiche le nom et le prénom des usagers habitant Granges-Paccots.
    ```` -->

3.
    ```{code-block} sql
    select usager.nom, usager.prenom from usager
    join emprunt on usager.code_barre = emprunt.code_barre
    where retour < '2024-12-01'
    ```

    <!-- ````{admonition} Solution
    :class: note dropdown
    Affiche le nom et le prénom des usagers qui doivent rendre un livre avant le
    premier décembre.
    ```` -->

## Exercice 5

Pour cet exercice, il faudra utiliser des jointures de tables.

1. Écrire une requête SQL qui affiche le titre des livres empruntés.

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select livre.titre from livre
    join emprunt on livre.isbn = emprunt.isbn;
    ```
    ```` -->

2. Écrire une requête SQL qui affiche le titre des livres empruntés à rendre
après le 15 décembre.

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select livre.titre from livre
    join emprunt on livre.isbn = emprunt.isbn
    where retour < '2024-12-15';
    ```
    ```` -->
3. Écrire une requête SQL qui affiche le nom et le prénom des usagers qui ont
emprunté des livres, sans doublons.

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select distinct usager.nom, usager.prenom from usager
    join emprunt on usager.code_barre = emprunt.code_barre;
    ```
    ```` -->

4. Écrire une requête SQL qui affiche le nom et le prénom de l'auteur du livre
"La Mort d'Ivan Ilitch".

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select auteur.nom, auteur.prenom from auteur
    join auteur_de on auteur.a_id = auteur_de.a_id
    join livre on livre.isbn = auteur_de.isbn
    where titre = 'La Mort d''Ivan Ilitch'
    ```
    ```` -->

5. Écrire une requête SQL qui affiche le titre des livres publiés avant "Astérix
chez les Bretons".

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select livre.titre from livre
    where annee < (select annee from livre
                   where titre = 'Astérix chez les Bretons')
    ```
    ```` -->


6. **Challenge**: Écrire une requête SQL qui affiche le nom et le prénom des
auteurs des livres de la question précédente.

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select auteur.nom, auteur.prenom from auteur
    join auteur_de on auteur.a_id = auteur_de.a_id
    join livre on livre.isbn = auteur_de.isbn
    where annee < (select annee from livre
                   where titre = 'Astérix chez les Bretons')
    ```
    ```` -->
