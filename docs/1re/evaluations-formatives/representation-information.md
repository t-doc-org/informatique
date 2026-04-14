% Copyright 2026 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Représentation de l'information

```{metadata}
subject: "Mathématiques 1re année"
print-styles: tdoc/print-exam.css
page-break-force: 1
page-break-avoid: 2
```

```{include} ../../entete-examen.md
```
```{class} align-center
**Détails des calculs obligatoires. Attention au soin. Calculatrice non
autorisée.**
```
---

## Question {nump}`question`{points}`2`

Complétez:

{.lower-alpha-paren}
1.  un Gigaoctet = {leader}`.|10em` octets.
2.  $8\,000$ bits = {leader}`.|10em` octets.

```{solution}
{.lower-alpha-paren}
1.  un Gigaoctet = 1\,000\,000\,000 octets.
2.  $8\,000$ bits = 1\,000 octets.
```

## Question {nump}`question`{points}`4`

**Nombre entiers non signés**

{.lower-alpha-paren}
1.  Convertissez $1001\,0001_2$ en décimal.
2.  Convertissez $85$ en binaire.
3.  Convertissez $1001\,1111\,1100\,0111_2$ en hexadécimal.
4.  Convertissez $1A6E_{16}$ en binaire.

```{solution}
{.lower-alpha-paren}
1.  $1001\,0001_2 = 145$
2.  $85 = 1010101_2$
3.  $1001\,1111\,1101\,0111_2 = 9FD7_{16}$
4.  $1A6E_{16} = 0001\,1010\,0110\,1110_2$
```

## Question {nump}`question`{points}`3`

**Nombre entiers signés**

{.lower-alpha-paren}
1.  Additionnez $1001_2$ et $0011_2$ sur 4 bits.
2.  Le nombre $1010\,0110_2$ est-il positif ou négatif? Justifier.
3.  Déterminez l'opposé de $1010\,0110_2$.

```{solution}
{.lower-alpha-paren}
1.  $1001_2 + 0011_2 = 1100_2$
2.  $1010\,0110_2$ est un nombre négatif, car le bit de poids fort (celui tout à
     gauche) est égal à 1.
3.  L'opposé de $1010\,0110_2$ est $0101\,1010$.
```

## Question {nump}`question`{points}`4`

{.lower-alpha-paren}
1.  Qu'est-ce que l'ASCII?
2.  Quel est la taille d'un caractère avec le code ASCII?
3.  Quel est l'avantage du code ASCII?
4.  Quel est le désavantage du code ASCII?

````{solution}
{.lower-alpha-paren}
1.  L'ASCII est un encodage pour les caractères.
2.  La taille d'un caractère avec le code ASCII est de 7 bits.
3.  Le code ASCII a l'avantage de prendre peu de place.
4.  Le désavantage du code ASCII est qu'il ne permet pas d'encoder les accents.
````

## Question {nump}`question`{points}`2`

Convertissez la chaîne de caractères **Info-23** en utilisant le code ASCII en hexadécimal (cf. annexe).

```{solution}
$49\,6E\,66\,6F\2D\,32\,33_{16}$
```

## Question {nump}`question`{points}`2`

Notez le calcul qui permet de déterminer le nombre de bits minimum pour représenter une image de 800 × 600 pixels en quatre niveaux de gris.

```{solution}
Pour encoder 4 niveaux de gris, il faut 2 bits, car $2^2 = 4$.

Nombre de bits: $2 \cdot 800 \cdot 600$ bits
```

## Question {nump}`question`{points}`3`

Représentez sur le quadrillage l'image dont l'encodage est le suivant:

```{code-block} text
P1
5 4
0 1 1 0 0 1 1 1 0 0
0 1 1 1 1 0 1 1 1 0
```

```{jsxgraph}
:template: grid(35, 10)
```

````{solution}
```{exec} pnm
:class: hidden
:when: load
P1
5 4
0 1 1 0 0 1 1 1 0 0
0 1 1 1 1 0 1 1 1 0
```
````
