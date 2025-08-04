% Copyright 2025 Brice Canvel
% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Labo - codes détecteurs et correcteurs d'erreur

## Code binaire

Un code binaire a été défini pour coder des messages:

|     | 00  | 01  | 10  | 11  |
| :-: | :-: | :-: | :-: | :-: |
| <b>00</b>  | Alice  | Bob  | Max | Mathilde |
| <b>01</b>  | mange  | prépare  | écrit | imagine |
| <b>10</b>  | un hamburger  | un texte  | un programme | un roman |
| <b>11</b>  | végétarien  | anglais  | compliqué | épique |

### Exemple {nump}`exemple`

| Mathilde | prépare | un roman | anglais |
| :------: | :--: | :------: | :-----: |
| 0011     | 0101 | 1011     | 1101    |


## Bit de parité

### Exercice {nump}`exercice`

En utilisant les fiches transmises par l'enseignant.e:

1.  Composez une phrase de 4 "mots" appartenant au tableau ci-dessus.
2.  Codez-là en incluant le bit à chaque "mot".
3.  Donnez le code noté au crayon à votre enseignant.e qui la transmettra à un
    autre élève pour la décoder.

Document pour l'enseignant.e: [`Fiche de l'élève pour la parité`](fiche-parite.pdf)

### Exercice {nump}`exercice`

Vous allez recevoir un message codé:
1.  Contrôlez que le message est correct en vérifiant la parité.
2.  Décodez le message.
3.  Allez voir l'expéditeur du message pour comparer votre résultat avec le
    message qui a effectivement été envoyé. Que s'est-il passé?

## Code de Hamming

### Exercice {nump}`exercice`

En utilisant les fiches transmises par l'enseignant.e:

1.  Composez une phrase de 4 "mots" appartenant au tableau ci-dessus.
2.  Codez-là en utilisant le code de Hamming.
3.  Donnez le code noté au crayon à votre enseignant.e qui la transmettra à un
    autre élève pour la décoder.

Document pour l'enseignant.e: [`Fiche de l'élève pour Hamming`](fiche-hamming.pdf)

### Exercice {nump}`exercice`

Vous allez recevoir un message codé.

En utilisant les fiches transmises par l'enseignant.e:

1.  Décodez le message en utilisant le code de Hamming.
2.  Allez voir l'expéditeur du message pour comparer votre résultat avec le
    message qui a effectivement été envoyé.

