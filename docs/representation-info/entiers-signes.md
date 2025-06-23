% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Nombres entiers signés

## Introduction

Pour encoder des nombres entiers relatifs (appelés entiers signés), l'idée
principale est d'utiliser le bit de poids fort (le chiffre qui se trouve le plus
à gauche) pour représenter le signe: 0 si le nombre est positif et 1 si le
nombre est négatif.

Cette représentation possède deux inconvénients:

- Le nombre 0 a deux présentations différents: 00000000 et 10000000
- Les opérations arithmétiques sont plus compliquées. Il faut notamment
  différencier le cas où les deux nombres sont de même signe du cas où ils sont
  de signes différents.

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

<script type="module">
const [core, quiz] = await tdoc.imports('tdoc/core.js', 'tdoc/quiz.js');

quiz.check('negdec', args => {
    args.answer = {
      neg: v => core.strToInt(v, 2),
      dec: v => core.strToInt(v),
    }[args.solution](args.answer);
    const tr = args.field.closest('tr');
    let s = '';
    for (const el of core.qsa(tr, 'math > mn, math > msub > mn:first-child')) {
      s += el.textContent;
    }
    const value = core.strToInt(s, 2);
    const wrap = 1 << s.length, neg = wrap - value;
    const dec = neg < wrap / 2 ? neg : neg - wrap;
    args.solution = {neg, dec}[args.solution];
});
quiz.check('mag', args => {
    const smallest = args.solution[0] === '<';
    const signed = args.solution[1] === 's';
    const bits = core.strToInt(args.solution.slice(2));
    const radix = args.role === 'dec' ? 10 : 2;
    let v = (1 << bits) - 1;
    if (smallest) v -= (1 << bits) - 1;
    if (signed) v -= 1 << (bits - 1);
    if (signed && v < 0 && radix !== 10) v += 1 << bits;
    args.answer = core.strToInt(args.answer, radix);
    args.solution = v;
});
</script>

Déterminer l'opposé des nombres suivants en binaire, ainsi que la valeur
décimale de celui-ci.

```{role} input(quiz-input)
:style: width: 6rem; text-align: center;
:check: remove negdec
```

```{quiz}
| Nombre binaire | Opposé       | Valeur décimale |
| :------------: | :----------: | :-------------: |
| $0111_2$       | {input}`neg` | {input}`dec`    |
| $0101\,1010_2$ | {input}`neg` | {input}`dec`    |
| $1111_2$       | {input}`neg` | {input}`dec`    |
| $1101\,0001_2$ | {input}`neg` | {input}`dec`    |
```

## Exercice {num}`exo-info`

Répondre aux questions suivantes:

```{role} dec(quiz-input)
:style: width: 3rem; text-align: center;
:check: remove mag
```
```{role} bin(quiz-input)
:style: width: 6rem; text-align: center;
:check: remove mag
```
```{role} str(quiz-input)
:style: width: 6rem; text-align: center;
:check: remove
```

```{quiz}
| Quel est le plus... | 4 bits, décimal | 4 bits, binaire | 8 bits, décimal | 8 bits, binaire | n bits |
| - | :-: | :-: | :-: | :-: | :-: |
| ... **grand** nombre entier **non signé** sur... | {dec}`>u4` | {bin}`>u4` | {dec}`>u8` | {bin}`>u8` | {str}`2^n-1` |
| ... **petit** nombre entier **non signé** sur... | {dec}`<u4` | {bin}`<u4` | {dec}`<u8` | {bin}`<u8` | {str}`0` |
| ... **grand** nombre entier **signé** sur...     | {dec}`>s4` | {bin}`>s4` | {dec}`>s8` | {bin}`>s8` | {str}`2^(n-1)-1` |
| ... **petit** nombre entier **signé** sur...     | {dec}`<s4` | {bin}`<s4` | {dec}`<s8` | {bin}`<s8` | {str}`-2^(n-1)` |
```
