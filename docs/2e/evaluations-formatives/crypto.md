% Copyright 2026 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Cryptographie

```{include} /_include/entete-examen.export.md
```
```{class} align-center
**Détails des calculs obligatoires. Attention au soin. Calculatrice autorisée.**
```
---

## Question {nump}`question`{points}`10`

Répondez aux questions:

{.lower-alpha-paren}
1.  Expliquez la différence entre la stéganographie et la cryptographie. Donnez
    un exemple de chacune d'elle.
2.  Pourquoi l'analyse de fréquences ne permet-elle pas de décrypter n'importe
    quel message?
3.  À quoi sert la clé publique dans le système RSA? Et la clé privée?
4.  Sachant que votre clé publique est (187, 7) et votre clé privée est
    (11, 17, 183), quel calcul faut-il effectuer pour déchiffrer le message codé
    suivant: **145**.
5.  La cryptographie moderne utilise-t-elle la cryptographie symétrique, la
    cryptographie asymétrique ou les deux? Expliquez pourquoi.


```{solution}
{.lower-alpha-paren}
1.  La stéganographie consiste à cacher l'existence d'un message, alors que la
    cryptographie chiffre un message.<br>
    Exemples de stéganographie: tatouage sur le crâne, tablette de cire, ...<br>
    Exemple de cryptographie: scytale, chiffre de César, ...
2.  L'analyde de fréquence fonctionne seulement pour les substitutions
    monoalphabétiques. Dans les autres cas, une lettre n'est pas toujours
    remplacée par le même symbole et donc l'analyse ne permet pas de savoir
    que, par exemple, le symbole le plus fréquent est forcément un e.
3.  La clé publique permet de chiffrer un message, alors que la clé privée
    permet de déchiffrer le message.
4.  $m = 145^183 mod (11 * 17)$
5.  La cryptographie utilise les deux. Elle utilise la cryptographie asymétrique
    lors de l'échange des clés pour ensuite utiliser la crytographie sysmétrique
    qui est beaucoup plus rapide.
```

## Question {nump}`question`{points}`5`

En expliquant ce que vous faites, déchiffrez le message suivant codé avec le
chiffre de Rail Fence avec une clé de chiffrement de 3:

**CTRSE DEECO LUSES IRSUR CTXRI EOAUA OEEC**

````{solution}
```{code-block} text
c   t   r   s   e   d   e   e   c
 o l u s e s i r s u r c t x r i e
  o   a   u   a   o   e   e   c
```

Cool tu as reussi a resoudre cet exercice
````

## Question {nump}`question`{points}`5`

En expliquant ce que vous faites, chiffrez le message suivant avec le chiffre de
Vigenère.

Clé de chiffrement:  **info**

Message: **mode sans echec**


```{solution}
UBISA NSGMP MSK
```

## Question {nump}`question`{points}`5`

Un texte a été codé avec le chiffre de César, mais pas le décalage standard de 3
positions. Au moyen de l'analyse de fréquences et des fréquences d'apparition
des lettres en français, décryptez le message suivant en expliquant ce que vous
faites:

**TMRTA ATCIS TRGNE IPVTG TJHHX**

````{list-grid}
:style: grid-template-columns: 1fr 1fr;
- ```{figure} images/frequences.png
  :align: center
  ```
- ```{figure} images/apparition.png
  :align: center
  ```
`````

```{solution}
Le décalage est de 15 positions et la phrase est:

excellent decryptage reussi
```
