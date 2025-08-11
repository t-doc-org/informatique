% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
solutions: dynamic
```

# SQL Lab 1

Le but de cette section est d'entraîner les concepts vus dans la section
[](sql.md).

Voici la table `canton` contenant certaines informations de différents cantons
suisses.

```{exec} sql
:after: sql-canton
:class: hidden
:when: load
select * from canton;
```

## Exercice {nump}`exercice`

Indiquer ce qu'afficheront les requêtes suivantes:

1.  ```{exec} sql
    :after: sql-canton
    select * from canton where nb_communes = 45;
    ```

2.  ```{exec} sql
    :after: sql-canton
    select * from canton where chef_lieu = Coire;
    ```

    ````{solution} Explication
    Cette requête produit une erreur, car il manque les guillemets simples
    autour de Coire.
    ````

3.  ```{exec} sql
    :after: sql-canton
    select nom, superficie from canton where nom = 'Fribourg';
    ```

4.  ```{exec} sql
    :after: sql-canton
    select * from canton where population > 500000;
    ```

5.  ```{exec} sql
    :after: sql-canton
    select * from canton where abr < 'GR';
    ```

    ````{solution} Explication
    Les opérateurs de comparaison pour du texte utilisent l'ordre alphabétique.\
    Exemples: 'a' < 'b' ou 'p' > 'd'
    ````

6.  ```{exec} sql
    :after: sql-canton
    select * from canton order by superficie asc;
    ```

## Exercice {nump}`exercice`

Voici à nouveau la table `canton`.

```{exec} sql
:after: sql-canton
:class: hidden
:when: load
select * from canton;
```

Créer et compléter la table `canton` avec des requêtes SQL. La table ne doit
pas accepter les valeurs `null`.

```{exec} sql
:then: sql-canton-select
:editor: e9b14e12-14fc-4725-930f-011f19914760
```

```{exec} sql
:name: sql-canton-select
:class: hidden
:when: never
select * from canton;
```

````{solution}
```{exec} sql
:name: sql-canton
:then: sql-canton-select
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
```
````

## Exercice {nump}`exercice`

1.  Écrire une requête SQL qui retourne toutes les colonnes du canton dont le
    chef-lieu est Bellinzone.

    ```{exec} sql
    :after: sql-canton
    :editor: 5e6516e0-18bb-4d38-8c90-767e1fd1f729
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-canton
    select * from canton where chef_lieu = 'Bellinzone';
    ```
    ````

2.  Écrire une requête SQL qui retourne toutes les colonnes des cantons dont la
    population est inférieure à 300'000 habitants.

    ```{exec} sql
    :after: sql-canton
    :editor: 57e619f9-cc9e-47d6-9cf5-a510f74465df
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-canton
    select * from canton where population < 300000;
    ```
    ````

3.  Écrire une requête SQL qui retourne toutes les colonnes des cantons dans
    l'ordre alphabétique des abréviations.

    ```{exec} sql
    :after: sql-canton
    :editor: e584473c-6e0d-41ca-bad5-b7f1888eae10
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-canton
    select * from canton order by abr asc;
    ```
    ````

4.  Écrire une requête SQL qui retourne le nom, l'abréviation et le chef-lieu
    des cantons.

    ```{exec} sql
    :after: sql-canton
    :editor: caf9b02f-d802-4876-a1ad-0b183c6bdc41
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-canton
    select nom, abr, chef_lieu from canton;
    ```

5.  Écrire une requête SQL qui retourne le nom, l'abréviation et le chef-lieu
    des cantons ordonnés selon le nombre d'habitants du plus grand au plus
    petit.

    ```{exec} sql
    :after: sql-canton
    :editor: 591d0ad5-71f4-4f8c-9281-f2639abe7a2e
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-canton
    select nom, abr, chef_lieu from canton order by population desc;
    ```
    ````

6.  Écrire une requête SQL qui retourne toutes les colonnes des cantons qui ont
    plus de 100 communes et une population inférieure à 500'000 habitants.

    ```{exec} sql
    :after: sql-canton
    :editor: 5dc7f7ee-caa7-439c-90a6-c636d8e15551
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-canton
    select * from canton where nb_communes > 100 and population < 500000;
    ```
    ````

7.  Écrire une requête SQL qui retourne toutes les colonnes des cantons dont le
    chef-lieu est Altdorf ou le nombre de communes supérieur ou égal à 150.

    ```{exec} sql
    :after: sql-canton
    :editor: 80d34995-7472-4051-a8af-577363ee3858
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-canton
    select * from canton where chef_lieu = 'Altdorf' or nb_communes >= 150;
    ```
    ````

8.  Écrire une requête SQL qui retourne le nom des cantons dont l'abréviation
    n'est pas FR.

    ```{exec} sql
    :after: sql-canton
    :editor: cfa9c7e3-cead-4b27-9405-3644a1b27335
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-canton
    select nom from canton where abr <> 'FR';
    ```
    ````

9.  Écrire une requête SQL qui retourne le nom et l'abréviation des cantons dont
    la population se trouve entre 300'000 et 500'000 habitants.

    ```{exec} sql
    :after: sql-canton
    :editor: 931ab749-fafb-4d51-b65f-c0c6aedd893a
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-canton
    select nom, abr from canton where population between 300000 and 500000;
    ```
    ````

## Exercice {nump}`exercice:bd-lab1-pays`

Voici le code d'une base de données qui contient des informations sur différents
pays.

```{exec} sql
:name: sql-pays
:when: never
create table pays (
  nom text not null,
  abr text not null,
  prefixe text not null,
  capitale text not null,
  population int not null,
  nourriture text
);
insert into pays values
  ('Suisse', 'CH', '+41', 'Zurich', 8776000, 'fondue'),
  ('France', 'FR', '+33', 'Paris', 67970000, null),
  ('Allemagne', 'AL', '+49', 'Berlin', 83800000, null),
  ('Italie', 'IT', '+39', 'Rome', 58940000, null),
  ('Autriche', 'AT', '+43', 'Vienne', 9042000, 'Kaiserschmarrn'),
  ('Yougoslavie', 'YU', '+38', 'Belgrade', 10656929, null),
  ('Lichtenstein', 'LI', '+423', 'Vaduz', 39327, null);
```

```{exec} sql
:name: sql-pays-select
:class: hidden
:when: never
select * from pays;
```

1.  Afficher le contenu de la table `pays`.

    ```{exec} sql
    :after: sql-pays
    :editor: bcaf5478-a98e-4604-94ed-25c68d55d0ec
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-pays
    select * from pays;
    ```
    ````

2.  La Yougoslavie n'existe plus depuis de nombreuses années. Supprimer cette
    ligne.

    ```{exec} sql
    :after: sql-pays
    :then: sql-pays-select
    :editor: 5b17366a-b154-4efa-ab9d-8ed38cc2aba5
    ```

    ````{solution}
    ```{exec} sql
    :name: sql-pays-delete
    :after: sql-pays
    :then: sql-pays-select
    delete from pays where nom = 'Yougoslavie';
    ```
    ````

3.  Corriger les deux erreurs qui se sont produites lors de la création de la
    base de donnée.
    - La capitale de la Suisse n'est pas Zurich.
    - L'abréviation de l'allemagne n'est pas **AL**, mais **DE**.

    ```{exec} sql
    :after: sql-pays-delete
    :then: sql-pays-select
    :editor: fe2e31ac-65cd-4c3b-aff5-fbe2a440ccaa
    ```

    ````{solution}
    ```{exec} sql
    :name: sql-pays-update
    :after: sql-pays-delete
    :then: sql-pays-select
    update pays set capitale = 'Berne' where nom = 'Suisse';
    update pays set abr = 'DE' where nom = 'Allemagne';
    ```
    ````

4.  Compléter la colonne nourriture par un plat connu pour la France et pour
    l'Italie.

    ```{exec} sql
    :after: sql-pays-update
    :then: sql-pays-select
    :editor: ac5b265f-c615-4075-b8e0-cfb48044e4e9
    ```

    ````{solution}
    ```{exec} sql
    :name: sql-pays-last
    :after: sql-pays-update
    :then: sql-pays-select
    update pays set nourriture = 'escargots' where nom = 'France';
    update pays set nourriture = 'pizza' where nom = 'Italie';
    ```
    ````

## Exercice {nump}`exercice`

Une application de rencontres demande, à l'enregistrement sur son site, les
informations suivantes: le nom, le prénom, l'email, le sexe,
la date de naissance, le statut, le lieu et les intérêts principaux.\
Les champs obligatoires sont le nom, le prénom, l'adresse mail, le sexe et la
date de naissance.

La table `contact` ressemble à cela:

```{exec} sql
:after: sql-contact
:class: hidden
:when: load
select * from contact limit 4;
```

```{exec} sql
:name: sql-contact
:include: contact.sql
:when: never
:class: hidden
```

1.  Rechercher l'email de toutes les personnes célibataires.

    ```{exec} sql
    :after: sql-contact
    :editor: 42ecaa2e-9771-490f-80f7-570a7d07bc04
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-contact
    select email from contact where statut = 'célibataire';
    ```
    ````

2.  Recherche toutes les personnes qui habitent à Lausanne.

    ```{exec} sql
    :after: sql-contact
    :editor: 947069b0-1deb-41b0-b825-c6b7193c4961
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-contact
    select * from contact where lieu = 'Lausanne';
    ```
    ````

3.  Rechercher toutes les personnes qui habitent à Val-d'Illiez.

    ```{tip}
    Le guillemet simple est utilisé en SQL pour indiquer le début et la fin
    d'une chaîne de caractères. Si une chaîne de caractères contient une
    apostrophe (ou un guillemet simple), il faut doubler le guillemet pour
    indiquer que ce n'est pas la fin de la chaîne de caractères, mais une
    apostrophe.
    ```

    ```{exec} sql
    :after: sql-contact
    :editor: 88542989-771f-4006-a767-e26463d78990
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-contact
    select * from contact where lieu = 'Val-d''Illiez';
    ```
    ````

4.  Rechercher toutes les personnes qui habitent dans la région lausannoise (le
    code postal doit commencer par 10..).

    ```{exec} sql
    :after: sql-contact
    :editor: 22d2f5a7-59dd-4dd5-91ce-5e6486f42f1c
    ```

    ````{tip}
    Pour chercher des chaînes de caractères dans un mot, utiliser le mot
    réservé `like` et les caractères `%` pour remplacer plusieurs caractères
    ou `_` qui remplace un seul caractère.

    Pour trouver tous les contacts dont le prénom commence par Ma, utiliser:
    ```{exec} sql
    :after: sql-contact
    select * from contact where prenom like 'Ma%';
    ```

    Pour trouver toutes les Laur**e** ou les Laur**a** dans la liste de
    contacts, utiliser:

    ```{exec} sql
    :after: sql-contact
    select * from contact where prenom like 'Laur_';
    ```
    ````

    ````{solution}
    ```{exec} sql
    :after: sql-contact
    select * from contact where code_postal like '10%';
    ```
    ````

5.  Rechercher le nom, le prénom et la date de naissance de toutes les personnes
    nées en 1995.

    ```{exec} sql
    :after: sql-contact
    :editor: ac361196-2c33-4bc1-abd6-6a2d32c50983
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-contact
    select nom, prenom, naissance from contact where naissance like '1995-%';
    ```
    ````

6.  Rechercher les contacts qui aiment le cinéma.

    ```{exec} sql
    :after: sql-contact
    :editor: 9925d041-a080-4cdc-8333-b6fd8b3661e3
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-contact
    select * from contact where interets like '%Cinéma%';
    ```
    ````

7.  Rechercher le nom, le prénom et la date de naissance de toutes les personnes
    nées en juin.

    ```{exec} sql
    :after: sql-contact
    :editor: 443ec60f-b656-4a3c-b163-e43cc0874d48
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-contact
    select nom, prenom, naissance from contact where naissance like '%-06-%';
    ```
    ````

8.  Rechercher tous les hommes qui sont célibataires et qui habitent dans la
    région genevoise (12..).

    ```{exec} sql
    :after: sql-contact
    :editor: 5233a1af-688a-402a-b172-dc9925814181
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-contact
    select * from contact
      where sexe = 'M' and statut = 'célibataire'
      and code_postal like '12%';
    ```
    ````

9.  Rechercher toutes les femmes qui sont divorcées et qui sont nées entre 1984
    et 1994.

    ```{exec} sql
    :after: sql-contact
    :editor: 05a9de22-d729-4d16-8168-7d9023456ae7
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-contact
    select * from contact
      where sexe = 'F' and statut = 'divorcé'
      and naissance between '1984-%' and '1994-%';
    ```
    ````

## Exercice {nump}`exercice` (facultatif)

Reprenons la base de données des pays de
l'{numref}`exercice %s<exercice:bd-lab1-pays>`.

1.  Ajouter une colonne `monnaie`. Pour cela, il faut utiliser l'instruction
    `alter table`. Rechercher sur le Web comment faire.

    ```{tip}
    Utiliser une valeur par défaut pour la colonne `monnaie`.
    ```

    ```{exec} sql
    :after: sql-pays-last
    :then: sql-pays-select
    :editor: 07d2ec39-ce18-4732-bd48-e886daaaadcc
    ```

    ````{solution}
    ```{exec} sql
    :name: sql-pays-6-1
    :after: sql-pays-last
    :then: sql-pays-select
    alter table pays add monnaie text default 'euro';
    ```
    ````

2.  Compléter cette nouvelle colonne pour chaque pays.

    ```{exec} sql
    :after: sql-pays-6-1
    :then: sql-pays-select
    :editor: a0f3cddc-3c4a-40ef-b5e2-277120730137
    ```

    ````{solution}
    ```{exec} sql
    :name: sql-pays-6-2
    :after: sql-pays-6-1
    :then: sql-pays-select
    update pays set monnaie = 'franc suisse' where nom = 'Suisse';
    update pays set monnaie = 'couronne' where nom = 'Lichtenstein';
    ```
    ````

3.  Supprimer la colonne `nourriture`.

    ```{exec} sql
    :after: sql-pays-6-2
    :then: sql-pays-select
    :editor: 24ceda93-97c4-4f78-b6c5-1c543a856ccd
    ```

    ````{solution}
    ```{exec} sql
    :after: sql-pays-6-2
    :then: sql-pays-select
    alter table pays drop column nourriture;
    ```
