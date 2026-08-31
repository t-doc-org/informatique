% Copyright 2026 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# HTML et CSS - Annexe

```{metadata}
date: 20.06.2026
```

## Fichier index.html

```{code} text
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <title>Collège du Sud</title>
  <link href="......(1)......" rel="stylesheet" type="text/css" />
</head>
......(2)......
  <h1>Le collège du Sud</h1>
  <p id="intro">Cette page Web présente le collège du Sud!</p>
  <h2>Présentation</h2>
  <p class="gras">Le Collège du Sud est un établissement fribourgeois du
  secondaire du 2e degré.</p>
  <p>Il offre actuellement 3 filières d’études: un gymnase, une école de
  commerce et une école de culture générale.</p>
  <p>Source: <a href="https://collegedusud.ch">Site du collège du Sud</a></p>
  <......(3)...... src="images/CSud.jpg" width="300px">
  <h2>Mes cours</h2>
  <ul>
    <li>Français</li>
    <li>Allemand</li>
    <li>Anglais</li>
  </ul>
</body>
......(4)......
```


## Fichier style.css

```{code} text
body {
  font-family: Arial, sans-serif;
  background-color: lightblue;
}
h1, h2 {
  font-family: Georgia, serif;
  color: blueviolet;
}
h1 {
  text-align: center;
}
.gras {
  font-weight: bold;
}
#intro {
  text-align: center;
  font-style: italic;
}
```
