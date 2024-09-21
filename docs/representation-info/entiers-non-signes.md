<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

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

$10101 = 1 \cdot 2^4 + 0 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0$

Une autre base beaucoup utilisée en informatique pour sa simplicité
d'utilisation et de représentation est la base 16 (hexadécimal). Pour la base
16, nous avons besoin de 16 caractères, nous en avons déjà 10 à disposition (0
à 9), il faut donc 6 symboles supplémentaires qui sont A (pour 10), B (11), C
(12), D (13), E (14) et F (15).

$3A7E0 = 3 \cdot 16^4 + 10 \cdot 16^3 + 7 \cdot 16^2 + 14 \cdot 16^1 + 0 \cdot 16^0$

## Conversion binaire - décimal

Pour convertir un nombre binaire en nombre décimal, il faut:
1. Écrire le nombre sous forme de puissances de 2,
2. Calculer les valeurs,
3. Additionner le tout.

$1101101_2 = 1 \cdot 2^6 + 1 \cdot 2^5 + 0 \cdot 2^4 + 1 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0$\
$= 64 + 32 + 0 + 8 + 4 + 0 + 1 = 109_{10}$

<!--
## Exercice 1
Convertir les nombres suivants de binaire en décimal.
1. $10_2$
2. $101_2$
3. $1111_2$
4. $1001_2$
5. $0110_2$
6. $1101_2$
7. $1010101_2$
8. $1100110_2$
-->

## Conversion décimal - binaire

Pour convertir un nombre décimal en nombre binaire, il existe plusieurs méthodes.

Le but est de décomposer le nombre décimal en puissances de 2. Pour cela nous
allons nous aider d'un tableau:

1. Noter les puissances de 2 dans le tableau.
2. Depuis la gauche, déterminer pour chaque colonne si la puissance de 2 est
plus petite ou égale au reste.
3. Calculer le reste.
4. Passer à la colonne suivante.

Que vaut $149_{10}$ en binaire?

| $2^n$             |  $2^8$ | $2^7$        | $2^6$ | $2^5$ | $2^4$     | $2^3$ | $2^2$   | $2^1$ | $2^0$   |
| :------:          | :---:  | :---:        | :---: | :---: | :---:     | :---: | :---:   | :---: | :---:   |
|                   | 256    | 128          | 64    | 32    | 16        | 8     | 4       | 2     | 1       |
| $2^n \leq$ reste? | 0      | 1            | 0     | 0     | 1         | 0     | 1       | 0     | 1       |
| Reste             | $149$  | $149-128=21$ | $21$  | $21$  | $21-16=5$ | $5$   | $5-4=1$ | $1$   | $1-1=0$ |

$149_{10} = 10010101_2$


<!--
## Exercice 2
Convertir les nombres suivants de décimal en binaire.
- $3_{10}$
- $6_{10}$
- $9_{10}$
- $41_{10}$
- $64_{10}$
- $171_{10}$
- $720_{10}$
- $1573_{10}$

## Exercice 3
Combien de bits faut-il pour écrire les nombres suivants en base 2?
- $13$
- $37$
- $128$
- $350$

-->

## Conversion binaire - hexadécimal

Pour convertir un nombre binaire en hexadécimal, il suffit de grouper les bits par 4 depuis la droite et de calculer leur valeur en hexadécimal.

Que vaut 1101110 en hexadécimal?

| binaire       | 0110 | 1110 |
|---------------|:----:|:----:|
| pseudo-décimal| 6    | 14   |
| hexadécimal   | 6    | E    |

$1101110_{2} = 6E_{16}$

## Conversion hexadécimal - binaire

Pour convertir un nombre hexadécimal en binaire, il suffit de remplacer chaque chiffre hexadécimal par sa valeur en binaire sur 4 bits.

Que vaut A0D7 en binaire?

| hexadécimal   | A    | 0    | D    | 7    |
|---------------|:----:|:----:|:----:|:----:|
| pseudo-décimal| 10   | 0    | 13   | 7    |
| binaire       | 1010 | 0000 | 1101 | 0111 |

$A0D7_{16} = 1010\,0000\,1101\,0111_{2}$

<!--
## Exercice 4
Convertir les nombres suivants en hexadécimal ou en binaire:
- $1000\,0111_2$
- $0101\,1010_2$
- $1001\,1111_2$
- $0111\,0001\,1110\,1001_2$
- $3A_{16}$
- $F4_{16}$
- $BD_{16}$
- $9C\,2E_{16}$
-->

## L'addition de nombres entiers en binaire

Le principe pour additionner des nombres en binaire est le même que pour
additionner en base 10, sauf que la retenue se produit dès que nous arrivons à 2
au lieu de 10.\
Voici les quelques règles importantes de l'addition en binaire:

- 0 + 0 = 0
- 0 + 1 = 1 + 0 = 1
- 1 + 1 = 10
- 1 + 1 + 1 = 11

Comment additionner $0101_2$ et $1001_2$?
```{code-block} text
   0 1 0 1
 + 1 0 0 1
 ---------
   1 1 1 0
```
$0101_2 + 1001_2 = 1110_2$

## Le dépassement de capacité (overflow)

En additionnant deux nombres entiers non signés en base 2 sur 4 bits, il peut se
produire un dépassement de capacité.

Que se passe-t-il lors de l'addition de $1101_2$ et de $1010_2$?
```{code-block} text
   1 1 0 1
 + 1 0 1 0
 ---------
 1 0 1 1 1
```
$1101_2 + 1010_2 = \cancel{1}0111_2$, mais comme nous n'avons que 4 bits à
dispositions et pas 5, le premier bit va être simplement ignoré et donc le
résultat sera faux ($13 + 12 \ne 7$).

Un exemple coûteux d'overflow est le [vol 501 d'Ariane 5](https://fr.wikipedia.org/wiki/Vol_501_d%27Ariane_5).

<!--
### Exercice 5
Effectuer les additions suivantes sur 4 bits:
- $0010 + 0011$
- $0101 + 1000$
- $1011 + 0001$
- $1111 + 1000$

### Exercice 6
Effectuer les additions suivantes sur 8 bits:
- $0110\,0110 + 0011\,0010$
- $0101\,1111 + 1000\,0000$
- $1011\,0001 + 0010\,1101$
- $0011\,1100 + 0110\,0101$
-->

