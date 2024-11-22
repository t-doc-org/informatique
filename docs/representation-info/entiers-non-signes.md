% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Nombres entiers non signés

Dans un premier temps, nous travaillerons avec les nombres entiers positifs,
appelés entiers non signés.

## Les différentes bases: décimal, binaire et hexadécimal

Dans la vie de tous les jours, nous utilisons habituellement la base 10. Ça
signifie que nous avons 10 symboles (les chiffres de 0 à 9) à disposition pour
écrire les nombres.

$7356 = 7000 + 300 + 50 + 6 = 7 \cdot 10^3 + 3 \cdot 10^2 + 5 \cdot 10^1 + 6 \cdot 10^0$

En informatique, nous utilisons souvent la base 2 (binaire). Les deux seuls
symboles à disposition sont le 0 et le 1.

$10101_2 = 1 \cdot 2^4 + 0 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0$

Une autre base beaucoup utilisée en informatique pour sa simplicité
d'utilisation et de représentation est la base 16 (hexadécimal). Pour la base
16, nous avons besoin de 16 symboles, nous en avons déjà 10 à disposition (0
à 9), il faut donc 6 symboles supplémentaires qui sont A (pour 10), B (11), C
(12), D (13), E (14) et F (15).

$3A7E0_{16} = 3 \cdot 16^4 + 10 \cdot 16^3 + 7 \cdot 16^2 + 14 \cdot 16^1 + 0 \cdot 16^0$

```{important}
Lorsque nous utilisons une autre base que la base 10, nous écrivons la base en
indice pour éviter toute ambiguïté.\
$100 \neq 100_2$, l'un est 100 et l'autre 4 en base 2.
```

## Conversion binaire - décimal

Pour convertir un nombre binaire en nombre décimal, il faut:
1. Écrire le nombre sous forme de puissances de 2,
2. Calculer les valeurs,
3. Additionner le tout.

$$
1101101_2 &= 1 \cdot 2^6 + 1 \cdot 2^5 + 0 \cdot 2^4 + 1 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0\\
          &= 64 + 32 + 0 + 8 + 4 + 0 + 1 = 109
$$

## Exercice {num}`exo-info`

Convertir les nombres suivants de binaire en décimal.

```{exec} python
:name: info-question
:when: never
:class: hidden
async def question(*solutions, format='{}'):
  solutions = [format.format(s) for s in solutions]
  while True:
    resp = await input_line("Réponse:")
    if resp.replace(" ", "").lower() in solutions: break
    print("\x0cEssaie encore")
  print("\x0cBravo")
```

1.  $10_2$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0b10)
    ```

2.  $101_2$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0b101)
    ```

3.  $1111_2$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0b1111)
    ```

4.  $1001_2$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0b1001)
    ```

5.  $0110_2$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0b0110)
    ```

6.  $1101_2$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0b1101)
    ```

7.  $1010101_2$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0b1010101)
    ```

8.  $1100110_2$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0b1100110)
    ```

## Conversion décimal - binaire

Pour convertir un nombre décimal en nombre binaire, il existe plusieurs
méthodes.

Le but est de décomposer le nombre décimal en puissances de 2. Pour cela nous
allons nous aider d'un tableau:

1. Noter les puissances de 2 dans le tableau.
2. Depuis la gauche, déterminer pour chaque colonne si la puissance de 2 est
plus petite ou égale au reste.
3. Calculer le reste.
4. Passer à la colonne suivante.

Que vaut $149$ en binaire?

| $2^n$             | $2^8$ | $2^7$ | $2^6$ | $2^5$ | $2^4$ | $2^3$ | $2^2$ | $2^1$ | $2^0$ |
| :---------------: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|                   | 256   | 128   | 64    | 32    | 16    | 8     | 4     | 2     | 1     |
| $2^n \leq$ reste? | 0     | 1     | 0     | 0     | 1     | 0     | 1     | 0     | 1     |
| Reste             | $149$ | $21$  | $21$  | $21$  | $5$   | $5$   | $1$   | $1$   | $0$   |

$$149 = 10010101_2$$

```{youtube} ysoWgx186DM
:title: Vidéo sur le binaire
```

## Exercice {num}`exo-info`

Convertir les nombres suivants de décimal en binaire.

1.  $3$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(3, format='{:b}')
    ```

2.  $6$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(6, format='{:b}')
    ```

3.  $9$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(9, format='{:b}')
    ```

4.  $41$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(41, format='{:b}')
    ```

5.  $64$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(64, format='{:b}')
    ```

6.  $171$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(171, format='{:b}')
    ```

7.  $720$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(720, format='{:b}')
    ```

8.  $1573$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(1573, format='{:b}')
    ```

## Exercice {num}`exo-info`

Combien de bits faut-il pour écrire les nombres suivants en base 2?

1.  $13$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question("4", "4bits")
    ```

2.  $37$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question("6", "6bits")
    ```

3.  $128$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question("8", "8bits")
    ```

4.  $350$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question("9", "9bits")
    ```

## Conversion binaire - hexadécimal

Pour convertir un nombre binaire en hexadécimal, il suffit de grouper les bits
par 4 depuis la droite et de calculer leur valeur en hexadécimal.

Que vaut 1101110 en hexadécimal?

| binaire       | 0110 | 1110 |
|---------------|:----:|:----:|
| pseudo-décimal| 6    | 14   |
| hexadécimal   | 6    | E    |

$$1101110_{2} = 6E_{16}$$

## Conversion hexadécimal - binaire

Pour convertir un nombre hexadécimal en binaire, il suffit de remplacer chaque
chiffre hexadécimal par sa valeur en binaire sur 4 bits.

Que vaut A0D7 en binaire?

| hexadécimal   | A    | 0    | D    | 7    |
|---------------|:----:|:----:|:----:|:----:|
| pseudo-décimal| 10   | 0    | 13   | 7    |
| binaire       | 1010 | 0000 | 1101 | 0111 |

$$A0D7_{16} = 1010\,0000\,1101\,0111_{2}$$

## Exercice {num}`exo-info`

Convertir les nombres suivants de binaire en hexadécimal ou vice-versa.

1.  $1000\,0111_2$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0b10000111, format='{:x}')
    ```

2.  $0101\,1010_2$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0b01011010, format='{:x}')
    ```

3.  $1001\,1111_2$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0b10011111, format='{:x}')
    ```

4.  $0111\,0001\,1110\,1001_2$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0b0111000111101001, format='{:x}')
    ```

5.  $3A_{16}$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0x3a, format='{:b}')
    ```

6.  $F4_{16}$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0xf4, format='{:b}')
    ```

7.  $BD_{16}$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0xbd, format='{:b}')
    ```

8.  $9C\,2E_{16}$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0x9c2e, format='{:b}')
    ```

## L'addition de nombres entiers en binaire

Le principe pour additionner des nombres en binaire est le même que pour
additionner en base 10, sauf que la retenue se produit dès que nous arrivons à 2
au lieu de 10.\
Voici les quelques règles importantes de l'addition en binaire:

- 0 + 0 = 0
- 0 + 1 = 1 + 0 = 1
- 1 + 1 = 10
- 1 + 1 + 1 = 11

Comment additionner $1011_2$ et $0011_2$?

```{code-block} text
     1 1     (retenues)
   1 0 1 1
 + 0 0 1 1
 ---------
   1 1 1 0
```

$$0101_2 + 1001_2 = 1110_2$$

## Le dépassement de capacité (overflow)

En additionnant deux nombres entiers non signés en base 2 sur 4 bits, il peut se
produire un dépassement de capacité.

Que se passe-t-il lors de l'addition de $1101_2$ et de $1010_2$?

```{code-block} text
 1           (retenues)
   1 1 0 1
 + 1 0 1 0
 ---------
 1 0 1 1 1
```

$1101_2 + 1010_2 = \cancel{1}0111_2$, mais comme nous n'avons que 4 bits à
disposition et pas 5, le premier bit va simplement être ignoré et donc le
résultat sera faux ($13 + 12 \ne 7$).

Un exemple coûteux d'overflow est le [vol 501 d'Ariane 5](https://fr.wikipedia.org/wiki/Vol_501_d%27Ariane_5).

## Exercice {num}`exo-info`

Effectuer les additions suivantes sur 4 bits.

1.  $0010 + 0011$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0b0010 + 0b0011, format='{:04b}')
    ```

2.  $0101 + 1000$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0b0101 + 0b1000, format='{:04b}')
    ```

3.  $1011 + 0001$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0b1011 + 0b0001, format='{:04b}')
    ```

4.  $1111 + 1000$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question("overflow")
    ```

## Exercice {num}`exo-info`

Effectuer les additions suivantes sur 8 bits.

1.  $0110\,0110 + 0011\,0010$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0b01100110 + 0b00110010, format='{:08b}')
    ```

2.  $0101\,1111 + 1000\,0000$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0b01011111 + 0b10000000, format='{:08b}')
    ```

3.  $1011\,0001 + 0010\,1101$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0b10110001 + 0b00101101, format='{:08b}')
    ```

4.  $0011\,1100 + 0110\,0101$

    ```{exec} python
    :when: load
    :after: info-question
    :class: hidden
    await question(0b00111100 + 0b01100101, format='{:08b}')
    ```
