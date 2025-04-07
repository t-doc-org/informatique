% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
hide-solutions: true
scripts:
  - src: quizz-helpers.js
```

# Compression

La compression sert à minimiser la taille d'un fichier pour limiter son poids et
permettre une transmission plus rapide, un temps de téléchargement ou un espace
de stockage réduit, tout en conservant au maximum sa qualité.

On distingue deux catégories principales de compression:

- **La compression sans perte:** Les données obtenues après décompression
  correspondent exactement aux données de départ.
- **La compression avec perte:** Les données obtenues après décompression
  présentent de légères différences par rapport aux données originales.

## Images

Il existe beaucoup de formats d'image différents. Certains permettent une
compression.

- Le format **GIF** (Graphicx Interchange Format) et le format **PNG** (Portable
  Network Graphics) sont des formats d'images compressées sans perte.

- Le format **JPG** (Joint Photographic Experts Group) est un format compressé
  avec perte pour les photos. La compression introduit des artefacts qui
  deviennent visibles lorsqu'elle est trop forte.

### Exemple {num}`ex-donnees`

En première année, vous avez vu comment encoder une image matricielle en noir et
blanc. Chaque pixel est représenté par un seul bit:\
0 pour un pixel blanc,\
1 pour un pixel noir.

Voici un exemple de fichier PBM (Portable BitMap):

```{code-block} text
P1
40 35
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 1 1 1 1 1 1 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 1 1 1 1 1 1 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 1 1 1 1 1 1 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 1 1 1 1 1 1 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0
```

### Exercice {num}`exo-donnees`

Comment pourrait-on compressez les données de l'image ci-dessus?

````{solution}
On pourrait regrouper les pixels identiques:
```{code-block} text
538 * 0
2 * 1
37 * 0
4 * 1
35 * 0
6 * 1
2 * 0
2 * 1
29 * 0
...
```
````

### Exercice {num}`exo-donnees`

1.  Télécharger le fichier [`maison.pbm`](maison.pbm).
2.  Quelle est le poids (taille) de cette image?
3.  Compressez cette image en l'envoyant dans un fichier compressé .zip.\
    Quelle est la taille de l'image compressée?

### Codage par plages

Le codage par plages (Run-Length Encoding en anglais) est un algorithme de
compression de données qui consiste à remplacer des suites de valeurs identiques
par des paires: nombre de répétitions/valeur à répéter.

#### Exemple {num}`ex-donnees`

Données brutes: aaaaaabcccdd -> 12 caractères\
Données codées: 6a1b3c2d -> 8 caractères (données compressées)

Cette manière de faire n'altère pas l'image, il s'agit donc d'une compression
sans perte.

## Son

À partir des années 1980, la numérisation audio a permis de stocker de la
musique sur des supports numériques, notamment les CD (disques compacts). Comme
pour les images, il existe des formats de compression audio sans perte, tels que
Dolby TrueHD ou Flac, qui préservent intégralement la qualité sonore mais
occupent un espace de stockage important.

En revanche, des formats comme **MP3** ou Dolby Digital utilisent une
compression avec perte. Ce type de compression, fondé sur des études
psychoacoustiques, élimine certaines parties du son jugées non essentielles à
l'écoute, afin de réduire considérablement la taille du fichier.

## Vidéo

Une vidéo est une succession d'images diffusées à un certain rythme et
accompagnées de son. La plupart des vidéos présentent un flux d'images compris
entre 24 et 30 images par seconde, un rythme qui correspond à la capacité du
cerveau à traiter les informations visuelles.

### Exemple {num}`ex-donnees`

Une image d'un film numérisé au format DVD en définition standard (720 x 576
pixels) en RGB a un poids de: $720 * 576 * 3 \cong 1.24 \textrm{ Mo}$.\
Une seconde de film à 25 images par seconde représente:
$25 * 1.24 \cong 31 \textrm{ Mo}$.\
Un film de 2 heures peut atteindre:
$31 * 2 * 3600 \cong 223\,200 \textrm{ Mo} \cong 223 \textrm{ Go}$.

Il est donc essentiel de compresser les vidéos afin de les stocker sur le
disque (DVD), dont la capacité est de 4.7 Go. Pour cela, on exploite les limites
de notre perception visuelle et auditive en supprimant les éléments que nos sens
ne distinguent pas clairement. Par exemple, un ensemble de pixels aux couleurs
proches peut être remplacé par une couleur moyenne, ce qui entraîne une perte de
qualité.

Une autre approche repose sur la similarité entre les images successives: plutôt
que d’encoder chaque image en entier, on représente uniquement les différences
par rapport à l’image précédente.

### Exercice {num}`exo-donnees`

Considérons un film en haute définition en format Blu-ray (HD: 1280 x 720 pixels)
encodé en RGB.

1. Quel est le poids d'une image?
2. Quel est le poids d'une seconde de film (à 25 images par seconde)?
3. Quel est le poids du film complet (2 heures)?

```{solution}
1. $1280 * 720 * 3 = 2\,764\,800 \cong 2.77 \textrm{ Mo}$
2. $25 * 2.77 \cong 69.1 \textrm{ Mo}$
3. $69.1 * 2 * 3600 \cong 497\,664 \textrm{ Mo} \cong 498 \textrm{ Go}$
```

### Exercice {num}`exo-donnees`

Vous disposez d'un accès internet en fibre optique permettant un débit de
téléchargement de 500 Mb/s. Combien de temps faut-il pour télécharger un film:

1. en Blu-ray non compressé (420 Go)?
2. au format MPEG-4 AVC (16.2 Go)?

```{solution}
1. $\dfrac{420000 * 8}{500} = 6720 \textrm{ s} = 112 \textrm{ min} = 1 \textrm{ h } 52$
2. $\dfrac{16200 * 8}{500} = 4 \textrm{ min} 19 \textrm{ s}$
```

### Exercice {num}`exo-donnees`

Netflix a diffusé ses films au format HD (1280 x 720) au lieu du format 4K
(3840 x 2160) au printemps 2020. Pour quelle raison?

```{solution}
Au printemps 2020, face à la crise sanitaire, la plupart des pays européens ont
imposé un confinement à leur population. Cela a entraîné une forte adoption du
télétravail, augmentant considérablement les besoins en accès internet,
notamment pour les visioconférences et le streaming vidéo. Pour répondre à cette
hausse soudaine de la demande, Netflix et YouTube ont accepté, à la demande de
l'Europe, de réduire leurs débits d’environ 25 % afin de libérer de la bande
passante et de faciliter le travail à distance.

Le débit moyen est de 5 Mb/s pour la qualité HD et de 25 Mb/s en 4K, ce qui
équivaut à une consommation de 3 Go par heure en HD contre 7 Go par heure en 4K.
```

## Codage de Huffman

Le codage de Huffman est un algorithme de compression de données sans perte, qui
utilise un code à longueur variable pour représenter les symboles de la source
(bits, suites de bits, pixels, lettres, etc.)

Sans compression, chaque symbole serait représenté par un nombre fixe de $n$
bits.

Avec compression, les symboles fréquents sont codés sur moins de $n$ bits et les
symboles rares sont codés sur plus de $n$ bits.

Pour mettre en place ce système, il faut calculer une statistique de la
fréquence d'apparition des symboles et définir un code de longueur variable
(tableau de correspondance entre les symboles et leur codage).

### Exemple {num}`ex-donnees`

Données brute: AAAAA...AAAAAAAAAABCD (le A est répété 100 fois)

Sans compression:

| symbole | codage |
| :-----: | :----: |
| A | 00 |
| B | 01 |
| C | 10 |
| D | 11 |

Le message codé sera 00 00 ... 00 00 01 10 11 -> 206 bits

Avec compression:

| symbole | codage |
| :-----: | :----: |
| A | 1 |
| B | 010 |
| C | 011 |
| D | 00 |

Le message codé sera 1 1 ... 1 1 010 011 00 -> 108 bits
