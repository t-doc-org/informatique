% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Cryptographie Lab

```{metadata}
hide-solutions: true
```

Dans le cours, nous avons vu plusieurs exemples de cryptographie symétrique et
asymétrique. Nous allons tester ces différents systèmes.

```{important}
Par convention, nous écrivons le texte en minuscules pour le message clair et en
majuscules pour le cryptogramme (texte chiffré).
```

## Exercice {num}`exo-crypto-lab`

**But:** Utilisation du chiffre de Rail Frence pour chiffrer et déchiffrer un
message.

Écrire un message pour un camarade de classe avec une clé de chiffrement de 3:

1. Chacun écrit un message qu'il chiffre et transmet à un autre élève.
2. Déchiffrer le message d'un autre élève.

## Exercice {num}`exo-crypto-lab`

**But:** Effectuer une analyse de fréquences pour décrypter un message codé avec un
chiffre de César.

Vous interceptez, sur le réseau public, un des messages suivants chiffré au moyen
du Chiffre de César.

Groupe 1:\
GOQVS NEISJ CHFSQ VWSBO RSDCG SEISZ EISGD SHWHS GPCAP SGDOF HCIHR OBGAC BXOFR
WBSHE ISQOA SQCBH FOFWS

Groupe 2:\
JMICK WCXLM KPWAM AMFQA BIQMV BRILQ AUIQA ICKCV LMKMC FYCQD QDMVB
ICRWC ZLPCQ VMAMV AWCDQ MVVMV B

Groupe 3:\
WYMNN LIJWU FGYDU CGYJU MNLIJ VYUOW IOJWU DJLYZ YLYKO UHXWY MNOHJ
YONLI JJFOM GICHM WUFGY

Groupe 4:\
ZCWRL KULTF LIRXV GFLIR WWIFE KVIJV JVEEV DZJDR ZJZCV EWRLK VETFI
VGCLJ GFLIR WWIFE KVIJV JRDZJ

Groupe 5:\
XSXKQ GBJBA FPXFP NRBJX SFBBQ XFQRK BQOXD BAFBG BJBOB KAPZL JMQBN
RBZBP QRKBZ LJBAF B

Groupe 6:\
QFANJ HJXYH TRRJZ SJGTN YJIJH MTHTQ FYXTS SJXFN YOFRF NXXZW VZTNT
SAFYT RGJW

1. Faire une analyse de fréquences. Vous pouvez utiliser le site suivant pour
   l'[analyse de fréquences](https://www.dcode.fr/analyse-frequences).
2. Déterminer la clé de chiffrement.
3. Déchiffrer le message.

```{solution}
1. GOQVS NEISJ CHFSQ VWSBO RSDCG SEISZ EISGD SHWHS GPCAP SGDOF HCIHR OBGAC BXOFR
WBSHE ISQOA SQCBH FOFWS\
**Clé:** décalage de 14\
**Texte clair:** sachez que votre chien a depose quelques petites bombes partout
dans  mon jardin et que ca me contrarie (Moi, moche et méchant)

2. JMICK WCXLM KPWAM AMFQA BIQMV BRILQ AUIQA ICKCV LMKMC FYCQD QDMVB ICRWC ZLPCQ
VMAMV AWCDQ MVVMV B\
**Clé:** décalage de 8\
**Texte clair:** beaucoup de choses existaient jadis mais aucun de ceux qui
vivent aujourd hui ne s en souviennent (Le Seigneur des anneaux)

3. WYMNN LIJWU FGYDU CGYJU MNLIJ VYUOW IOJWU DJLYZ YLYKO UHXWY MNOHJ YONLI JJFOM
GICHM WUFGY\
**Clé:** décalage de 20\
**Texte clair:** c est trop calme j aime pas trop beaucoup ca j prefere quand c
est un peu trop plus moins calme
(Astérix et Obélix mission Cléopatre)

4. ZCWRL KULTF LIRXV GFLIR WWIFE KVIJV JVEEV DZJDR ZJZCV EWRLK VETFI VGCLJ GFLIR
WWIFE KVIJV JRDZJ\
**Clé:** décalage de 17\
**Texte clair:** il faut du courage pour affronter ses ennemis mais il en faut
encore plus pour affronter ses amis (Harry Potter)

5. XSXKQ GBJBA FPXFP NRBJX SFBBQ XFQRK BQOXD BAFBG BJBOB KAPZL JMQBN RBZBP QRKBZ
LJBAF B\
**Clé:** décalage de 23\
**Texte clair:** avant je me disais que ma vie etait une tragedie je me rends
compte que c est une comedie (Joker)

6. QFANJ HJXYH TRRJZ SJGTN YJIJH MTHTQ FYXTS SJXFN YOFRF NXXZW VZTNT SAFYT RGJW
**Clé:** décalage de 5\
**Texte clair:** la vie c est comme une boite de chocolats on ne sait jamais sur
quoi on va tomber (Forrest Gump)
```

## Exercice {num}`exo-crypto-lab`

**But:** Décrypter un message utilisant la substitution monoalphabétique en
faisant une analyse de fréquences.

Décrypter à l'aide de l'analyse de fréquences, le cryptogramme suivant,
chiffré par une substitution monoalphabétique (cas général):

ZRJ VDAARJ CLWJJRCK RK ERARMHRCK ZWIHRJ RK RULMP RC EHDWKJ. ZRJ EWJKWCBKWDCJ
JDBWLZRJ CR FRMNRCK RKHR TDCERRJ GMR JMH Z'MKWZWKR BDAAMCR.

Les espaces et la ponctuation ont été laissés pour faciliter l'exercice.

1. Faire une [analyse de fréquences](https://www.dcode.fr/analyse-frequences)
   des lettres, des digrammes et des caractères répétés et utiliser les
   [tables de fréquences](frequences.md).
2. Décrypter le message.

````{tip}
Écrire un programme python qui permet de remplacer les lettres les unes après
les autres.
```{code-block} python
:linenos:
texte = "IMPLU SR KPXOR"
texte = texte.replace("R", "t")
print(texte)
```
Ce programme donnera:
```{code-block} text
IMPLU St KPXOt
```
````

```{solution}
**Texte clair:** les hommes naissent et demeurent libres et egaux en droits. les
distinctions sociales ne peuvent etre fondees que sur l'utilite commune.
```

## Exercice {num}`exo-crypto-lab`

**But:** Échanger un message en utilisant le système RSA.

1. Création des clés:
    - Calculer votre clé privée.
    - Calculer et transmettre votre clé publique.

```{tip}
Utiliser [WolframAlpha](https://www.wolframalpha.com/) comme aide pour les
calculs.
```

2. Chiffrement du message:
    - Écrire un message (une petite phrase avec majuscule, espaces et
      ponctuations).
    - Transformer le message en nombre en utilisant le code ASCII étendu
      correspondant à chaque caractère. Utiliser le tableau suivant:
      [Code ASCII](images/code-ascii.pdf).
    - Chiffrer le message avec la bonne clé.
    - Transmettre le message chiffré au bon groupe.

3. Déchiffrement d'un autre message:
    - Déchiffrer le message reçu.
