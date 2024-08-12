<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# Cryptographie symétrique

La **cryptographie symétrique**, également appelée cryptographie à clé secrète,
est la méthode de chiffrement la plus ancienne. Elle repose sur l'utilisation
d'une même clé pour chiffrer et déchiffrer un message.

```{figure} images/crypt-sym.png
:alt: Schéma de la cryptographie symétrique
:width: 70%
:align: center

source: www.pgpi.org
```

- Une clé est choisie et échangée entre les participants.
- Le chiffrement et le déchiffrement s'effectue à l'aide d'un algorithme qui
utilise cette clé.

## Transposition

Dans une **transposition**, les lettres du texte clair sont mélangées, mais pas
modifiées. C'est-à-dire que le texte mélangé est un anagramme du texte
d'origine.

<table><tr><td valign="top">

### Scytale

Ce procédé était déjà utilisé pendant l'Antiquité par les Spartes. La scytale
est un morceau de bois autour duquel est entouré une bande de cuir ou de
parchemin. L'expéditeur écrit son message et déroule la bande qui est une suite
de lettre sans signification. Le messager amène cette bande, en générale portée
comme ceinture, au destinataire qui enroulera cette bande sur son bâton de même
diamètre pour lire le message en clair.\
**Clé de chiffrement:** la largeur du bâton.

</td><td>

```{figure} images/scytale.jpg
:alt: Scytale
:width: 1000px
:align: center

source: [apprendre en ligne](https://www.apprendre-en-ligne.net/crypto/index-crypto-transpo.html)
```
</td></tr></table>

### Chiffre Rail Fence

Ce procédé a été beaucoup utilisé pendant la guerre de Sécession. Le Rail Fence
dipose les lettres en "zig zag" sur un nombre de lignes donné.

Le texte VIVE LE COLLEGE SAINTE-CROIX donnera le message codé sur 2 lignes:
VVLCLEEANERIIEEOLGSITCOX\
Écrit en "zig zag" donne:

```{code-block} text
V V L C L E E A N E R I
 I E E O L G S I T C O X
```

Le même texte donnera le message codé sur 3 lignes: VLLENRIEEOLGSITCOXVCEAEI\
Écrit en "zig zag" donne:

```{code-block} text
V   L   L   E   N   R
 I E E O L G S I T C O X
  V   C   E   A   E   I
```

**Clé de chiffrement:** le nombre de lignes.


## Substitution monoalphabétique

Dans la **substitution monoalphabétique**, aussi appelée substitution simple,
chaque lettre est remplacée par un autre symboles, toujours le même.


### Chiffre de César

Ce procédé, déjà utilisé dans l'Antiquité, était connu des Romains. Jules César,
dont elle tire le nom, l'employait pour chiffrer certaines de ses
correspondances. La substitution proposée par César est un décalage de trois
positions. C'est-à-dire que a est remplacé par D, b par E, etc.

| Clair | a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z |
| :---: |:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Chiffré | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C |

**Clé de chiffrement:** décalage de trois positions.

Il est possible de décaler de 1 à 25 positions. Il existe donc 25 clés de César
différentes.

Une telle substitution n'est pas très sûre, car la connaissance d'une seule
lettre permet de découvrir tout le message sans difficulté.

Si les 25 positions possibles sont testées, le message sera découvert.

### Cas général

Pour rendre le décryptage plus difficile, on peut substituté à chaque lettre une
lettre tirée au hasard. Dans ce cas, il y a environ $1.5 \cdot 10^{25}$
possibilités.

| Clair | a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z |
| :---: |:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Chiffré | K | T | E | W | Q | J | S | V | M | A | Z | G | P | X | C | U | I | O | B | L | Y | F | R | N | D | H |

**Clé de chiffrement:** le tableau de correspondance entier.

### Attaque

Une méthode efficace pour attaquer un message qui utilise une substitution
monalphabétique est l'**analyse des fréquences**. En supposant que le symbole le
plus fréquent remplace la lettre la plus fréquente en français (le "e") et en
appliquant cette logique aux autres lettres, il devient possible de
décrypte le message, à condition qu'il soit suffisamment long.

Voici un tableau qui représente la fréquence d'apparition des lettres en
français (les lettres accentuées ont été remplacée par des lettres non
accentuées, les espaces et ponctuations ont été supprimés).

| Lettre | e | a | s | i | t | n | r | ... |
| :---: |:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Fréquence (en %) | 17.4 | 8.2 | 8.1 | 7.3 | 7.2 | 7.1 | 6.6 | ... |

```{figure} images/batonsfr.gif
:alt: Fréquence d'apparition des lettres en français
:align: center

source: [apprendre en ligne](https://apprendre-en-ligne.net/crypto/stat/francais.html)
```






