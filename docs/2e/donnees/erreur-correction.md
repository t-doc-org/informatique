% Copyright 2021 Xavier Dutoit
% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Correction d'erreur

## Introduction

Dans le chapitre précédent, nous avons vu des procédés qui permettent de
détecter des erreurs. Lorsqu'une erreur est détectée, nous aimerions dans
l'idéal la corriger. Mais la correction est une opération compliquée et elle
n'est dans certains cas pas nécessaire.

### Exemple {num2}`exemple`

#### Carte de crédit

Lorsqu'un numéro de carte de crédit est entré sur un site web, un code détecteur
d'erreur permet de savoir si le numéro est correct ou pas. Dans ce cas, seule
l'information de la validité du numéro est intéressante.

#### Connexion téléphonique

Lors d'un appel téléphonique, des erreurs peuvent se produire. Comme la
communication est synchrone, il n'est pas possible d'utiliser un code correcteur
d'erreur, mais le code détecteur d'erreur permet simplement d'ignorer la partie
du message qui contient une erreur et la conversation est tout de même
compréhensible.

#### Transmission entre Mars et la Terre

Lorsqu'une sonde qui se trouve sur Mars envoie un message, la latence (le délai
de transmission) peut être plus de 22 minutes. Dans ce cas, le renvoi du
message n'est pas une solution.

#### Sauvegarde de données sur un disque dur externe

Lorsqu'une erreur est détectée lors de la copie de données sur un disque dur
externe, il est facile de retransmettre les données. Cela est plus rapide que
d'utiliser un code correcteur d'erreur.

## Codes correcteurs d'erreur

Les exemples précédents montrent qu'il n'est souvent pas nécessaire de corriger
des erreurs et que le simple fait de savoir est suffisant. Mais dans certains
cas, il est essentiel de pouvoir corriger des erreurs.

Nous allons voir deux procédés qui permettent de corriger des erreurs.

### Répétition de l'information

Chaque bit est répété $n$ fois.

#### Exemple {num2}`exemple`

$H(3, 1)$

| message utile | message codé |
| :-----------: | :----------: |
| 0             | 000          |
| 1             | 111          |

message utile: 0 &rarr; message codé (envoyé): 000

| message reçu  | nombre d'erreurs | message décodé | correct? |
| :-----------: | :--------------: | :------------: | :------: |
| 000           | 0                | 0              | oui      |
| 001           | 1                | 0              | oui      |
| 010           | 1                | 0              | oui      |
| 100           | 1                | 0              | oui      |
| 110           | 2                | 1              | non      |
| 101           | 2                | 1              | non      |
| 011           | 2                | 1              | non      |
| 111           | 3                | 1              | non      |

Une erreur est détectée et corrigée.\
Deux erreurs sont détectées, mais mal corrigées.\
Trois erreurs ne sont pas détectées.\
$C_d = 2$ et $C_c = 1$

Efficacité: u = 1 et m = 3\
$\dfrac{u}{m} = \dfrac{1}{3} \cong 33.3 \%$

#### Exercice {num2}`exercice`

En vous aidant de l'exemple précédent, effectuez la même analyse du code
$H(3, 1)$ pour le message utile: 1.

```{solution}
message utile: 1 &rarr; message codé (envoyé): 111

| message reçu  | nombre d'erreurs | message décodé | correct? |
| :-----------: | :--------------: | :------------: | :------: |
| 111           | 0                | 1              | oui      |
| 110           | 1                | 1              | oui      |
| 101           | 1                | 1              | oui      |
| 011           | 1                | 1              | oui      |
| 001           | 2                | 0              | non      |
| 010           | 2                | 0              | non      |
| 100           | 2                | 0              | non      |
| 000           | 3                | 0              | non      |

L'efficacté, la capacité de détection et la capacité de correction sont les
mêmes, car elles ne dépendent pas du message envoyé, mais du code utilisé, ici
$H(3, 1)$:

- $C_d = 2$ et $C_c = 1$
- Efficacité $\cong 33.3 \%$
```

### Code de Hamming

Le code de correction d'erreur le plus efficace est le code de Hamming. Il
utilise plusieurs bits de parité sur des morceaux différents.

Structure du code de Hamming $H(m, u)$:
1.  Il est composé de différents éléments:
    - le message utile composé de $u$ bits
    - les $c$ bits de contrôle de parité

    Les $u$ bits du message et les $c$ bits de contrôle sont mélangés, mais
    placés à des endroits bien définis.
2.  Le message codé est de longueur $m = 2^u - 1$, C'est-à-dire 7, 15, 31, ...
3.  Les bits de parité $p_i$ sont en position $2^i$, avec $i = 0, 1, 2, \dots$
4.  Les bits du message $d_i$ occupent les autres places.

#### Exemple {num2}`exemple`

$H(7, 4)$

Message utile de 4 bits: $d_1$, $d_2$, $d_3$ et $d_4$

Bits de contrôle: il y a 3 bits de parité $p_1$, $p_2$ et $p_3$

Les bits de données vont dans un ordre particulier:

```{figure} images/hamming5.svg
:alt: Bits de contrôle
:width: 250px
:align: center
```

````{list-grid}
:style: |
: grid-template-columns: 1fr 1fr; align-items: center;
: margin-bottom: 0;
- $p_1$: bit de parité de $d_1$, $d_2$ et $d_4$

  $p_2$: bit de parité de $d_1$, $d_3$ et $d_4$

  $p_3$: bit de parité de $d_2$, $d_3$ et $d_4$
- ```{figure} images/hamming1.svg
  :alt: Bits de contrôle
  :width: 200px
  :align: center
  ```
````

Vérification: Les trois parités doivent être correctes.

##### Cas 1: une parité fausse

````{list-grid}
:style: |
: grid-template-columns: 1fr 1fr; align-items: center;
: margin-bottom: 0;
- <span style="color: #EA4335;">Parité 1:</span>
  $p_1$, $d_1$, $d_2$, $d_4$ <b><span style="color: #EA4335;">&#10007;</span></b>

  <span style="color: #34A853;">Parité 2:</span>
  $p_2$, $d_1$, $d_3$, $d_4$ <b><span style="color: #34A853;">&#10003;</span></b>

  <span style="color: #4285F4;">Parité 3:</span>
  $p_3$, $d_2$, $d_3$, $d_4$ <b><span style="color: #34A853;">&#10003;</span></b>

  &rArr; $p_1$ est faux
- ```{figure} images/hamming2.png
  :alt: Bits de contrôle
  :width: 200px
  :align: center
  ```
````

##### Cas 2: deux parités fausses

````{list-grid}
:style: |
: grid-template-columns: 1fr 1fr; align-items: center;
: margin-bottom: 0;
- <span style="color: #EA4335;">Parité 1:</span>
  $p_1$, $d_1$, $d_2$, $d_4$ <b><span style="color: #EA4335;">&#10007;</span></b>

  <span style="color: #34A853;">Parité 2:</span>
  $p_2$, $d_1$, $d_3$, $d_4$ <b><span style="color: #34A853;">&#10003;</span></b>

  <span style="color: #4285F4;">Parité 3:</span>
  $p_3$, $d_2$, $d_3$, $d_4$ <b><span style="color: #EA4335;">&#10007;</span></b>

  &rArr; $d_2$ est faux
- ```{figure} images/hamming3.png
  :alt: Bits de contrôle
  :width: 200px
  :align: center
  ```
````

##### Cas 3: trois parités fausses

````{list-grid}
:style: |
: grid-template-columns: 1fr 1fr; align-items: center;
: margin-bottom: 0;
- <span style="color: #EA4335;">Parité 1:</span>
  $p_1$, $d_1$, $d_2$, $d_4$ <b><span style="color: #EA4335;">&#10007;</span></b>

  <span style="color: #34A853;">Parité 2:</span>
  $p_2$, $d_1$, $d_3$, $d_4$ <b><span style="color: #EA4335;">&#10007;</span></b>

  <span style="color: #4285F4;">Parité 3:</span>
  $p_3$, $d_2$, $d_3$, $d_4$ <b><span style="color: #EA4335;">&#10007;</span></b>

  &rArr; $d_4$ est faux
- ```{figure} images/hamming4.svg
  :alt: Bits de contrôle
  :width: 200px
  :align: center
  ```
````

Vérification des trois parités:

```{figure} images/hamming6.svg
:alt: Bits de contrôle
:width: 250px
:align: center
```

Une erreur est détectée et corrigée.\
Deux erreurs sont détectées, mais mal corrigées.\
Trois erreurs ne sont pas détectées.\
$C_d = 2$ et $C_c = 1$

Efficacité: u = 4 et m = 7\
$\dfrac{u}{m} = \dfrac{4}{7} \cong 57.1 \%$

#### Exercice {num2}`exercice`

On considère le code de Hamming $H(7, 4)$.
Pour chacun des messages utiles suivants:

- indiquez les 3 bits de parités
- encodez le message

<script type="module">
const [core, quiz] = await tdoc.imports('tdoc/core.js', 'tdoc/quiz.js');

// Hamming-encode the given message.
function hammingEncode(msg, parityBits) {
    const ebits = (1 << parityBits) - 1;
    const dataBits = ebits - parityBits;
    let parity = 0, encoded = 0, mask = 1 << (dataBits - 1);
    for (let i = 1; i <= ebits; ++i) {
        if ((i & (i - 1)) === 0) continue;
        const bit = (msg & mask) !== 0 ? 1 : 0;
        encoded |= bit << (ebits - i);
        for (let p = 0; p < parityBits; ++p) {
            if ((i & (1 << p)) !== 0) parity ^= bit << p;
        }
        mask >>= 1;
    }
    for (let p = 0; p < parityBits; ++p) {
        const bit = (parity & (1 << p)) !== 0 ? 1 : 0;
        encoded |= bit << (ebits - (1 << p));
    }
    return encoded;
}

// Hamming-decode the given encoded message.
function hammingDecode(encoded, parityBits) {
    const ebits = (1 << parityBits) - 1;
    const dataBits = ebits - parityBits;
    let error = 0;
    for (let i = 1; i <= ebits; ++i) {
        for (let p = 0; p < parityBits; ++p) {
            const bit = (encoded & (1 << (ebits - i))) !== 0 ? 1 : 0;
            if ((i & (1 << p)) !== 0) error ^= bit << p;
        }
    }
    let corrected = encoded;
    if (error !== 0) corrected ^= 1 << (ebits - error);
    let decoded = 0;
    let shift = dataBits - 1;
    for (let i = 1; i <= ebits; ++i) {
        if ((i & (i - 1)) === 0) continue;
        if ((corrected & (1 << (ebits - i))) !== 0) decoded |= 1 << shift;
        shift -= 1;
    }
    return {error, corrected, decoded};
}

function encode(parityBits) {
    return () => {
        const dataBits = (1 << parityBits) - parityBits - 1;
        const msg = Math.floor(Math.random() * (1 << dataBits));
        const encoded = core.toRadix(hammingEncode(msg, parityBits), 2,
                                     (1 << parityBits) - 1);
        if (tdoc.dev) {
            console.log(`${core.toRadix(msg, 2, dataBits)} => ${encoded}`);
        }
        return {
            msg,
            equal(other) { return other.msg === msg; },
            history: (1 << dataBits) / 2,

            msg(ph) { ph.textContent = core.toRadix(msg, 2, dataBits); },
            p(args, p) { args.ok = args.answer === encoded[(1 << p) - 1]; },
            p1(args) { this.p(args, 0); },
            p2(args) { this.p(args, 1); },
            p3(args) { this.p(args, 2); },
            encoded(args) { args.ok = args.answer.trim() === encoded; },
        };
    };
}

function decode(parityBits) {
    return () => {
        const ebits = (1 << parityBits) - 1;
        const dataBits = ebits - parityBits;
        const msg = Math.floor(Math.random() * (1 << ebits));
        const dec = hammingDecode(msg, parityBits);
        if (tdoc.dev) {
            console.log(`\
${core.toRadix(msg, 2, ebits)} => ${core.toRadix(dec.corrected, 2, ebits)}`);
        }
        return {
            msg,
            equal(other) { return other.msg === msg; },
            history: (1 << ebits) / 2,

            msg(ph) { ph.textContent = core.toRadix(msg, 2, ebits); },
            p(args, p) {
                args.ok = {'correcte': 0, 'fausse': 1}[args.answer]
                          === ((dec.error >> p) & 1);
            },
            p1(args) { this.p(args, 0); },
            p2(args) { this.p(args, 1); },
            p3(args) { this.p(args, 2); },
            err(args) {
                let a = args.answer.trim();
                if (a === '') a = '0';
                args.ok = a === dec.error.toString();
            },
            corrected(args) {
                args.ok = args.answer.trim()
                          === core.toRadix(dec.corrected, 2, ebits);
            },
            decoded(args) {
                args.ok = args.answer.trim()
                          === core.toRadix(dec.decoded, 2, dataBits);
            },
        };
    };
}

quiz.generator('hamming-encode', encode(3));
quiz.generator('hamming-decode', decode(3));
</script>

```{role} bit(quiz-select)
:options: |
: 0
: 1
```
```{role} input(quiz-input)
:style: width: 8rem; text-align: center;
```

```{quiz} table hamming-encode
| message utile  | $p_1$     | $p_2$     | $p_3$     | message codé     |
| :-----------:  | :-------: | :-------: | :-------: | :--------------: |
| 1010           | 1         | 0         | 1         | 1011010          |
| {quiz-ph}`msg` | {bit}`p1` | {bit}`p2` | {bit}`p3` | {input}`encoded` |
```

#### Exercice {num2}`exercice`

On considère le code de Hamming $H(7, 4)$.
Pour chacun des messages reçus suivants:

- indiquez si chacune des 3 parités est correcte ou fausse
- indiquez quel bit est erroné (laissez vide s'il n'y en a pas)
- corrigez le message reçu
- décodez le message

```{role} parity(quiz-select)
:options: |
: correcte
: fausse
```
```{role} nbit(quiz-input)
:style: width: 3rem; text-align: center;
```
```{role} bin7(quiz-input)
:style: width: 7rem; text-align: center;
```
```{role} bin4(quiz-input)
:style: width: 4rem; text-align: center;
```

```{quiz} table hamming-decode
| message reçu   | parité&nbsp;1 | parité&nbsp;2 | parité&nbsp;3 | bit erroné  | message corrigé   | message décodé  |
| :------------: | :-----------: | :-----------: | :-----------: | :---------: | :---------------: | :-------------: |
| 0101001        | fausse        | correcte      | correcte      | 1           | 1101001           | 0001            |
| {quiz-ph}`msg` | {parity}`p1`  | {parity}`p2`  | {parity}`p3`  | {nbit}`err` | {bin7}`corrected` | {bin4}`decoded` |
```
