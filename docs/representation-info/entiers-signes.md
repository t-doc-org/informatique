% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Nombres entiers signés

## Introduction

Pour encoder des nombres entiers relatifs (appelés entiers signés), l'idée
principale est d'utiliser le bit de poids fort (le chiffre qui se trouve le plus
à gauche) pour représenter le signe: 0 si le nombre est positif et 1 si le
nombre est négatif.

Cette représentation possède deux inconvénients:

- le nombre 0 a deux présentations différents: 00000000 et 10000000
- les opérations arithmétiques sont plus compliquées. Il faut notamment
différencier le cas où les deux nombres sont de même signe du cas où ils sont de
signes différents.

## Complément à 2

La notation en complément à 2 permet de remédier à ces problèmes. Les nombres
entiers relatifs positifs sont représentés comme des entiers positifs avec le
bit de poids fort qui est à zéro (bit de signe) et les entiers relatifs négatifs
sont obtenus selon le tableau ci-dessous:

| Écriture | Entiers non signés (valeur décimale) | Entiers signés (valeur décimale) |
|:--------:|:-----------------------------------:|:--------------------------------:|
| 4 bits   | tous les bits sont utilisés pour définir le nombre | le bit de poids fort est utilisé pour le signe |
| 0000     | 0                                   | 0                                |
| 0001     | 1                                   | 1                                |
| 0010     | 2                                   | 2                                |
| 0011     | 3                                   | 3                                |
| 0100     | 4                                   | 4                                |
| 0101     | 5                                   | 5                                |
| 0110     | 6                                   | 6                                |
| 0111     | 7                                   | 7                                |
| 1000     | 8                                   | -8                               |
| 1001     | 9                                   | -7                               |
| 1010     | 10                                  | -6                               |
| 1011     | 11                                  | -5                               |
| 1100     | 12                                  | -4                               |
| 1101     | 13                                  | -3                               |
| 1110     | 14                                  | -2                               |
| 1111     | 15                                  | -1                               |

### Remarques

| Entiers non signés sur 4 bits | Entiers signés sur 4 bits |
|:------------------:|:--------------:|
| La valeur minimale est 0 | La valeur minimale est $-2^{4-1} = -8$ |
| La valeur maximale est $2^4-1 = 15$ | La valeur maximale est $2^{4-1}-1 = 7$ |

## Opposé d'un nombre

Pour déterminer l'opposé d'un nombre, il faut:
1. Inverser tous les bits (0 $\rightarrow$ 1 et 1 $\rightarrow$ 0);
2. Additionner 1.

L'opposé de $0101_2$ est $1011_2$. En effet,
```{code-block} text
  1 0 1 0     (inverser chaque bit)
+       1     (ajouter 1)
----------
  1 0 1 1
```

Vérification: l'addition d'un nombre et de son opposé doit donner 0.
```{code-block} text
  1 1 1 1      (retenues)
    0 1 0 1
+   1 0 1 1
------------
  1 0 0 0 0    (sans tenir compte de la retenue finale)
```

## Exercice {num}`exo-info`

Déterminer l'opposé des nombres suivants en binaire, ainsi que la valeur
décimale de celui-ci.

<script>
async function questionNeg(value, bits) {
  let node = document.currentScript;
  const core = await tdoc.import('tdoc/core.js');
  const quizz = await tdoc.import('tdoc/quizz.js');
  const wrap = 1 << bits, neg = wrap - value;
  node = quizz.question(node, "Opposé:", resp => {
    return core.strToInt(resp.replaceAll(' ', ''), 2) === neg;
  });
  const dec = neg < wrap / 2 ? neg : neg - wrap;
  quizz.question(node, "Valeur décimale:", resp => {
    return core.strToInt(resp.replaceAll(' ', '')) === dec;
  });
}
</script>

1.  $0111_2$
    <script>questionNeg(0b0111, 4);</script>
2.  $0101\,1010_2$
    <script>questionNeg(0b01011010, 8);</script>
3.  $1111_2$
    <script>questionNeg(0b1111, 4);</script>
4.  $1101\,0001_2$
    <script>questionNeg(0b11010001, 8);</script>

## Exercice {num}`exo-info`

Répondre aux questions suivantes:

<script>
async function questionMagOne(node, prompt, value, bits, radix) {
  const core = await tdoc.import('tdoc/core.js');
  const quizz = await tdoc.import('tdoc/quizz.js');
  if (bits && value < 0 && radix === 2) value += 1 << bits;
  return quizz.question(node, prompt, resp => {
    resp = resp.replaceAll(' ', '');
    return (bits ? core.strToInt(resp, radix) : resp) === value;
  });
}

async function questionMag(v4, v8, vn) {
  let node = document.currentScript;
  node = await questionMagOne(node, "... sur 4 bits, en décimal?", v4, 4, 10);
  node = await questionMagOne(node, "... sur 4 bits, en binaire?", v4, 4, 2);
  node = await questionMagOne(node, "... sur 8 bits, en décimal?", v8, 8, 10);
  node = await questionMagOne(node, "... sur 8 bits, en binaire?", v8, 8, 2);
  await questionMagOne(node, "... sur n bits?", vn);
}
</script>

1.  Quel est le plus **grand** nombre entier **non signé** que nous pouvons
    écrire...
    <script>questionMag((1 << 4) - 1, (1 << 8) - 1, "2^n-1");</script>

2.  Quel est le plus **petit** nombre entier **non signé** que nous pouvons
    écrire...
    <script>questionMag(0, 0, "0");</script>

3.  Quel est le plus **grand** nombre entier **signé** que nous pouvons
    écrire...
    <script>
    questionMag((1 << (4 - 1)) - 1, (1 << (8 - 1)) - 1, "2^(n-1)-1");
    </script>

4.  Quel est le plus **petit** nombre entier **signé** que nous pouvons
    écrire...
    <script>questionMag(-(1 << (4 - 1)), -(1 << (8 - 1)), "-2^(n-1)");</script>
