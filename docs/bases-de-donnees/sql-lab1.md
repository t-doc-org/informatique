<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# SQL Lab 1

Le but de cette section est d'entraîner les concepts vus dans la section
[](./sql.md).

Voici la table **canton** contenant certaines informations sur des cantons
suisses.

```{exec} sql
:name: sql-canton
:class: hidden
create table canton (
    nom text not null,
    abr text not null,
    chef_lieu text not null,
    nb_communes int not null,
    population int not null,
    superficie decimal(6,2) not null
);
insert into canton values
    ('Fribourg', 'FR', 'Fribourg', 126, 334465, 1670.7),
    ('Genève', 'GE', 'Genève', 45, 514114, 282.48),
    ('Berne', 'BE', 'Berne', 335, 1051437, 5959.44),
    ('Zurich', 'ZH', 'Zurich', 160, 1579967, 1729),
    ('Tessin', 'TI', 'Bellinzone', 106, 354023, 2812.2),
    ('Grison', 'GR', 'Coire', 101, 202538, 7105.44),
    ('Uri', 'UR', 'Altdorf', 19, 37317, 1076.57);
select * from canton;
```

## Exercice 1

<!-- TODO: Cacher les solutions pour que les élèves ne puissent pas y accéder
            pendant qu'ils font les exercices. -->

Indiquer ce qu'afficheront les requêtes suivantes:

1.  ```{code-block} sql
    select * from canton where nb_communes = 45;
    ```

<!--    ````{admonition} Solution
    :class: note dropdown
    ```{code-block} text
    Genève    GE    Genève      45        514114      282.48
    ```
    ````-->

2.  ```{code-block} sql
    select * from canton where chef_lieu = Coire;
    ```

<!--    ````{admonition} Solution
    :class: note dropdown
    Cette requête produira une erreur, car il manque les guillemets simples
    autour de Coire.
    ```` -->

3.  ```{code-block} sql
    select nom, superficie from canton where nom = 'Fribourg';
    ```

<!--    ````{admonition} Solution
    :class: note dropdown
    ```{code-block} text
    Fribourg    1670.7
    ```
    ````-->

4.  ```{code-block} sql
    select * from canton where population > 500000;
    ```

<!--    ````{admonition} Solution
    :class: note dropdown
    ```{code-block} text
    Genève    GE    Genève      45        514114      282.48
    Berne     BE    Berne       335       1051437     5959.44
    Zurich    ZH    Zurich      160       1579967     1729
    ```
    ````-->

5.  ```{code-block} sql
    select * from canton where abr < 'GR';
    ```

<!--    ````{admonition} Solution
    :class: note dropdown
    Les opérateurs de comparaison pour du texte utilisent l'ordre alphabétique.\
    Exemples: 'a' < 'b' ou 'p' > 'd'

    ```{code-block} text
    Fribourg  FR    Fribourg    126       334465      1670.7
    Genève    GE    Genève      45        514114      282.48
    Berne     BE    Berne       335       1051437     5959.44
    ```
    ````-->

6.  ```{code-block} sql
    select * from canton order by superficie asc;
    ```

<!--    ````{admonition} Solution
    :class: note dropdown
    ```{code-block} text
    Genève    GE    Genève      45        514114      282.48
    Uri       UR    Altdorf     19        37317       1076.57
    Fribourg  FR    Fribourg    126       334465      1670.7
    Zurich    ZH    Zurich      160       1579967     1729
    Tessin    TI    Bellinzone  106       354023      2812.2
    Berne     BE    Berne       335       1051437     5959.44
    Grison    GR    Coire       101       202538      7105.44

    ```
    ````-->

## Exercice 2

Créer et compléter la table **canton** avec des requêtes SQL. La table ne doit
pas accepter les valeurs `null`.\
Contrôler les réponses de l'exercice précédent.

```{code-block} sql
select * from canton order by superficie asc;
```


<!--````{admonition} Solution
:class: note dropdown
```{code-block} sql
create table canton (
  nom text not null,
  abr text not null,
  chef_lieu text not null,
  nb_communes text not null,
  population int not null,
  superficie decimal(6,2) not null
);

insert into canton values ('Fribourg', 'FR', 'Fribourg', 126, 334465, 1670.7);
insert into canton values ('Genève', 'GE', 'Genève', 45, 514114, 282.48);
insert into canton values ('Berne', 'BE', 'Berne', 335, 1051437, 5959.44);
insert into canton values ('Zurich', 'ZH', 'Zurich', 160, 1579967, 1729);
insert into canton values ('Tessin', 'TI', 'Bellinzone', 106, 354023, 2812.2);
insert into canton values ('Grison', 'GR', 'Coire', 101, 202538, 7105.44);
insert into canton values ('URI', 'UR', 'Altdorf', 19, 37317, 1076.57);

select * from canton order by superficie asc;
```
````-->

## Exercice 3

1. Écrire une requête SQL qui permet d'afficher toutes les colonnes du canton
dont le chef-lieu est Bellinzone.

<!--    ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select * from canton where chef_lieu = 'Bellinzone';
    ```
    ````-->

2. Écrire une requête SQL qui permet d'afficher toutes les colonnes des
cantons dont la population est inférieure à 300'000 habitants.

<!--    ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select * from canton where population < 300000;
    ```
    ````-->

3. Écrire une requête SQL qui permet d'afficher toutes les colonnes des
cantons dans l'ordre alphabétique des abréviations.

<!--    ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select * from canton order by abr asc;
    ```
    ````-->

4. Écrire une requête SQL qui permet d'afficher le nom, l'abréviation et le
chef-lieu des cantons.

<!--    ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select nom, abr, chef_lieu from canton;
    ```-->

5. Écrire une requête SQL qui permet d'afficher le nom, l'abréviation et le
chef-lieu des cantons ordonnés selon le nombre d'habitants du plus grand au plus
petit.

<!--    ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select nom, abr, chef_lieu from canton order by population desc;
    ```
    ````-->

6. Écrire une requête SQL qui permet d'afficher toutes les colonnes des cantons
qui ont plus de 100 communes et une population inférieure à 500'000 habitants.

<!--    ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select * from canton where nb_communes > 100 and population < 500000;
    ```
    ````-->

7. Écrire une requête SQL qui permet d'afficher toutes les colonnes des cantons
dont le chef-lieu est Altdorf ou le nombre de communes supérieur ou égal à 150.

<!--    ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select * from canton where chef_lieu = 'Altdorf' or nb_communes >= 150;
    ```
    ````-->

8. Écrire une requête SQL qui permet d'afficher le nom des cantons dont
l'abréviation n'est pas FR.

<!--    ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select nom from canton where abr <> 'FR';
    ```
    ````-->

9. Écrire une requête SQL qui permet d'afficher le nom et l'abréviation  des
cantons dont la population se trouvent entre 300'000 et 500'000 habitants.

<!--    ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select nom from canton where population between 300000 and 500000;
    ```
    ````-->

## Exercice 4

<!-- TODO: Ajout de la base de données contact.sql à télécharger pour les
            élèves. -->

Une application de rencontres demande, à l'enregistrement sur son site, les
informations suivantes: le nom, le prénom, l'adresse mail, le sexe,
la date de naissance, le statut, le lieu et les intérêts principaux.\
Les champs obligatoires sont le nom, le prénom, adresse mail, le sexe et la date
de naissance.

La table `contact` ressemble à cela:

```{exec} sql
:name: sql-contact
:class: hidden
create table contact (
    nom text not null,
    prenom text not null,
    email text not null,
    sexe text not null,
    anniversaire text not null,
    statut text,
    lieu text,
    code_postal text,
    interets text
);

insert into contact values ('Dupont', 'Bob', 'dupont.bob@glog.com', 'M', '1990-09-10', 'divorcé', 'Villars-sur-Glâne', '1752', 'Tennis, Animaux');
insert into contact values ('Martin', 'Anne', 'amartin@fri.ch', 'F', '1995-06-02', 'célibataire', 'Lausanne', '1000', 'Escape game');
insert into contact values ('Dunant', 'Martine', 'martine.dunant@google.com', 'F', '1985-12-24', 'séparé', 'Val d''Illiez', '1873', 'Lecture');
insert into contact values ('Schmidt', 'Léo', 'leo@cine.ch', 'M', '2000-01-01', 'célibataire', 'La Roche', '1634', 'Cinéma, Jeux de société');

select * from contact;
```

0. [Importer](#import) la base de données [contact.sql](./contact.sql) dans
VSCode.

1. Rechercher les adresses mail de toutes les personnes célibataires.

<!--    ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select email from contact where statut = 'célibataire';
    ```
    ````-->

2. Rechercher toutes les personnes qui habitent à Val-d'Illiez.

    ```{tip}
    Le guillemet simple est utilisé en SQL pour indiquer le début et la fin
    d'une chaîne de caractères. Si une chaîne de caractères contient une
    apostrophe (ou un guillemet simple), il faut doubler le guillemet pour que
    le logiciel comprenne que ce n'est pas la fin de la chaîne de caractères,
    mais une apostrophe.
    ```

<!--    ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select * from contact where lieu = 'Val-d''Illiez';
    ```
    ````-->

3. Recherche toutes les personnes qui habitent à Lausanne.

<!--    ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select * from contact where lieu = 'Lausanne';
    ```
    ````-->

4. Rechercher toutes les personnes qui habitent dans la région lausannoise (le
code postal doit commencer par 10..).

    ````{tip}
    Pour chercher des chaînes de caractères dans un mot, utiliser le mot
    réservé **like** et les caractères **%** pour remplacer plusieurs caractères ou
    **_** qui remplace un seul caractère.

    Pour trouver tous les contacts dont le prénom commence par Ma, utiliser
    ```{code-block} sql
    select * from contact where prenom like 'Ma%';
    ```

    Pour trouver toutes les Laure ou les Laura dans la liste de contacts, utiliser
    ```{code-block} sql
    select * from contact where prenom like 'Laur_';
    ```
    ````

<!--    ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select * from contact where code_postal like '10%';
    ```
    ````-->

5. Rechercher le nom, le prénom et la date de naissance de toutes les personnes
nées 1995.

<!--    ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select nom, prenom from contact where naissance like '1995-%';
    ```
    ````-->

6. Rechercher les contacts qui aiment le cinéma.

<!--    ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select * from contact where interets like '%Cinéma%';
    ```
    ````-->

7. Rechercher le nom, le prénom et la date de naissance de toutes les personnes
nées en juin.

<!--    ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select nom, prenom, naissance from contact where naissance like '%-06-%';
    ```
    ````-->

8. Rechercher tous les hommes qui sont célibataires et qui habitent dans la
région genevoise (12..).

<!--    ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select * from contact where sexe = 'M' and statut = 'célibateire'
        and code_postal like '12%';
    ```
    ````-->

9. Rechercher toutes les femmes qui sont divorcées et qui ont entre 30 et
40 ans.

<!--    ````{admonition} Solution
    :class: note dropdown
    ```{code-block} sql
    select * from contact where sexe = 'F' and statut = 'divorcé'
        and naissance between '1984-%' and '1994-%';
    ```
    ````-->


