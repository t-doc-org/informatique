% Copyright 2026 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Données et réseaux

```{metadata}
subject: "Informatique 2e année"
print-styles: tdoc/print-exam.css
page-break-force: 1
page-break-avoid: 2
```

```{include} /_include/entete-examen.export.md
```
```{class} align-center
**Détails des calculs obligatoires. Attention au soin. Calculatrice autorisée.**
```
---

## Question {nump}`question`{points}`4`


1.  Vous souhaitez envoyer les messages suivants en ajoutant 1 bit de parité aux
    messages utiles donnés ci-dessous.<br>

    {.lower-alpha-paren}
    1.  Message utile: $1000$ {hspace}`3em` message encodé:
    2.  Message utile: $11111111$ {hspace}`3em` message encodé:


2.  Vous avez reçu les messages suivants qui utilisent un bit de parité.<br>
    Les messages sont-ils corrects? Justifiez.

    {.lower-alpha-paren}
    1.  $1101$
    2.  $101011$

```{solution}
1.  {.lower-alpha-paren}
    1. $10001$
    2. $111111110$
2.  {.lower-alpha-paren}
    1. Pas correct, car il y a un nombre impair (3) bits à 1.
    2. Correct, car il y a un nombre pair (4) bits à 1.
```

## Question {nump}`question`{points}`4`

```{code} text
Algorithme de Luhn:

Il consiste à doubler un chiffre sur deux, puis de faire une somme de contrôle
sur les chiffres ainsi obtenus (la somme doit être un multiple de 10).
Pour déterminer quels chiffres sont doublés, on part de la fin, et le chiffre de
contrôle n'est jamais doublé.
```

{.lower-alpha-paren}
1.  Le message reçu suivant $123789$ est-il correct? Justifiez.
2.  Encodez le message suivant $931502$ en utilisant l'algorithme de Luhn.

```{solution}
{.lower-alpha-paren}
1.  $2+2+6+7+1+6+9 = 33$ n'est pas un multiple de $10$.<br>
    Le message n'est donc pas correct.
2.  $9+6+1+1+0+0+4=21$<br>
    Message encodé: $9315029$
```

## Question {nump}`question`{points}`2`

Répondez par vrai ou faux et justifiez.

{.lower-alpha-paren}
1.  Avec un bit de parité, il est possible de corriger une erreur.
2.  Avec l'algorithme de Luhn, une permutation de deux chiffres consécutifs est
    toujours détectée.

```{solution}
{.lower-alpha-paren}
1.  Non, un bit de parité permet seulement de détecter un erreur, si le nombre
    de bits à 1 n'est pas pair, mais il n'est pas possible de savoir où est
    l'erreur.
2.  Oui, car un des chiffres est doublé, alors que l'autre pas pour le calcul du
    bit de parité.
```

## Question {nump}`question`{points}`6`

````{list-grid}
:style: |
: grid-template-columns: 1fr 1fr; align-items: center;
: margin-bottom: 0;
- ```{figure} images/hamming6.svg
  :alt: Bits de contrôle
  :width: 60%
  :align: center
  ```
- ```{figure} images/hamming1.svg
  :alt: Bits de contrôle
  :width: 60%
  :align: center
  ```
````

{.lower-alpha-paren}
1.  Encodez le message suivant $0111$ en utilisant le code de Hamming $H(7, 4)$
2.  Décodez le message reçu suivant $0111110$ utilisant le code de Hamming
    $H(7, 4)$ en complétant le tableau ci-dessous.
    |message reçu|$p_1$|$p_2$|$p_3$|bit erroné|message corrigé|message décodé|
    |:----------:|:---:|:---:|:---:|:--------:|:-------------:|:------------:|
    |  <br>      |     |     |     |          |               |              |


````{solution}
{.lower-alpha-paren}
1.  $p_1=0$, $p_2=0$ et $p_3=1$, Message encodé: $0001111$
2.  |message reçu|$p_1$|$p_2$|$p_3$|bit erroné|message corrigé|message décodé|
    |:----------:|:---:|:---:|:---:|:--------:|:-------------:|:------------:|
    | $0111110$  | $0$ | $0$ | $0$ | 6/$d_3$  |  $0111100$    |   $1100$     |
````

## Question {nump}`question`{points}`2`

Combien de fichier MP3 de 4 Mo en moyenne peut-on stocker sur un disque dur de
$32$ Go?

```{solution}
$32 \text{ Go} = 32\,000 \text{Mo}$

Nombre de fichiers: $\dfrac{32\,000}{4} = 8\,000$ fichiers
```

## Question {nump}`question`{points}`2`

Citez un avantage et un inconvénient des transmissions par Wi-Fi.

```{solution}
Avantages: pas besoin de câbles, installation facile / mobilité.

Inconvénients: pas très rapide / sujet aux interférences.
```

## Question {nump}`question`{points}`2`

Reliez, si possible, chaque équipement à son rôle:

```{list-grid}
:style: |
: grid-template-columns: 1fr 0fr 0fr 0fr 6fr;

- Routeur
- &#9679;
- {hspace}`3em`
- &#9679;
- convertit les données numériques en signal modulé analogique et vice-versa
- Modem
- &#9679;
- {hspace}`3em`
- &#9679;
- pont entre le réseau filaire et le réseau sans fil
- Switch
- &#9679;
- {hspace}`3em`
- &#9679;
- permet à deux réseaux qui fonctionnent différemment de se comprendre
- Borne Wi-Fi
- &#9679;
- {hspace}`3em`
- &#9679;
- interconnecte plusieurs appareils sur un même réseau
```

```{solution}
Modem: convertit les données numériques en signal modulé analogique et vice-versa

Switch: interconnecte plusieurs appareils sur un même réseau

Borne Wi-Fi: pont entre le réseau filaire et le réseau sans fil
```

## Question {nump}`question`{points}`2`

Bob souhaite envoyer une impression sur une imprimante du même réseau local.
Expliquez comment cela se passe (Quelles informations sont transmises? Par quels
équipements transitent les données?).

```{solution}
Le message est découpé en paquets auxquels sont ajoutés l'adresse de
l'imprimante et celle de l'expéditeur.

L'ordinateur envoie les paquets au switch qui les transmets ensuite directement
à l'imprimante.
```

## Question {nump}`question`{points}`2`

Cochez la bonne réponse:

```{list-grid}
:style: |
: grid-template-columns: 5fr 1fr 1fr;

- Les adresses IPv4 sont de la forme 156.25.4.255.
- &#9744; Vrai
- &#9744; Faux
- Toutes les adresses IP sont uniques.
- &#9744; Vrai
- &#9744; Faux
- Deux machines dans un même sous-réseau peuvent avoir la même adresse IP privée.
- &#9744; Vrai
- &#9744; Faux
- Un DNS est un service qui associe les noms de domaine internet à leur adresse
  IP.
- &#9744; Vrai
- &#9744; Faux
```

```{solution}
Vrai, Faux, Faux, Vrai
```
