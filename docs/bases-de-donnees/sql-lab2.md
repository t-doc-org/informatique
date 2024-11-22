% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# SQL Lab 2

Le but de cette section est d'entraîner les concepts vus dans les sections
[](bd-relationnelle.md) et [](sql2.md).

## Exercice {num}`exo-bd-lab2`

Nous souhaitons créer une base de données pour une bibliothèque communale. Pour
emprunter un livre, Bob doit scanner son code-barre personnel et celui du livre.
Lors de l'emprunt, la date de retour est fixée. Chaque livre a un titre, un
auteur, un éditeur, un ISBN qui est unique et une année de sortie. Un usager a
un nom, un prénom, une adresse, un code postal, une ville, un email et un
code-barre personnel. De chaque auteur, nous connaissons le nom et le prénom.

1. Déterminer les différentes tables nécessaires.
2. Déterminer les colonnes de chaque table.
3. Déterminer les clés primaires et étrangères.
4. Dessiner le schéma relationnel.

````{solution}
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
          <tr> <td align="left" port="u3">adresse</td> </tr>
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
````

## Exercice {num}`exo-bd-lab2`

Créer les différentes tables: `usager`, `livre`, `auteur`, `auteur_de` et
`emprunt`. Ne pas oublier d'indiquer le type et les attributs (`primary key`,
`not null`, etc.) quand c'est nécessaire.

```{exec} sql
:name: sql-biblio-resp
:then: sql-biblio-select-usager sql-biblio-select-livre sql-biblio-select-auteur sql-biblio-select-auteur-de sql-biblio-select-emprunt
:editable:
```

Pour tester que la table `usager` est correcte:
```{exec} sql
:name: sql-biblio-select-usager
:after: sql-biblio-resp
select * from usager;
```

Pour tester que la table `livre` est correcte:
```{exec} sql
:name: sql-biblio-select-livre
:after: sql-biblio-resp
select * from livre;
```

Pour tester que la table `auteur` est correcte:
```{exec} sql
:name: sql-biblio-select-auteur
:after: sql-biblio-resp
select * from auteur;
```

Pour tester que la table `auteur_de` est correcte:
```{exec} sql
:name: sql-biblio-select-auteur-de
:after: sql-biblio-resp
select * from auteur_de;
```

Pour tester que la table `emprunt` est correcte:
```{exec} sql
:name: sql-biblio-select-emprunt
:after: sql-biblio-resp
select * from emprunt;
```

````{solution}
```{exec} sql
:name: sql-biblio
:when: never
:include: biblio-creation.sql
```
````

## Exercice {num}`exo-bd-lab2`

Toutes les requêtes de cet exercice se font dans une seule table.

```{exec} sql
:name: sql-biblio-insert
:after: sql-biblio
:include: biblio-insertion.sql
:when: never
:class: hidden
```

1.  Écrire une requête SQL qui retourne tous les livres.

    ```{exec} sql
    :after: sql-biblio-insert
    :editable:
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-biblio-insert
    select * from livre;
    ```
    ````

2.  Écrire une requête SQL qui retourne tous les noms des usagers.

    ```{exec} sql
    :after: sql-biblio-insert
    :editable:
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-biblio-insert
    select nom from usager;
    ```
    ````

3.  Écrire une requête SQL qui retourne tous les éditeurs sans doublons.

    ```{exec} sql
    :after: sql-biblio-insert
    :editable:
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-biblio-insert
    select distinct editeur from livre;
    ```
    ````

4.  Écrire une requête SQL qui retourne le titre et l'année des livres publiés
    avant 1980.

    ```{exec} sql
    :after: sql-biblio-insert
    :editable:
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-biblio-insert
    select titre, annee from livre where annee < 1980;
    ```
    ````

5.  Écrire une requête SQL qui retourne le titre des livres dont le titre
    commence par le mot "Astérix".

    ```{exec} sql
    :after: sql-biblio-insert
    :editable:
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-biblio-insert
    select titre from livre where titre like 'Astérix%';
    ```
    ````

6.  Écrire une requête SQL qui retourne le titre des livres dont le titre
    contient le mot "Astérix".

    ```{exec} sql
    :after: sql-biblio-insert
    :editable:
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-biblio-insert
    select titre from livre where titre like '%Astérix%';
    ```
    ````


7.  Écrire une requête SQL qui retourne l'isbn des livres à rendre avant le 31
    décembre 2024.

    ```{tip}
    Les dates se notent entre guillemets simples.
    ```

    ```{exec} sql
    :after: sql-biblio-insert
    :editable:
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-biblio-insert
    select isbn from emprunt where retour < '2024-12-31';
    ```
    ````

8.  Écrire une requête SQL qui retourne le nom et le prénom de tous les auteurs
    triés par ordre alphabétique.

    ```{exec} sql
    :after: sql-biblio-insert
    :editable:
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-biblio-insert
    select nom, prenom from auteur order by nom asc;
    ```
    ````

9.  Écrire une requête SQL qui retourne le nom, le prénom et l'adresse des usagers
    vivant à Fribourg.

    ```{exec} sql
    :after: sql-biblio-insert
    :editable:
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-biblio-insert
    select nom, prenom, adresse from usager where ville = 'Fribourg';
    ```
    ````

10. Écrire une requête SQL qui retourne l'année et le titre des livres publiés
    entre 2012 et 2015.

    ```{exec} sql
    :after: sql-biblio-insert
    :editable:
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-biblio-insert
    select annee, titre from livre where annee between 2012 and 2015;
    ```
    ````

## Exercice {num}`exo-bd-lab2`

Formuler en français ce que nous cherchons avec les requêtes suivantes:

1.  ```{code-block} sql
    select * from livre where titre like '%Robot%';
    ```

    ````{solution}
    Affiche tous les livres dont le titre contient "Robot".
    ````

2.  ```{code-block} sql
    select nom, prenom from usager where ville = 'Granges-Paccots';
    ```

    ````{solution}
    Affiche le nom et le prénom des usagers habitant Granges-Paccots.
    ````

3.  ```{code-block} sql
    select usager.nom, usager.prenom from usager
      join emprunt on usager.code_barre = emprunt.code_barre
      where retour < '2024-12-01';
    ```

    ````{solution}
    Affiche le nom et le prénom des usagers qui doivent rendre un livre avant le
    premier décembre.
    ````

## Exercice {num}`exo-bd-lab2`

Pour cet exercice, il faudra utiliser des jointures de tables.

1.  Écrire une requête SQL qui retourne le titre des livres empruntés.

    ```{exec} sql
    :after: sql-biblio-insert
    :editable:
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-biblio-insert
    select livre.titre from livre
      join emprunt on livre.isbn = emprunt.isbn;
    ```
    ````

2.  Écrire une requête SQL qui retourne le titre des livres empruntés à rendre
    après le 15 décembre.

    ```{exec} sql
    :after: sql-biblio-insert
    :editable:
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-biblio-insert
    select livre.titre from livre
      join emprunt on livre.isbn = emprunt.isbn
      where retour > '2024-12-15';
    ```
    ````

3.  Écrire une requête SQL qui retourne le nom et le prénom des usagers qui ont
    emprunté des livres.

    ```{exec} sql
    :after: sql-biblio-insert
    :editable:
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-biblio-insert
    select usager.nom, usager.prenom from usager
      join emprunt on usager.code_barre = emprunt.code_barre;
    ```
    ````

    Les mêmes noms et prénoms apparaissent plusieurs fois, supprimer les
    doublons.

      ```{exec} sql
    :after: sql-biblio-insert
    :editable:
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-biblio-insert
    select distinct usager.nom, usager.prenom from usager
      join emprunt on usager.code_barre = emprunt.code_barre;
    ```
    ````

4.  Écrire une requête SQL qui retourne le nom et le prénom de l'auteur du livre
    "La Mort d'Ivan Ilitch".

    ```{exec} sql
    :after: sql-biblio-insert
    :editable:
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-biblio-insert
    select auteur.nom, auteur.prenom from auteur
      join auteur_de on auteur.a_id = auteur_de.a_id
      join livre on auteur_de.isbn = livre.isbn
      where titre = 'La Mort d''Ivan Ilitch';
    ```
    ````

5.  Écrire une requête SQL qui retourne le nom et le prénom de l'usager qui a
    emprunté "Jack Barron et l'Éternité".

    ```{exec} sql
    :after: sql-biblio-insert
    :editable:
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-biblio-insert
    select usager.nom, usager.prenom from usager
      join emprunt on usager.code_barre = emprunt.code_barre
      join livre on emprunt.isbn = livre.isbn
      where titre = 'Jack Barron et l''Éternité';
    ```
    ````

6.  Écrire une requête SQL qui retourne le titre et la date de retour des livres
    empruntés par Philippe Dubois.

    ```{exec} sql
    :after: sql-biblio-insert
    :editable:
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-biblio-insert
    select livre.titre, emprunt.retour from livre
      join emprunt on livre.isbn = emprunt.isbn
      join usager on emprunt.code_barre = usager.code_barre
      where usager.nom = 'Dubois' and usager.prenom = 'Philippe';
    ```
    ````

7.  Écrire une requête SQL qui retourne le titre des livres publiés avant
    "Astérix chez les Bretons".

    ```{exec} sql
    :after: sql-biblio-insert
    :editable:
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-biblio-insert
    select livre.titre from livre
      where annee < (select annee from livre
                     where titre = 'Astérix chez les Bretons');
    ```
    ````

8.  **Challenge**: Écrire une requête SQL qui retourne le nom et le prénom des
    auteurs des livres de la question précédente sans doublons.

    ```{exec} sql
    :after: sql-biblio-insert
    :editable:
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-biblio-insert
    select distinct auteur.nom, auteur.prenom from auteur
      join auteur_de on auteur.a_id = auteur_de.a_id
      join livre on livre.isbn = auteur_de.isbn
      where annee < (select annee from livre
                     where titre = 'Astérix chez les Bretons');
    ```
    ````
