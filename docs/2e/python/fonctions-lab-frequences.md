% Copyright 2026 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{defaults} exec
:editor-config: store: 'cloud'
```

# Fonctions Lab - Analyse de fréquences

## Exercice {nump}`exercice`

Nous allons analyser la phrase "C'est une belle phrase à analyser!".

1.  Affichez la phrase.
2.  Calculez et affichez le nombre de caractères de cette phrase.
3.  Calculez et affichez la fréquence de la lettre "e".

```{exec} python
:editor: b33b9a10-d665-48dd-8344-8acb34ea20e3
phrase = "C'est une belle phrase à analyser!"
```

````{solution}
```{exec} python
phrase = "C'est une belle phrase à analyser!"
# 1
print("La phrase est:", phrase)
# 2
total = len(phrase)
print("La longueur de la phrase est:", total, "caractères.")
# 3
n = phrase.count("e")
f = n/total
print("La fréquence de la lettre e est:", f, "soit", f * 100, "%.")
```
````

## Exercice {nump}`exercice`

```{exec} python
:name: texte
:class: hidden
texte = "L'école moderne, c'est l'art d'enseigner le théorème de Pythagore à des ados capables de scroller sur TikTok à la vitesse de la lumière tout en ouvrant discrètement trois onglets de jeux en ligne pendant le cours d'histoire. Aujourd'hui, le stylo plume a pris sa retraite, remplacé par des tablettes où les notes de cours cohabitent joyeusement avec des mèmes et des vidéos en tendance. Les profs ne se battent plus contre les avions en papier, mais contre le correcteur automatique et les copier-coller un peu trop magiques de ChatGPT. Au fond, c'est une génération ultra-connectée et pleine de ressources, capable de faire un montage vidéo digne d'Hollywood en deux minutes sur leur téléphone, mais qui cherche encore la formule magique pour faire ses devoirs sans procrastiner."
```

Un texte, généré par Gemini, a été sauvegardé dans la variable `texte`.

1.  Affichez le texte.
2.  Calculez et affichez le nombre de caractères de ce texte.
3.  Calculez et affichez la fréquence de la lettre "e", de la lettre "a", de la
    lettre "d" et de la lettre "x".<br>
    Les valeurs correspondent-elles à celles attendues
    (voir [](../crypto/frequences.md))? Pourquoi?

```{exec} python
:after: texte
:editor: e43729d7-c4e9-491d-8874-9c7e21038966
```

````{solution}
```{exec} python
:after: texte
# 1
print(texte)
# 2
total = len(texte)
print("La longueur de la phrase est:", total, "caractères.")
# 3
n = texte.count("e")
f = n/total
print("La fréquence de la lettre e est:", f, "soit", f * 100, "%.")
n = texte.count("a")
f = n/total
print("La fréquence de la lettre a est:", f, "soit", f * 100, "%.")
n = texte.count("d")
f = n/total
print("La fréquence de la lettre d est:", f, "soit", f * 100, "%.")
n = texte.count("x")
f = n/total
print("La fréquence de la lettre x est:", f, "soit", f * 100, "%.")
```

Les valeurs pour le "d" et le "x" sont proches, mais pas pour le "e" et le "a".

Les fréquences d'apparition des lettres en français des
[](../crypto/frequences.md) ne tiennent pas compte des différences entre une
lettre majuscule ou minuscule, ni celles des lettres accentuées. De plus, la
ponctuation et les espaces doivent être ignorés. Pour faire une analyse de
fréquences, il faudrait tout d'abord modifier le texte (supprimer les
majuscules, les accents, la ponctuation, ...).
````

## Exercice {nump}`exercice`

Avant de pouvoir faire une analyse de fréquences, il faut "nettoyer" un peu le
texte:

- convertir le texte en minuscule,
- supprimer les espaces,
- convertir toutes les lettres accentuées en caractères sans accents,
- supprimer la ponctuation.


1.  Affichez le texte original.
2.  Convertissez et affichez le texte en minuscule.
3.  Supprimez les espaces et affichez le texte modifié.
4.  Définissez une fonction qui convertit toutes les lettres accentuées en
    caractères sans accents et affichez le texte modifié.
5.  Supprimez toutes les ponctuations et affichez le texte modifié.
6.  Refaites l'analyse de fréquences de l'exercice précédent en définissant une
    fonction `analyse` qui prend en paramètre le texte et la lettre à analyser.<br>
    La fonction doit afficher l'analyse de fréquences en pourcents comme
    ci-dessous.
    ```{code-block} text
    La fréquence de la lettre e est de 18.39622641509434 %.
    ```

```{exec} python
:after: texte
:editor: 90a2b2e7-8f40-40b3-b0b8-5cb28b866dd7

```

````{solution}
```{exec} python
:after: texte
def suppression_accents(texte):
  texte = texte.replace("é", "e")
  texte = texte.replace("è", "e")
  texte = texte.replace("ê", "e")
  texte = texte.replace("ë", "e")
  texte = texte.replace("à", "a")
  texte = texte.replace("à", "a")
  texte = texte.replace("î", "i")
  texte = texte.replace("ï", "i")
  texte = texte.replace("ô", "o")
  texte = texte.replace("ù", "u")
  texte = texte.replace("û", "u")
  texte = texte.replace("ü", "u")
  texte = texte.replace("ç", "c")
  return texte

def suppression_pontuation(texte):
  texte = texte.replace("'", "")
  texte = texte.replace(",", "")
  texte = texte.replace(".", "")
  texte = texte.replace(":", "")
  texte = texte.replace(";", "")
  texte = texte.replace("!", "")
  texte = texte.replace("?", "")
  texte = texte.replace('"', "")
  return texte

def analyse(texte, lettre):
  total = len(texte)
  n = texte.count(lettre)
  f = n/total
  print("La fréquence de la lettre", lettre, "est de", f * 100, "%.")


# 1
print(texte)
# 2
txt = texte.lower()
print(txt)
# 3
txt = txt.replace(" ", "")
print(txt)
# 4
txt = suppression_accents(txt)
print(txt)
# 5
txt = suppression_pontuation(txt)
print(txt)
# 6
analyse(txt, "e")
analyse(txt, "a")
analyse(txt, "d")
analyse(txt, "x")
```

````
