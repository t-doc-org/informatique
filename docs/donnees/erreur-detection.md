% Copyright 2021 Xavier Dutoit
% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Détection d'erreur

## Stockage et transmission de l'information

L'information doit souvent être transmise ou stockée:

- envoi d'un mail
- copie d'un texte sur un disque dur externe
- copie d'un film sur une clé USB
- sauvegarde d'un fichier en mémoire
- envoi d'un message via Bluetooth
- envoi d'une photo via Air Drop
- etc.

Lors de ces opérations, il peut y avoir des erreurs.

## Erreurs de transmission

### Exemple {num1}`exemple`

Alice et Bob s'envoient des messages via Bluetooth. Ils se trouvent à une dizaine
de mettre l'un de l'autre, la connexion n'est donc pas bonne et le message
contient des erreurs.

```{figure} images/message.png
:alt: Envoi de message via bluetooth
:width: 80%
:align: center
```

Bob se rend compte qu'il y a des erreurs dans le message et arrive tout de même
à lire et comprendre le message d'Alice.

Lorsque nous transmettons des informations sous forme numérique (suites de 0 et
de 1), il y a parfois des erreurs.

```{figure} images/erreur.png
:alt: Erreur de transmission
:width: 50%
:align: center
```

Malheureusement, un seul bit peut corrompre tout un fichier. Il est nécessaire
de pouvoir garantir l'intégrité des données et donc de **détecter** et
**corriger** les erreurs.

## Principes de base

1.  L'émetteur et le récepteur doivent utiliser un ensemble de **règles
    communes**.
2.  Il faut ajouter ou répéter des informations, c'est-à-dire de la
    **redondance**.

### Exemple {num1}`exemple`

```{iframe} https://docs.google.com/presentation/d/e/2PACX-1vQEemAMuCYvYvdxAJVRJBFD5NU8NQzasRyRpNau10iIVNGCpZSRgw_5dYTUd8EDhE8YyB_6v8b_2F37/embed?start=false&loop=false&delayms=3000
```

## Définitions

Détection d'erreur
: Je sais qu'il y a une erreur, mais je ne sais pas où.

Correction d'erreur
: Je sais qu'il y a une erreur et je peux la corriger.

Message utile:
: Information que l'on souhaite envoyer. Longueur
  **<span style="color:#336600">u</span>** bits.

Bits de contrôle:
: Bits ajoutés au message utile pour la détection et/ou la correction. Longueur
  **<span style="color:#CC0000">c</span>** bits.

Message codé
: Message utile auquel on a ajouté de l'information, de la redondance.
  Message effectivement envoyé. Longueur
  **<span style="color:#3366CC">m</span>** =
  **<span style="color:#336600">u</span>** +
  **<span style="color:#CC0000">c</span>** bits.

```{figure} images/bits.png
:alt: Répartition des bits
:width: 50%
:align: center
```

Code
: Transformation d'un message utile en un message codé. Noté: $X(m, u)$.

Transmission correcte
: Lorsque le message décodé est le même que le message utile.\
  message utile &#8658; message codé &#8658; transmission (avec erreurs) &#8658;
  message reçu &#8658; message décodé

### Exemple {num1}`exemple`

L'alphabet IRSA (International Radiotelephony Spelling Alphabet) utilise des
mots pour représenter des lettres:

a &#x27FA; alpha, b &#x27FA; bravo, c &#x27FA; charlie, d &#x27FA; delta, e
&#x27FA; echo, f &#x27FA; foxtrot, g &#x27FA; golf, h &#x27FA;hotel, i &#x27FA;
india, j &#x27FA; juliett, k &#x27FA; kilo, l &#x27FA; lima, etc.

[Alphabet phonétique de l'OTAN](https://fr.wikipedia.org/wiki/Alphabet_phon%C3%A9tique_de_l%27OTAN)

```{iframe} https://docs.google.com/presentation/d/e/2PACX-1vT9yvDLq8eQqwlPhYCz6T3vY-hOumtcUT6lTQabpzNTATlLX36DZll3hp6ER0lVxQQI3MYvViZecYxH/embed?start=false&loop=false&delayms=3000
```

Capacité de détection C<sub>d</sub>
: Le code peut toujours **détecter** C<sub>d</sub> erreurs ou moins.

Capacité de correction C<sub>c</sub>
: Le code peut toujours **corriger** C<sub>d</sub> erreurs ou moins.

Efficacité
: L'efficacité d'un code est déterminée par le rapport $\dfrac{u}{m}$ avec
  $\dfrac{u}{m} \leq 1$.

## Somme de contrôle (checksum)

Lorsqu'on détecte une erreur, il y a plusieurs possibilités:

- Retransmettre le message
- Corriger l'erreur (processus souvent difficile)

Lors de l'utilisation d'une somme de contrôle, on ajoute au message utile un
(ou des) bit(s) de contrôle qui permettent de vérifier selon un certain critère
et avec une très haute probabilité que le message reçu est correct.

## Bit de parité

Le bit de parité est un exemple de somme de contrôle.\
Critère: il doit toujours y avoir un nombre pair de bits 1.

### Exemple {num1}`exemple`

On veut transmettre un message utile de 4 bits $B(5, 4)$.\
$u$ = 4 bits, $c$ = 1 bit et donc $m = u + c = 4 + 1 = 5$ bits.

| message utile | message codé | nombre de bits à 1 |
| :-----------: | :----------: | :----------------: |
| 0000          | 0000<span style="color:red">0</span>| 0 |
| 1011          | 1011<span style="color:red">1</span>| 4 |
| 1100          | 1100<span style="color:red">0</span>| 2 |
| 0010          | 0010<span style="color:red">1</span>| 2 |

Capacité de détection:\
Avec le bit de parité, on peut détecter un nombre impair d'erreurs. Il n'est pas
possible de détecter un nombre pair d'erreurs.
$$C_d = 1$$

Efficacité:\
$$\dfrac{u}{m} = \dfrac{4}{5} = 80 \%$$

### Exercice {num1}`exercice`

On utilise un code $B(5, 4)$ où on ajoute à un message utile de 4 bits et 1 bit
de parité. La somme doit être paire.

Les messages suivants sont-ils corrects?

<script type="module">
const [core, quiz] = await tdoc.imports('tdoc/core.js', 'tdoc/quiz.js');

function parity(msg) {
    let p = 0;
    while (msg !== 0) {
        p ^= msg & 1;
        msg >>= 1;
    }
    return p;
}

function check(min, max, p) {
    return () => {
        const bits = Math.floor(min + 1 + Math.random() * (max - min  + 1));
        const msg = Math.floor(Math.random() * (1 << bits));
        const correct = parity(msg) ^ p;
        return {
            msg,
            equal(other) { return other.msg === msg; },
            history: (max - min + 1) / 2,

            msg(ph) { ph.textContent = core.toRadix(msg, 2, bits); },
            correct(args) {
                args.ok = {'oui': 0, 'non': 1}[args.answer] === correct;
            },
        };
    };
}

function encode(min, max, p) {
    return () => {
        const bits = Math.floor(min + Math.random() * (max - min  + 1));
        const msg = Math.floor(Math.random() * (1 << bits));
        const encoded = core.toRadix((msg << 1) | (parity(msg) ^ p), 2,
                                     bits + 1);
        return {
            msg,
            equal(other) { return other.msg === msg; },
            history: (max - min + 1) / 2,

            msg(ph) { ph.textContent = core.toRadix(msg, 2, bits); },
            encoded(args) {
                args.ok = args.answer.trim() === encoded;
            },
        };
    };
}

quiz.generator('parity-check-4', check(4, 4, 0));
quiz.generator('parity-check-4-9', check(4, 9, 0));
quiz.generator('parity-encode', encode(4, 9, 0));
</script>

```{role} oui-non(quiz-select)
:options: |
: oui
: non
```

```{quiz} table parity-check-4
| message reçu   | correct?           |
| :------------: | :----------------: |
| {quiz-ph}`msg` | {oui-non}`correct` |
```

### Exercice {num1}`exercice`

On utilise différents codes $B(n + 1, n)$ où on ajoute à un message utile de
$n$ bits et 1 bit de parité. La somme doit être paire.

Les messages suivants sont-ils corrects?

```{quiz} table parity-check-4-9
| message reçu   | correct?           |
| :------------: | :----------------: |
| {quiz-ph}`msg` | {oui-non}`correct` |
```

### Exercice {num1}`exercice`

On utilise différents codes $B(n + 1, n)$ où on ajoute à un message utile de
$n$ bits et 1 bit de parité. La somme doit être paire.

Encodez les messages suivants.

```{role} input(quiz-input)
:style: width: 8rem;
```

```{quiz} table parity-encode
| message        | message encodé   |
| :------------: | :--------------: |
| {quiz-ph}`msg` | {input}`encoded` |
```

### Exercice {num1}`exercice`

On considère le code $B(5, 4)$.

```{role} input(quiz-input)
:right: width: 5rem;
:check: split remove lowercase
```
```{role} select(quiz-select)
:right:
:options: |
: oui
: non
```

```{quiz}
1.  {input}`80%,4/5,0.8`
    Quelle est l'efficacité de ce code?
2.  {select}`non`
    S'il y a 1 erreur, le récepteur considère-t-il que le message reçu est
    correct?
3.  {select}`oui`
    S'il y a 2 erreurs, le récepteur considère-t-il que lemessage reçu est
    correct?
4.  {select}`non`
    S'il y a 3 erreurs, le récepteur considère-t-il que le message reçu est
    correct?
5.  {select}`oui`
    S'il y a 4 erreurs, le récepteur considère-t-il que le message reçu est
    correct?
6.  {select}`non`
    S'il y a 5 erreurs, le récepteur considère-t-il que le message reçu est
    correct?
7.  {input}`1`
    Quelle est la capacité de détection $C_d$ de $B(5, 4)$?
```

### Exercice {num1}`exercice`

On ajoute à un message utile de $n$ chiffres un chiffre de contrôle pour que la
somme soit un multiple de 10. Pour chacun des messages suivants, indiquez la
somme et déterminez si le message est correct.

<script type="module">
const [core, quiz] = await tdoc.imports('tdoc/core.js', 'tdoc/quiz.js');
const debug = false;

// Compute the sum of the digits of the given message.
function digitSum(msg) {
    let s = 0;
    while (msg !== 0) {
        s += msg % 10;
        msg = Math.floor(msg / 10);
    }
    return s;
}

// Compute the Luhn sum of the given message.
function luhnSum(msg) {
    let s = 0, double = false;
    while (msg !== 0) {
        let d = msg % 10;
        if (double) d *= 2;
        s += d % 10 + Math.floor(d / 10);
        msg = Math.floor(msg / 10);
        double = !double;
    }
    return s;
}

// Encode a message such that the given sum has `last` as the least
// significant digit.
function sumEncode(msg, fnSum, last = 0) {
    msg *= 10;
    return msg + (10 - fnSum(msg) % 10 + last) % 10;
}

// Generate a random decimal message.
function randomDecimal(digits) {
    const mag = 10 ** (digits - 1);
    return Math.floor(mag + Math.random() * 9 * mag);
}

function check(fnSum, min, max) {
    return () => {
        // Generate a new random message, with a 0.5 probability of being
        // correct.
        const msg = sumEncode(
            randomDecimal(core.randomInt(min, max)), fnSum,
                          Math.random() < 0.5 ? 0 : core.randomInt(1, 9));
        const sum = fnSum(msg);
        if (debug) console.log(`${msg} => ${sum}`);
        return {
            msg,
            equal(other) { return other.msg === msg; },
            history: 10 ** (min - 1) / 2,

            msg(ph) { ph.textContent = `${msg}`; },
            sum(args) { args.ok =  args.answer.trim() === sum.toString(); },
            correct(args) {
                args.ok = {'oui': true, 'non': false}[args.answer]
                          === (sum % 10 === 0);
            },
        };
    };
}

function encode(fnSum, min, max) {
    return () => {
        // Generate a new random message.
        const msg = randomDecimal(core.randomInt(min, max));
        const encoded = sumEncode(msg, fnSum);
        if (debug) console.log(`${msg} => ${encoded}`);
        return {
            msg,
            equal(other) { return other.msg === msg; },
            history: 10 ** (min - 1) / 2,

            msg(ph) { ph.textContent = `${msg}`; },
            encoded(args) {
                args.ok = args.answer.trim() === encoded.toString();
            },
        };
    };
}

quiz.generator('sum-digit-check', check(digitSum, 4, 9));
quiz.generator('sum-digit-encode', encode(digitSum, 4, 9));
quiz.generator('sum-luhn-check', check(luhnSum, 4, 9));
quiz.generator('sum-luhn-encode', encode(luhnSum, 4, 9));
</script>

```{role} input(quiz-input)
:style: width: 4rem;
```

```{quiz} table sum-digit-check
| message reçu   | somme        | correct?           |
| :------------: | :----------: | :----------------: |
| {quiz-ph}`msg` | {input}`sum` | {oui-non}`correct` |
```

### Exercice {num1}`exercice`

Sachant que le critère pour la somme de contrôle est que la somme doit être un
multiple de 10, encodez les messages suivants.

```{role} input(quiz-input)
:style: width: 10rem;
```

```{quiz} table sum-digit-encode
| message        | message encodé   |
| :------------: | :--------------: |
| {quiz-ph}`msg` | {input}`encoded` |
```

### Exercice {num1}`exercice`

La technique de la somme de contrôle permet-elle de détecter:

1.  une erreur dans un chiffre?
2.  deux erreurs dans deux chiffres?
3.  la permutation de deux chiffres?

```{solution}
1.  Oui, une erreur unique est toujours détectée.
2.  Pas toujours. Si l'erreur d'un chiffre "compense" celle de l'autre.\
    Exemple: 476355 et
    <span style="color:red">8</span>7<span style="color:red">2</span>355
    ont la même somme de contrôle.
3.  Non, une permutation n'est pas détectée.
```

## Algorithme de Luhn

L'algorithme de Luhn est un autre exemple de somme de contrôle. Il consiste à
doubler un chiffre sur deux, puis de faire une somme de contrôle sur les
chiffres ainsi obtenus (la somme doit être un multiple de 10).

Pour déterminer quels chiffres sont doublés, on part de la fin, et le chiffre de
contrôle n'est jamais doublé.

Cet algorithme est notamment utilisé pour valider les numéros de carte de
crédit.

### Exemple {num1}`exemple`

Exemples de décodage

| message reçu | message modifié | somme des chiffres | correct? |
| :----------: | :-------------: | :----------------: | :------: |
| 123789       | <b>2</b>2<b>6</b>7<b>16</b>9 | 2 + 2 + 6 + 7 + 1 + 6 + 9 = 33 | non |
| 67892        | 6<b>14</b>8<b>18</b>2 | 6 + 1 + 4 + 8 + 1 + 8 + 2 = 30 | oui |

### Exercice {num1}`exercice`

Calculez la somme selon l'algorithme de Luhn des messages suivants et déterminez
si le message est correct.

```{role} input(quiz-input)
:style: width: 4rem;
```

```{quiz} table sum-luhn-check
| message reçu   | somme        | correct?           |
| :------------: | :----------: | :----------------: |
| {quiz-ph}`msg` | {input}`sum` | {oui-non}`correct` |
```

### Exercice {num1}`exercice`

En utilisant l'algorithme de Luhn, encodez les messages suivants.

```{role} input(quiz-input)
:style: width: 10rem;
```

```{quiz} table sum-luhn-encode
| message        | message encodé   |
| :------------: | :--------------: |
| {quiz-ph}`msg` | {input}`encoded` |
```

### Exercice {num1}`exercice`

L'algorithme de Luhn permet-il de détecter:

1.  une erreur dans un chiffre?
2.  la permutation de deux chiffres consécutifs?

```{solution}
1.  Oui, une erreur unique est toujours détectée.
2.  Oui, une permutation de deux chiffres consécutifs est toujours détectée, car
    l'un est doublé dans la somme, alors que l'autre pas.\
    Exemple:\
    4713, la somme vaut $8 + 7 + 2 + 3 =  20$ &#8658; correct\
    <span style="color:red">7</span><span style="color:red">4</span>13, la somme
    vaut $1 + 4 + 4 + 2 + 3 = 14$ &#8658; faux
```

### Exercice {num1}`exercice`

Les cartes de crédit suivantes sont-elles valides?

<table><tr><td>

```{figure} images/carte1.png
:alt: Carte de crédit 1
:width: 80%
:align: center
```

</td><td>

```{figure} images/carte2.png
:alt: Carte de crédit 2
:width: 80%
:align: center
```
</td></tr></table>

```{solution}
1.  Numéro de carte: 4703 1234 5678 9991\
    Numéro modifié:
    <b>8</b>7<b>0</b>3 <b>2</b>2<b>6</b>4 <b>10</b>6<b>14</b>8
    <b>18</b>9<b>18</b>1\
    Somme: $8+7+0+3+2+2+6+4+1+0+6+1+4+8+1+8+9+1+8+1 = 80$\
    Ce numéro est correct.
2.  Numéro de carte: 4970 1012 3456 7890\
    Numéro modifié:
    <b>8</b>9<b>14</b>0 <b>2</b>0<b>2</b>2 <b>6</b>4<b>10</b>6
    <b>14</b>8<b>18</b>0\
    Somme: $8+9+1+4+0+2+0+2+2+6+4+1+0+6+1+4+8+1+8+0 = 76$\
    Ce numéro est faux.
```
