% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Cryptographie Lab

```{important}
Par convention, nous écrivons le texte en minuscules pour le message clair et en
majuscules pour le cryptogramme (texte chiffré).
```

## Cryptographie moderne:

La cryptographie moderne utilise
- la cryptographie asymétrique (par exemple RSA) pour l'échange de la clé
    symétrique,
- la cryptographe symétrique pour l'envoi de tous les autres messages.

Pendant ce laboratoire, vous allez faire le processus complet utilisé en
cryptographie moderne:


### Exercice {nump}`exercice`: Envoi de la clé symétrique avec RSA

{.lower-alpha-paren}
1.  Créez les clés publique et privée avec les valeurs $p$ et $q$ transmises
    par l'enseignant.e (cf. [](#creation-cles)):
    - Calculez votre clé privée.
    - Calculez votre clé publique et "publiez-la" au tableau noir.

    ```{tip}
    Utilisez [WolframAlpha](https://www.wolframalpha.com/) comme aide pour les
    calculs.
    ```
2.  Choisissez une **clé de chiffrement symétrique** que vous utiliserez
    pour chiffrer tous les autres messages avec le chiffre de Vigenère (un
    mot entre 4 et 8 lettres).

3.  Chiffrez votre clé symétrique:
    - Transformez la clé symétrique en nombre en utilisant le code ASCII
        étendu correspondant à chaque caractère. Utilisez le tableau
        suivant: [Code ASCII](images/code-ascii.pdf).
    - Chiffrez la clé symétrique avec la bonne clé. (cf. [](#chiffrement))
4.  Transmettez la clé symétrique chiffrée au bon groupe.

```{solution}
Génération de quelques clés:

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

**Chiffrement de "Hello":**

Code ASCII: 072 101 108 108 111 033

Chiffrement avec la clé publique (15229, 5):

$072^5 \textrm{ mod } 15229 = 12266$\
$101^5 \textrm{ mod } 15229 = 4128$\
$108^5 \textrm{ mod } 15229 = 6530$\
$108^5 \textrm{ mod } 15229 = 6530$\
$111^5 \textrm{ mod } 15229 = 12860$

Les caractères seront envoyés les uns après les autres, il y aura donc 5
messages envoyés:\
12266 4128 6530 6530 12860

```


### Exercice {nump}`exercice`: Réception et déchiffrement d'un message avec RSA

Déchiffrez la clé symétrique reçue en utilisant la bonne clé. Cette
clé vous permettra ensuite de chiffrer et envoyer des messages au groupe
correspondant. (cf. [](#dechiffrement))

```{solution}
Déchiffrement de 12266 4128 6530 6530 12860 12092 avec la clé privé
(97, 157, 11981):

$12266^11981 \textrm{ mod } (97 \cdot 157) = 72$ -> h\
$4128^11981 \textrm{ mod } (97 \cdot 157) = 101$ -> e\
$6530^11981 \textrm{ mod } (97 \cdot 157) = 108$ -> l\
$6530^11981 \textrm{ mod } (97 \cdot 157) = 108$ -> l\
$12860^11981 \textrm{ mod } (97 \cdot 157) = 111$ -> o

La clé de chiffrement pour Vigenère est donc **hello**.
```

### Exercice {nump}`exercice`: Envoi d'un message avec Vigenère

Écrivez un message (une phrase) au groupe qui vous a transmis la clé
symétrique. (cf. [](#vigenere))

````{solution}
Clé de chiffrement: hello

Message: Le chiffre de Vigenère a été utilisé.

```{list-table}
:class: text-center
:stub-columns: 1
:align: center
:widths: 10 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
* - Texte clair
  - l
  - e
  - c
  - h
  - i
  - f
  - f
  - r
  - e
  - d
  - e
  - v
  - i
  - g
  - e
  - n
  - e
  - r
  - e
  - a
  - e
  - t
  - e
  - u
  - t
  - i
  - l
  - i
  - s
  - e
* - Clé
  - h
  - e
  - l
  - l
  - o
  - h
  - e
  - l
  - l
  - o
  - h
  - e
  - l
  - l
  - o
  - h
  - e
  - l
  - l
  - o
  - h
  - e
  - l
  - l
  - o
  - h
  - e
  - l
  - l
  - o
* - Décalage
  - 7
  - 4
  - 11
  - 11
  - 14
  - 7
  - 4
  - 11
  - 11
  - 14
  - 7
  - 4
  - 11
  - 11
  - 14
  - 7
  - 4
  - 11
  - 11
  - 14
  - 7
  - 4
  - 11
  - 11
  - 14
  - 7
  - 4
  - 11
  - 11
  - 14
* - Code
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
```

Code: SINSW MJCPR LZTRS UICPO LXPFH PPTDS
````

### Exercice {nump}`exercice`: Réception et déchiffrement d'un message avec Vigenère

Déchiffrez le message reçu.

````{solution}
Code: SINSW MJCPR LZTRS UICPO LXPFH PPTDS

Clé de chiffrement: hello

```{list-table}
:class: text-center
:stub-columns: 1
:align: center
:widths: 10 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
* - Texte clair
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
* - Clé
  - h
  - e
  - l
  - l
  - o
  - h
  - e
  - l
  - l
  - o
  - h
  - e
  - l
  - l
  - o
  - h
  - e
  - l
  - l
  - o
  - h
  - e
  - l
  - l
  - o
  - h
  - e
  - l
  - l
  - o
* - Décalage
  - 7
  - 4
  - 11
  - 11
  - 14
  - 7
  - 4
  - 11
  - 11
  - 14
  - 7
  - 4
  - 11
  - 11
  - 14
  - 7
  - 4
  - 11
  - 11
  - 14
  - 7
  - 4
  - 11
  - 11
  - 14
  - 7
  - 4
  - 11
  - 11
  - 14
* - Code
  - S
  - I
  - N
  - S
  - W
  - M
  - J
  - C
  - P
  - R
  - L
  - Z
  - T
  - R
  - S
  - U
  - I
  - C
  - P
  - O
  - L
  - X
  - P
  - F
  - H
  - P
  - P
  - T
  - D
  - S
```
Message: Le chiffre de Vigenère a été utilisé.
````


## Décryptage de messages

### Exercice {nump}`exercice`: Décryptage d'un chiffre de César

Vous avez intercepté, sur le réseau public, un des messages suivants chiffré au
moyen du Chiffre de César (décalage de l'alphabet, mais pas forcément de 3
positions). (cf. [](#cesar))

1. Faites une analyse de fréquences. Vous pouvez utiliser le site suivant pour
   l'[analyse de fréquences](https://www.dcode.fr/analyse-frequences).
2. Déterminez la clé de chiffrement (le décalage utilisé).
3. Après avoir déterminé le décalage, déchiffrez le message.

**Groupe 1:**\
GOQVS NEISJ CHFSQ VWSBO RSDCG SEISZ EISGD SHWHS GPCAP SGDOF HCIHR OBGAC BXOFR
WBSHE ISQOA SQCBH FOFWS

**Groupe 2:**\
JMICK WCXLM KPWAM AMFQA BIQMV BRILQ AUIQA ICKCV LMKMC FYCQD QDMVB
ICRWC ZLPCQ VMAMV AWCDQ MVVMV B

**Groupe 3:**\
WYMNN LIJWU FGYDU CGYJU MNLIJ VYUOW IOJWU DJLYZ YLYKO UHXWY MNOHJ
YONLI JJFOM GICHM WUFGY

**Groupe 4:**\
ZCWRL KULTF LIRXV GFLIR WWIFE KVIJV JVEEV DZJDR ZJZCV EWRLK VETFI
VGCLJ GFLIR WWIFE KVIJV JRDZJ

**Groupe 5:**\
XSXKQ GBJBA FPXFP NRBJX SFBBQ XFQRK BQOXD BAFBG BJBOB KAPZL JMQBN
RBZBP QRKBZ LJBAF B

**Groupe 6:**\
QFANJ HJXYH TRRJZ SJGTN YJIJH MTHTQ FYXTS SJXFN YOFRF NXXZW VZTNT
SAFYT RGJW

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


### Exercice {nump}`exercice`: Décryptage d'une substitution monoalphabétique

Décryptez à l'aide de l'analyse de fréquences, le cryptogramme suivant,
chiffré par une substitution monoalphabétique (cas général, c'est-à-dire que
chaque lettre a été remplacée par une autre lettre) (cf. [](#cas-general)):

ZRJ VDAARJ CLWJJRCK RK ERARMHRCK ZWIHRJ RK RULMP RC EHDWKJ. ZRJ EWJKWCBKWDCJ
JDBWLZRJ CR FRMNRCK RKHR TDCERRJ GMR JMH Z'MKWZWKR BDAAMCR.

Les espaces et la ponctuation ont été laissés pour faciliter l'exercice.

1. Faites une [analyse de fréquences](https://www.dcode.fr/analyse-frequences)
   des lettres, des digrammes et des caractères répétés et utiliser les
   [tables de fréquences](frequences.md).
2. Essayez de décrypter le message en vous aidant de l'analyse de fréquences.

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

## Cryptographie symétrique

### Exercice {nump}`exercice`: Déchiffrage d'un chiffre de Rail Fence

Vous avez reçu ce message qui a été chiffré avec le chiffre de Rail Fence à 3
niveaux. (cf. [](#railfence))

Clé de chiffrement: 3 niveaux

Message codé:

NASLU IEAEA IVXRI ETOSV NUIIE NHFRD RIFNE TOSIE UPUER RCTXE UOTSC FELCR NAOCE E


