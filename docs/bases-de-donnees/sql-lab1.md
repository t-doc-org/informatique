<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# SQL Lab 1

Le but de cette section est d'entraîner les concepts vus dans la section
[](./sql.md).

Voici la table **canton** contenant certaines informations sur des cantons
suisses.

```{exec} sql
:after: sql-canton
:class: hidden
:when: load
select * from canton;
```

## Exercice 1

<!-- TODO: Remettre les solutions après les labos. -->

Indiquer ce qu'afficheront les requêtes suivantes:

1.  ```{code-block} sql
    select * from canton where nb_communes = 45;
    ```

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{exec} sql
    :after: sql-canton
    select * from canton where nb_communes = 45;
    ```
    ```` -->

2.  ```{code-block} sql
    select * from canton where chef_lieu = Coire;
    ```

    <!-- ````{admonition} Solution
    :class: note dropdown
    Cette requête produira une erreur, car il manque les guillemets simples
    autour de Coire.
    ```{exec} sql
    :after: sql-canton
    select * from canton where chef_lieu = Coire;
    ```
    ```` -->

3.  ```{code-block} sql
    select nom, superficie from canton where nom = 'Fribourg';
    ```

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{exec} sql
    :after: sql-canton
    select nom, superficie from canton where nom = 'Fribourg';
    ```
    ```` -->

4.  ```{code-block} sql
    select * from canton where population > 500000;
    ```

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{exec} sql
    :after: sql-canton
    select * from canton where population > 500000;
    ```
    ```` -->

5.  ```{code-block} sql
    select * from canton where abr < 'GR';
    ```

<!--
    ````{admonition} Solution
    :class: note dropdown
    Les opérateurs de comparaison pour du texte utilisent l'ordre alphabétique.\
    Exemples: 'a' < 'b' ou 'p' > 'd'

    ```{exec} sql
    :after: sql-canton
    select * from canton where abr < 'GR';
    ```
    ````
-->


6.  ```{code-block} sql
    select * from canton order by superficie asc;
    ```

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{exec} sql
    :after: sql-canton
    select * from canton order by superficie asc;
    ```
    ```` -->

## Exercice 2

Créer et compléter la table **canton** avec des requêtes SQL. La table ne doit
pas accepter les valeurs `null`.\
Contrôler les réponses de l'exercice précédent.

````{admonition} Solution
:class: note dropdown
```{exec} sql
:name: sql-canton
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
````

## Exercice 3

1. Écrire une requête SQL qui permet d'afficher toutes les colonnes du canton
dont le chef-lieu est Bellinzone.

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{exec} sql
    :after: sql-canton
    select * from canton where chef_lieu = 'Bellinzone';
    ```
    ```` -->

2. Écrire une requête SQL qui permet d'afficher toutes les colonnes des
cantons dont la population est inférieure à 300'000 habitants.

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{exec} sql
    :after: sql-canton
    select * from canton where population < 300000;
    ```
    ```` -->

3. Écrire une requête SQL qui permet d'afficher toutes les colonnes des
cantons dans l'ordre alphabétique des abréviations.

     <!-- ````{admonition} Solution
    :class: note dropdown
    ```{exec} sql
    :after: sql-canton
    select * from canton order by abr asc;
    ```
    ```` -->

4. Écrire une requête SQL qui permet d'afficher le nom, l'abréviation et le
chef-lieu des cantons.

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{exec} sql
    :after: sql-canton
    select nom, abr, chef_lieu from canton;
    ```-->

5. Écrire une requête SQL qui permet d'afficher le nom, l'abréviation et le
chef-lieu des cantons ordonnés selon le nombre d'habitants du plus grand au plus
petit.

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{exec} sql
    :after: sql-canton
    select nom, abr, chef_lieu from canton order by population desc;
    ```
    ```` -->

6. Écrire une requête SQL qui permet d'afficher toutes les colonnes des cantons
qui ont plus de 100 communes et une population inférieure à 500'000 habitants.

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{exec} sql
    :after: sql-canton
    select * from canton where nb_communes > 100 and population < 500000;
    ```
    ```` -->

7. Écrire une requête SQL qui permet d'afficher toutes les colonnes des cantons
dont le chef-lieu est Altdorf ou le nombre de communes supérieur ou égal à 150.

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{exec} sql
    :after: sql-canton
    select * from canton where chef_lieu = 'Altdorf' or nb_communes >= 150;
    ```
    ```` -->

8. Écrire une requête SQL qui permet d'afficher le nom des cantons dont
l'abréviation n'est pas FR.

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{exec} sql
    :after: sql-canton
    select nom from canton where abr <> 'FR';
    ```
    ```` -->

9. Écrire une requête SQL qui permet d'afficher le nom et l'abréviation  des
cantons dont la population se trouvent entre 300'000 et 500'000 habitants.

    <!-- ````{admonition} Solution
    :class: note dropdown
    ```{exec} sql
    :after: sql-canton
    select nom from canton where population between 300000 and 500000;
    ```
    ```` -->

## Exercice 4

Une application de rencontres demande, à l'enregistrement sur son site, les
informations suivantes: le nom, le prénom, l'adresse mail, le sexe,
la date de naissance, le statut, le lieu et les intérêts principaux.\
Les champs obligatoires sont le nom, le prénom, adresse mail, le sexe et la date
de naissance.

La table `contact` ressemble à cela:

```{exec} sql
:name: sql-exemple-contact
:class: hidden
:when: load
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

<!-- TODO:  importer la bd directement depuis le fichier contact.sql. -->

```{exec} sql
:name: sql-contact
:when: never
:class: hidden
create table contact (
    nom text not null,
    prenom text not null,
    email text not null,
    sexe char(1) not null,
    naissance date,
    statut text,
    lieu text,
    code_postal char(4),
    interets text
);

insert into contact values
    ('Dupont', 'Bob', 'dupont.bob@glog.com', 'M', '1990-09-10', 'divorcé', 'Villars-sur-Glâne', '1752', 'Tennis, Animaux'),
    ('Martin', 'Anne', 'amartin@fri.ch', 'F', '1995-06-02', 'célibataire', 'Lausanne', '1000', 'Escape game'),
    ('Dunant', 'Martine', 'martine.dunant@google.com', 'F', '1985-12-24', 'séparé', 'Val-d''Illiez', '1873', 'Lecture'),
    ('Schmidt', 'Léo', 'leo@cine.ch', 'M', '2000-01-01', 'célibataire', 'La Roche', '1634', 'Cinéma, Jeux de société'),

    ('Dupont', 'Jean', 'jean.dpt85@swissmail.ch', 'M', '1985-06-15', 'célibataire', 'Genève', '1201', 'Sports, Musique'),
    ('Dubois', 'Marie', 'm.dubois_lovesreading@romandie.com', 'F', '1992-03-22', 'séparé', 'Lausanne', '1000', 'Lecture, Voyage'),
    ('Martin', 'Luc', 'lmartin.rando@helvetia.org', 'M', '2001-11-02', 'célibataire', 'Neuchâtel', '2000', 'Cuisine, Randonnée'),
    ('Lefevre', 'Sophie', 's.lefevre.art@photochic.ch', 'F', '1989-08-30', 'divorcé', 'Fribourg', '1700', 'Photographie, Art'),
    ('Roux', 'Pierre', 'pieroux.musicfan@playmail.ch', 'M', '1995-12-10', 'célibataire', 'Yverdon-les-Bains', '1400', 'Cinéma, Musique'),

    ('Moreau', 'Laura', 'laura.moreau_travel@swissmail.ch', 'F', '1981-04-11', 'séparé', 'Vevey', '1800', 'Voyage, Cuisine'),
    ('Simon', 'David', 'dsimon.techgeek@romandie.com', 'M', '1990-09-18', 'célibataire', 'Nyon', '1260', 'Sports, Technologie'),
    ('Blanc', 'Emilie', 'emilie_blanc.art@postnet.ch', 'F', '1986-07-24', null, 'Montreux', '1820', 'Musique, Art'),
    ('Gauthier', 'Antoine', 'antoine.g.photo@helvetia.org', 'M', '1993-01-14', 'célibataire', 'Bulle', '1630', 'Randonnée, Photographie'),
    ('Garcia', 'Elena', 'elena.garcia_cooking@genmail.ch', 'F', '1982-05-05', 'séparé', 'Sion', '1950', 'Cuisine, Lecture'),

    ('Lambert', 'Lucas', 'lucas_lambert.moviebuff@swissmail.ch', 'M', '1988-10-23', 'célibataire', 'Morges', '1110', 'Cinéma, Sports'),
    ('Lemoine', 'Julie', 'julie_traveller@romandie.com', 'F', '1991-02-17', 'En couple', null, null, 'Voyage, Cinéma'),
    ('Duval', 'Alexandre', 'aduval_tech@postnet.ch', 'M', '1983-03-30', 'séparé', 'Payerne', '1530', 'Technologie, Cuisine'),
    ('Leroux', 'Claire', 'claire.leroux_artistic@swissmail.ch', 'F', '1996-06-29', 'célibataire', null, null, 'Lecture, Art'),
    ('Giraud', 'Thomas', 'thomas_giraud@playmail.ch', 'M', '1987-12-01', 'célibataire', 'La Chaux-de-Fonds', '2300', 'Sports, Musique'),

    ('Perrin', 'Manon', 'manon.perrin_photo@romandie.com', 'F', '1990-07-13', 'séparé', 'Carouge', '1227', 'Photographie, Voyage'),
    ('Renaud', 'Nicolas', 'n.renaud_films@genmail.ch', 'M', '1979-11-25', 'célibataire', 'Meyrin', '1217', 'Technologie, Cinéma'),
    ('Mercier', 'Isabelle', 'isabelle_cooking_music@swissmail.ch', 'F', '1984-05-18', 'divorcé', 'Chavannes-près-Renens', '1022', 'Cuisine, Musique'),
    ('Chevalier', 'Vincent', 'vincent.chevalier.sport@playmail.ch', 'M', '1995-04-07', 'célibataire', 'Renens', '1020', null),
    ('Barbier', 'Camille', 'camille.barbier_art@helvetia.org', 'F', '1987-10-19', 'séparé', 'Onex', '1213', 'Lecture, Art'),

    ('Rousseau', 'Adrien', 'adrien.r_travel@romandie.com', 'M', '1992-03-12', 'divorcé', 'Versoix', '1290', 'Photographie, Voyage'),
    ('Leclerc', 'Sarah', 'sarah_leclerc@helvetia.org', 'F', '1980-06-02', 'séparé', 'Thônex', '1226', 'Musique, Lecture'),
    ('Faure', 'Guillaume', 'guillaume_faure.tech@genmail.ch', 'M', '1986-11-15', 'célibataire', 'Vernier', '1214', 'Technologie, Sports'),
    ('Royer', 'Alice', 'alice_r.artistic@romandie.com', 'F', '1991-08-27', 'célibataire', 'Plan-les-Ouates', '1228', 'Art, Photographie'),
    ('Pichon', 'Benoit', 'benoit.pichon_music@swissmail.ch', 'M', '1985-09-06', 'séparé', 'Pregny-Chambésy', '1292','Voyage, Musique'),

    ('Noel', 'Julien', 'julien_noel_athlete@helvetia.org', 'M', '1993-12-24', 'célibataire', 'Vésenaz', '1222', 'Sports, Cinéma'),
    ('Aubry', 'Pauline', 'pauline.aubry_cooking@playmail.ch', 'F', '1988-04-09', 'séparé', 'Collonge-Bellerive', '1254', 'Cuisine, Lecture'),
    ('Jacquet', 'François', 'f.jacquet.versoix@swissmail.ch', 'M', '2004-09-19', 'célibataire', 'Versoix', '1290', 'Technologie, Voyage'),
    ('Marchand', 'Valérie', 'valerie_m.art@romandie.com', 'F', '1990-02-25', null, 'Carouge', '1227', 'Musique, Art'),
    ('Muller', 'Philippe', 'philippe.muller_photo@genmail.ch', 'M', '1984-10-11', 'séparé', 'Nyon', '1260', null),

    ('Lemoine', 'Nathalie', 'nathalie.lemoine_trek@helvetia.org', 'F', '2001-05-30', 'séparé', 'Sion', '1950', 'Voyage, Randonnée'),
    ('Collin', 'Laurent', 'laurent.collin.movies@postnet.ch', 'M', '1995-07-14', 'célibataire', 'Sierre', '3960', 'Technologie, Cinéma'),
    ('Brunet', 'Camille', 'camille.brunet_food@swissmail.ch', 'F', '1987-08-07', 'célibataire', 'Fribourg', '1700', 'Lecture, Cuisine'),
    ('Girard', 'Mathieu', 'mathieu_g.music@playmail.ch', 'M', '1982-12-30', 'célibataire', 'Monthey', '1870', 'Musique, Art'),
    ('Bourdon', 'Elodie', 'elodie_b.photo@romandie.com', 'F', '1990-06-18', 'séparé', 'Vevey', '1800', 'Photographie, Randonnée'),

    ('Renaud', 'Aurélien', 'aurelien_renaud_sport@swissmail.ch', 'M', '1989-01-13', 'célibataire', 'Lausanne', '1000', 'Voyage, Sports'),
    ('Germain', 'Laure', 'laure_g.art@genmail.ch', 'F', '1994-11-20', 'célibataire', 'Yverdon-les-Bains', '1400', null),
    ('Perrier', 'Quentin', 'quentin.perrier_music@romandie.com', 'M', '1993-03-01', 'séparé', 'Neuchâtel', '2000', 'Technologie, Musique'),
    ('Robin', 'Chloé', 'chloe.robin.cooking@postnet.ch', 'F', '1985-07-29', 'célibataire', 'Genève', '1201', 'Cuisine, Photographie'),
    ('Lemoine', 'Jérôme', 'jerome.lemoine.trek@swissmail.ch', 'M', '1986-02-22', 'séparé', 'Nyon', '1260', 'Randonnée, Voyage'),

    ('Renard', 'Catherine', 'catherine.renard_books@romandie.com', 'F', '1990-09-05', 'divorcé', 'La Chaux-de-Fonds', '2300', 'Art, Lecture'),
    ('Durand', 'Victor', 'victor_durand.movies@swissmail.ch', 'M', '1997-01-17', 'divorcé', 'Martigny', '1920', 'Sports, Cinéma'),
    ('Lemoine', 'Thomas', 'thomas.lemoine.tech@genmail.ch', 'M', '1984-11-03', 'célibataire', 'Fribourg', '1700', 'Musique, Technologie'),
    ('Bernard', 'Claire', 'claire.bernard.photo@romandie.com', 'F', '1992-04-16', 'séparé', null, null, 'Voyage, Photographie'),
    ('Petit', 'Julie', 'julie.petit.books@postnet.ch', 'F', '1983-08-26', null, 'Sion', '1950', 'Lecture, Randonnée');
    select * from contact;
```

0. [Importer](#import) la base de données [contact.sql](./contact.sql) dans
VSCode.

<!-- TODO: Enlever le :class: hidden après les labos. -->

1. Rechercher les adresses mail de toutes les personnes célibataires.

    ````{admonition} Solution
    :class: note dropdown
    Ce que vous devez obtenir comme résultat.
    ```{exec} sql
    :when: load
    :class: hidden
    :after: sql-contact
    select email from contact where statut = 'célibataire';
    ```
    ````


2. Rechercher toutes les personnes qui habitent à Val-d'Illiez.

    ```{tip}
    Le guillemet simple est utilisé en SQL pour indiquer le début et la fin
    d'une chaîne de caractères. Si une chaîne de caractères contient une
    apostrophe (ou un guillemet simple), il faut doubler le guillemet pour que
    le logiciel comprenne que ce n'est pas la fin de la chaîne de caractères,
    mais une apostrophe.
    ```

    ````{admonition} Solution
    :class: note dropdown
    ```{exec} sql
    :after: sql-contact
    :when: load
    :class: hidden
    select * from contact where lieu = 'Val-d''Illiez';
    ```
    ````

3. Recherche toutes les personnes qui habitent à Lausanne.

    ````{admonition} Solution
    :class: note dropdown
    ```{exec} sql
    :after: sql-contact
    :when: load
    :class: hidden
    select * from contact where lieu = 'Lausanne';
    ```
    ````

4. Rechercher toutes les personnes qui habitent dans la région lausannoise (le
code postal doit commencer par 10..).

    ````{tip}
    Pour chercher des chaînes de caractères dans un mot, utiliser le mot
    réservé **like** et les caractères **%** pour remplacer plusieurs caractères ou
    **_** qui remplace un seul caractère.

    Pour trouver tous les contacts dont le prénom commence par Ma, utiliser
    ```{exec} sql
    :after: sql-contact
    select * from contact where prenom like 'Ma%';
    ```

    Pour trouver toutes les Laure ou les Laura dans la liste de contacts, utiliser
    ```{exec} sql
    :after: sql-contact
    select * from contact where prenom like 'Laur_';
    ```
    ````

    ````{admonition} Solution
    :class: note dropdown
    ```{exec} sql
    :after: sql-contact
    :when: load
    :class: hidden
    select * from contact where code_postal like '10%';
    ```
    ````

5. Rechercher le nom, le prénom et la date de naissance de toutes les personnes
nées 1995.

    ````{admonition} Solution
    :class: note dropdown
    ```{exec} sql
    :after: sql-contact
    :when: load
    :class: hidden
    select nom, prenom from contact where naissance like '1995-%';
    ```
    ````

6. Rechercher les contacts qui aiment le cinéma.

    ````{admonition} Solution
    :class: note dropdown
    ```{exec} sql
    :after: sql-contact
    :when: load
    :class: hidden
    select * from contact where interets like '%Cinéma%';
    ```
    ````

7. Rechercher le nom, le prénom et la date de naissance de toutes les personnes
nées en juin.

    ````{admonition} Solution
    :class: note dropdown
    ```{exec} sql
    :after: sql-contact
    :when: load
    :class: hidden
    select nom, prenom, naissance from contact where naissance like '%-06-%';
    ```
    ````

8. Rechercher tous les hommes qui sont célibataires et qui habitent dans la
région genevoise (12..).

    ````{admonition} Solution
    :class: note dropdown
    ```{exec} sql
    :after: sql-contact
    :when: load
    :class: hidden
    select * from contact where sexe = 'M' and statut = 'célibataire'
        and code_postal like '12%';
    ```
    ````

9. Rechercher toutes les femmes qui sont divorcées et qui ont entre 30 et
40 ans.

    ````{admonition} Solution
    :class: note dropdown
    ```{exec} sql
    :after: sql-contact
    :when: load
    :class: hidden
    select * from contact where sexe = 'F' and statut = 'divorcé'
        and naissance between '1984-%' and '1994-%';
    ```
    ````
