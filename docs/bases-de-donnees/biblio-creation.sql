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
