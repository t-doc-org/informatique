% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Introduction

Depuis la nuit des temps, les humains ont cherché à protéger leurs secrets et à
garantir la confidentialité de leurs échanges, développant des techniques
ingénieuses pour transmettre des messages secrets.  Deux approches distinctes
ont émergé pour ce faire: la stéganographie et la cryptographie.

## Stéganographie

La **stéganographie** est une technique qui consiste à cacher l'existence même
du message. Si quelqu'un devine l'existence du message, il peut le
lire.

## Exemples

<table><tr><td style="width:50%" valign="top">

### Tatouage sur le crâne

L'historien grec Hérodote, raconte qu'au V{sup}`e` siècle avant Jésus-Christ,
un certain Histiée rasa le crâne d'un de ses esclaves, y tatoua le message et
attendit que les cheveux repoussent. Ensuite, il envoya l'esclave à Aristagoras,
son gendre, avec la consigne de lui raser la tête.

</td><td>

```{figure} images/crane.jpg
:alt: Écriture sur le crâne
:align: center

source: hareenlaks.blogspot.com
```

</td></tr></table>

<table><tr><td style="width:50%" valign="top">

### Tablette de cire

Toujours selon Hérodote, un certain Démarate, pour informer discrètement les
Spartiates de l'attaque imminente des Perses, prit des tablettes, en racla la
cire et grava le message secret sur le bois, puis il recouvrit le bois de cire.
Ainsi les tablettes semblent vierges et n'attirent pas l'attention.

</td><td>

```{figure} images/tablette.jpg
:alt: Tablette de cire
:align: center

photo: Peter van der Sluijs
```

</td></tr></table>

### Boule de cire

En Chine, le message secret était écrit sur une fine soie et placé dans une
petite boule de cire. Le messager avalait ensuite cette boule...

### Oeuf dur

Au XVI{sup}`e` siècle, le scientifique italien Giovanni Porta dissimula un
message dans un oeuf dur. Pour cela, il faut écrire sur la coquille avec une
encre contenant une once[^sn1] d'alun pour une pinte[^sn2] de vinaigre. Cette solution
traverse la coquille et se dépose sur le blanc d'oeuf. Pour lire le message, il
suffit de peler l'oeuf.
[^sn1]: Unité de masse comprise entre 25 et 34 grammes.
[^sn2]: Unité de volume qui vaut environ 0.9 litre.

## Cryptographie

La **{term}`cryptographie`** est l'ensemble des procédés visant à
{term}`chiffrer` un message. Elle assure la confidentialité entre l'émetteur et
le destinataire. Seul celui qui a la {term}`clé` de déchiffrement peut lire le message.

## Exemples

### Code Mary Stuart

Le 15 octobre 1586, Marie Stuart est jugée pour trahison. Elle est accusée
d'avoir pris part à un complot pour tenter d'assassiner la reine Elizabeth et
ainsi s'emparer de la couronne d'Angleterre.

Le code[^sn3] utilisé est constitué de 23 symboles qui remplacent les lettres de
l'alphabet (sauf j, v et w), ainsi que 36 symboles représentant des mots ou des
phrases. De plus, il y a quatre symboles qui ne font rien et un symbole qui
indique que la lettre suivante est doublée.
[^sn3]: Ensemble des conventions et des symboles utilisés pour rendre le message
secret.

```{figure} images/code-mary.gif
:alt: Tablette de cire
:align: center

source: [apprendre en ligne](https://www.apprendre-en-ligne.net/crypto/codes/mary.html)
```

### Chiffre Pig Pen

Le chiffre de Pig Pen est un chiffre de substitutions qui a perduré pendant des
siècles sous des formes variées. Un voici un exemple:

```{figure} images/pigpen.gif
:alt: Chiffre de Pig Pen
:align: center

source: [apprendre en ligne](https://www.apprendre-en-ligne.net/crypto/subst/pigpen.html)
```

#### Exercice

Que signifie le message suivant?

```{figure} images/ex1.png
:alt: Message codé avec le chiffre de Pig Pen
:align: center
:width: 80%
```

````{solution}
steganographie ou cryptographie
````
