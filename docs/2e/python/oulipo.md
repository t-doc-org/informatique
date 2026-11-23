% Copyright 2026 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{defaults} exec
:editor-config: store: 'cloud'
```

# Oulipo - Outil d'analyse de texte

```{exec} python
:include: textes.py
:name: textes
:class: hidden
```


```{exec} python
:after: textes
:editor: 20ef7108-e211-41ba-961a-e88a9bf4b92c
def suppression_accents(texte):
  texte = texte.replace("é", "e")
  texte = texte.replace("è", "e")
  texte = texte.replace("ê", "e")
  texte = texte.replace("ë", "e")
  texte = texte.replace("à", "a")
  texte = texte.replace("â", "a")
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
  texte = texte.replace("«", "")
  texte = texte.replace("»", "")
  texte = texte.replace("“", "")
  texte = texte.replace("”", "")
  texte = texte.replace("-", "")
  texte = texte.replace("…", "")
  return texte

def suppression_caracteres_speciaux(texte):
  texte = texte.replace("_", "")
  texte = texte.replace("\n", "")
  texte = texte.replace("(", "")
  texte = texte.replace(")", "")
  texte = texte.replace("[", "")
  texte = texte.replace("]", "")
  return texte

def suppression_chiffres(texte):
  texte = texte.replace("0", "")
  texte = texte.replace("1", "")
  texte = texte.replace("2", "")
  texte = texte.replace("3", "")
  texte = texte.replace("4", "")
  texte = texte.replace("5", "")
  texte = texte.replace("6", "")
  texte = texte.replace("7", "")
  texte = texte.replace("8", "")
  texte = texte.replace("9", "")
  return texte

def analyse(texte, lettre):
  total = len(texte)
  n = texte.count(lettre)
  f = n/total
  return round(f * 100, 2)

```

<!-- lettres = ["e", "a", "s", "i", "t", "n", "r", "u", "l", "o", "d", "m", "c", "p", "v", "q", "f", "g", "h", "b", "j", "x", "y", "z", "k", "w"]
textes = [texte0, texte1, texte2, texte3, texte4, texte5, texte6, texte7, texte8]

for texte in textes:
  txt = texte.lower()
  txt = txt.replace(" ", "")
  txt = suppression_accents(txt)
  txt = suppression_pontuation(txt)
  txt = suppression_caracteres_speciaux(txt)
  txt = suppression_chiffres(txt)
  resultat = ""
  for l in lettres:
    resultat += l + ": " + str(analyse(txt, l)) + " "
  print(resultat) -->




