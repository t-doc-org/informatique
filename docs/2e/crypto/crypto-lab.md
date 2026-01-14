% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
solutions: dynamic
```

# Cryptographie Lab

Dans le cours, nous avons vu plusieurs exemples de cryptographie symétrique et
asymétrique. Nous allons tester ces différents systèmes.

```{important}
Par convention, nous écrivons le texte en minuscules pour le message clair et en
majuscules pour le cryptogramme (texte chiffré).
```

## Exercice {nump}`exercice`

**But:** Utilisation du chiffre de Rail Frence pour chiffrer et déchiffrer un
message.

Écrivez un message pour un camarade de classe avec une clé de chiffrement de 3:

1. Chacun écrit un message qu'il chiffre et transmet à un autre élève.
2. Déchiffrez le message d'un autre élève.

## Exercice {nump}`exercice`

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

1. Faites une analyse de fréquences. Vous pouvez utiliser le site suivant pour
   l'[analyse de fréquences](https://www.dcode.fr/analyse-frequences).
2. Déterminez la clé de chiffrement.
3. Déchiffrez le message.

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

6. QFANJ HJXYH TRRJZ SJGTN YJIJH MTHTQ FYXTS SJXFN YOFRF NXXZW VZTNT SAFYT RGJW\
**Clé:** décalage de 5\
**Texte clair:** la vie c est comme une boite de chocolats on ne sait jamais sur
quoi on va tomber (Forrest Gump)
```

## Exercice {nump}`exercice`

**But:** Décrypter un message utilisant la substitution monoalphabétique en
faisant une analyse de fréquences.

Décryptez à l'aide de l'analyse de fréquences, le cryptogramme suivant,
chiffré par une substitution monoalphabétique (cas général):

ZRJ VDAARJ CLWJJRCK RK ERARMHRCK ZWIHRJ RK RULMP RC EHDWKJ. ZRJ EWJKWCBKWDCJ
JDBWLZRJ CR FRMNRCK RKHR TDCERRJ GMR JMH Z'MKWZWKR BDAAMCR.

Les espaces et la ponctuation ont été laissés pour faciliter l'exercice.

1. Faire une [analyse de fréquences](https://www.dcode.fr/analyse-frequences)
   des lettres, des digrammes et des caractères répétés et utiliser les
   [tables de fréquences](frequences.md).
2. Décrypter le message.

````{tip}
Écrivez un programme python qui permet de remplacer les lettres les unes après
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

Article 1 de la Déclaration des Droits de l'homme et du Citoyen de 1789.
```

## Exercice {nump}`exercice`

**But:** Échanger un message en utilisant le système RSA.

1. Création des clés:
    - Calculez votre clé privée.
    - Calculez et transmettez votre clé publique.

```{tip}
Utilisez [WolframAlpha](https://www.wolframalpha.com/) comme aide pour les
calculs.
```

2. Chiffrement du message:
    - Écrivez un message (une petite phrase avec majuscule, espaces et
      ponctuations entre 6 et 15 caractères).
    - Transformez le message en nombre en utilisant le code ASCII étendu
      correspondant à chaque caractère. Utiliser le tableau suivant:
      [Code ASCII](images/code-ascii.pdf).
    - Chiffrez le message avec la bonne clé.
    - Transmettez le message chiffré au bon groupe.

3. Déchiffrement d'un autre message:
    - Déchiffrez le message reçu.

```{solution}
Quelques calculs de clés:

1.  $p=101$ et q=$151$<br>
    $n = 101 \cdot 151 = 15251$<br>
    $\phi = 100 \cdot 150 = 15000$<br>
    $15000 \textrm{ mod } e \neq 0$ La valeur la plus petite possible est $e=7$<br>
    $7 \cdot 15000  \textrm{ mod } d = 1 $ La valeur la plus petite possible est $d=2143$<br>
    La clé privée est (101, 151, 2143) et la clé publique est (15251, 7).
2.  $p=89$ et q=$167$<br>
    $n = 89 \cdot 167 = 14863$<br>
    $\phi = 88 \cdot 166 = 14608$<br>
    $14608 \textrm{ mod } e \neq 0$ La valeur la plus petite possible est $e=3$<br>
    $3 \cdot 14608  \textrm{ mod } d = 1 $ La valeur la plus petite possible est $d=9739$<br>
    La clé privée est (89, 167, 9739) et la clé publique est (14863, 3).
3.  $p=79$ et q=$191$<br>
    $n = 79 \cdot 191 = 15089$<br>
    $\phi = 78 \cdot 190 = 14820$<br>
    $14820 \textrm{ mod } e \neq 0$ La valeur la plus petite possible est $e=7$<br>
    $7 \cdot 14820  \textrm{ mod } d = 1 $ La valeur la plus petite possible est $d=12703$<br>
    La clé privée est (79, 191, 12703) et la clé publique est (15089, 7).
4.  $p=83$ et q=$179$<br>
    $n = 83 \cdot 179 = 14857$<br>
    $\phi = 82 \cdot 178 = 14596$<br>
    $14596 \textrm{ mod } e \neq 0$ La valeur la plus petite possible est $e=3$<br>
    $3 \cdot 14596  \textrm{ mod } d = 1 $ La valeur la plus petite possible est $d=9731$<br>
    La clé privée est (83, 179, 9731) et la clé publique est (14857, 3).
5.  $p=103$ et q=$149$<br>
    $n = 103 \cdot 149 = 15347$<br>
    $\phi = 102 \cdot 148 = 15096$<br>
    $15096 \textrm{ mod } e \neq 0$ La valeur la plus petite possible est $e=5$<br>
    $5 \cdot 15096  \textrm{ mod } d = 1 $ La valeur la plus petite possible est $d=12077$<br>
    La clé privée est (103, 149, 12077) et la clé publique est (15347, 5).
6.  $p=97$ et q=$157$<br>
    $n = 97 \cdot 157 = 15229$<br>
    $\phi = 96 \cdot 156 = 14976$<br>
    $14976 \textrm{ mod } e \neq 0$ La valeur la plus petite possible est $e=5$<br>
    $5 \cdot 14976  \textrm{ mod } d = 1 $ La valeur la plus petite possible est $d=11981$<br>
    La clé privée est (97, 157, 11981) et la clé publique est (15229, 5).

**Chiffrement de "Hello!":**

Code ASCII: 072 101 108 108 111 033

Chiffrement avec la clé privée (97, 157, 11981) et la clé publique (15229, 5):

$072^5 \textrm{ mod } 15229 = 12266$\
$101^5 \textrm{ mod } 15229 = 4128$\
$108^5 \textrm{ mod } 15229 = 6530$\
$108^5 \textrm{ mod } 15229 = 6530$\
$111^5 \textrm{ mod } 15229 = 12860$\
$33^5 \textrm{ mod } 15229 = 12092$

Les caractères seront envoyés les uns après les autres, il y aura donc 6
messages envoyés:\
12266 4128 6530 6530 12860 12092

```
