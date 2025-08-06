% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Stockage et transmission de données

## Volumes de données

L'information traitée par un ordinateur (texte, image, son, vidéo) est sous
forme de données binaires, c'est-à-dire sous la forme d'une suite de 0 ou de 1.
Le **bit** vient de BInary digiT (b minuscule dans les notations) est l'unité la
plus simple en informatique, représenté par le chiffre 0 ou 1.

L'**octet**, en anglais byte, (o minuscule ou B majuscule dans les notations)
est une unité composée de 8 bits. Pour faciliter la lisibilité, nous regroupons
en général l'information par paquet de 8, 16, 32 ou 64 bits.

Voici les unités standardisées depuis 1998:

| Unité | Valeur en octets | Valeur en puissance de 10 |
|-------|------------------|---------------------------|
| Un **kilooctet** (ko ou kB) | 1 000 octets | $10^3$ octets |
| Un **megaoctet** (Mo ou MB) | 1 000 ko | 1 000 000 octets = $10^6$ octets |
| Un **gigaoctet** (Go ou GB) | 1 000 Mo | 1 000 000 000 octets = $10^9$ octets |
| Un **téraoctet** (To ou TB) | 1 000 Go | 1 000 000 000 000 octets = $10^{12}$ octets |


### Ordre de grandeur

| Type | taille |
| :--- | :----- |
| Un fichier texte | 50 ko |
| Une image pour le web | 30 ko |
| Une musique (mp3) | 4 Mo |
| Une photo | 6 Mo |
| Un film | 700 Mo à 2 Go |
| Un CD | 700 Mo |
| Un DVD | 4.7 Go |
| Un Blu-ray | 25 Go |
| Une clé USB | 8 Go à 256 Go |
| Un disque dur | 500 Go à 7 To |

### Exercice {num2}`exercice`

Associez à chaque type de fichier un ordre de grandeur de volume de stockage.

```{role} select(quiz-select)
:right:
:options: |
: quelques ko
: quelques Mo
: quelques centaines de Mo
: plusieurs Go
: plusieurs To
```

```{quiz}
1.  {select}`quelques centaines de Mo`
    Une vidéo de basse qualité de quelques minutes
2.  {select}`plusieurs Go`
    Un film ou un gros jeu vidéo
3.  {select}`quelques Mo`
    Un fichier image ou audio mp3
4.  {select}`plusieurs To`
    Un film 4K non compressé, en studio
5.  {select}`quelques ko`
    Un document texte sans image ni formatage
```

### Exercice {num2}`exercice`

```{role} input(quiz-input)
:right: width: 10rem;
```

```{quiz}
1.  {input}`16000000000`
    Quelle est la taille en octets d'une clé USB de 16 Go?
2.  {input}`4000`
    Combien de fichier MP3 de 4 Mo en moyenne peut-on stocker sur une clé USB de
    16 Go?
```

## Débit

Le **débit** d'une transmission de données est la vitesse à laquelle les données
sont transmises sur le réseau. Il est exprimé en kb/s (kilobits par seconde) ou
Mb/s (Megabits par seconde).

### Exercice {num2}`exercice`

```{quiz}
1.  {input}`180`
    Pendant une vidéo live de deux minutes avec un débit de 1,5 Mo/s, quelle
    quantité de données sont transmises (en Mo)?
2.  Dans les années 90, la plupart des foyers se connectaient à Internet avec
    des « modems 56 k », qui avaient un débit théorique maximum de 56 kb/s.

    {input}`5`
    Combien de temps fallait-il pour télécharger une photo de 2.1 Mo (en
    minutes)?
```

Allez sur le site [https://www.speedtest.net](https://www.speedtest.net) et
mesurez le débit de votre connexion internet.
