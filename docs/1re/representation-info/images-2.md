% Copyright 2026 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
solutions: dynamic
```

# Images version 2

Nous avons vu comment représenter des nombres et des caractères. Maintenant nous
allons nous intéresser aux images.

<style>
.box > * {
  margin: 10px;
}

.box {
  display: flex;
}

.tdoc-code {
  min-width: 200px;
  height: 150px;
}
</style>

<div class="box">
<div>
<textarea class="tdoc-code">
P1
10 10
0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 1 0 0
0 1 1 0 0 0 0 1 1 0
0 1 0 0 0 0 0 0 1 0
0 1 0 0 0 0 0 0 1 0
0 1 0 0 0 0 0 0 1 0
0 1 0 0 0 0 0 0 1 0
0 1 1 0 0 0 0 1 1 0
0 0 1 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 0
</textarea>
</div>

<div><button class="tdoc-btn-convertir">Convertir</button></div>

<div class="image">

</div>
</div>

<div class="box">
<div>
<textarea class="tdoc-code">
P2
8 8
3
3 2 3 3 3 3 2 3
2 2 1 2 2 1 2 2
2 2 2 2 2 2 2 2
1 2 0 2 2 0 2 1
2 2 0 2 2 0 2 2
1 2 2 2 2 2 2 1
3 2 0 1 1 0 2 3
3 3 1 1 1 1 3 3
</textarea>
</div>

<div><button class="tdoc-btn-convertir">Convertir</button></div>

<div class="image">

</div>
</div>



<script>
function afficher(encodage) {
  switch (encodage[0]) {
    case "P1":
      afficherPBM(encodage);
      break;
    case "P2":
      afficherPGM(encodage);
      break;
    case "P3":
      afficherPPM(encodage);
      break;
    default:
      document.querySelector('.image').innerHTML = "Erreur dans le format.";

  }
}

function afficherPBM(encodage) {
  nb_meta = 3;
  const w = largeur * encodage[1], h = largeur * encodage[2];
  let svg;
  if (encodage.length !== encodage[1] * encodage[2] + nb_meta) {
    svg = "Le nombre de données ne correspond pas aux dimensions de l'image annoncée."
  } else {
    svg = `<svg width="${w}" height="${h}" xmlns="http://www.w3.org/2000/svg">`
    for (let j = 0; j < encodage[2]; j++) {
      for (let i = 0; i < encodage[1]; i++) {
        let couleur = encodage[nb_meta + j * encodage[1] + i] === '1' ? '#000000':'#FFFFFF';
        svg += `<rect x = "${i * largeur}" y = "${j * largeur}" width = "${largeur}" height= "${largeur}" fill = "${couleur}"/>`;
      }
    }
    svg += '</svg>';
  }
  document.querySelector('.image').innerHTML = svg;
}

function afficherPGM(encodage) {
  nb_meta = 4;
  const w = largeur * encodage[1], h = largeur * encodage[2];
  let svg;
  if (encodage.length !== encodage[1] * encodage[2] + nb_meta) {
    svg = "Le nombre de données ne correspond pas aux dimensions de l'image annoncée."
  } else {
    svg = `<svg width="${w}" height="${h}" xmlns="http://www.w3.org/2000/svg">`
    for (let j = 0; j < encodage[2]; j++) {
      for (let i = 0; i < encodage[1]; i++) {
        let nuance = Math.round(encodage[nb_meta + j * encodage[1] + i] * 255 / encodage[3]);
        let couleur = `rgb(${nuance} ${nuance} ${nuance})`;
        svg += `<rect x = "${i * largeur}" y = "${j * largeur}" width = "${largeur}" height= "${largeur}" fill = "${couleur}"/>`;
      }
    }
    svg += '</svg>';
  }
  document.querySelector('.image').innerHTML = svg;
}

function afficherPPM(encodage) {
  nb_meta = 4;
  const w = largeur * encodage[1], h = largeur * encodage[2];
  let svg;
  if (encodage.length !== encodage[1] * encodage[2] * 3 + nb_meta) {
    svg = "Le nombre de données ne correspond pas aux dimensions de l'image annoncée."
  } else {
    svg = `<svg width="${w}" height="${h}" xmlns="http://www.w3.org/2000/svg">`
    for (let j = 0; j < encodage[2]; j++) {
      for (let i = 0; i < encodage[1]; i++) {
        let index = nb_meta + j * encodage[1] * 3 + i * 3;
        let couleur = `rgb(${encodage[index] * 255 / encodage[3]} ${encodage[index+1] * 255 / encodage[3]} ${encodage[index+2] * 255 / encodage[3]})`;
        svg += `<rect x = "${i * largeur}" y = "${j * largeur}" width = "${largeur}" height= "${largeur}" fill = "${couleur}"/>`;
      }
    }
    svg += '</svg>';
  }
  document.querySelector('.image').innerHTML = svg;
}

const largeur = 20;
let btn_convertir = document.querySelector('.tdoc-btn-convertir');
btn_convertir.addEventListener('click', function() {
  let text = document.querySelector('.tdoc-code').value;
  const encodage = text.trim().split(/[\n, ]/);
  afficher(encodage);
});

</script>
