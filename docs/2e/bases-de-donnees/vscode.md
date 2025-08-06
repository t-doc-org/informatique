% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Visual Studio Code

[Installation de Visual Studio Code](/logiciels/vscode.md)

## Installation de l'extension SQLite

Pour l'utilisation de bases de données dans VSCode, il faut installer
une extension.

1. Dans VSCode, sélectionner dans le menu à gauche "Extensions".
2. Rechercher l'extension **SQLite** créée par alexcvzz.
3. Cliquer sur installer.
4. Redémarrer VSCode.
```{figure} images/extension.png
:alt: Installer SQLite
:width: 40%
:align: center
```

(creation)=
## Création d'une base de donnée

1. Créer un nouveau dossier dans votre OneDrive. Par exemple, SQL_stock
2. Depuis VSCode, dans le menu "Fichier", choisir "Ouvrir le dossier..."" et
sélectionner le dossier créé en 1.
```{figure} images/menu-fichier.png
:alt: Menu fichier
:width: 50%
:align: center
```
3. Cliquer sur nouveau fichier. Cela permet de créer une nouvelle base de
données.
```{figure} images/new-bd.png
:alt: Nouvelle base de données
:width: 50%
:align: center
```
4. Nommer-là `stock.sqlite`.
```{figure} images/nommer.png
:alt: Nommer la nouvelle base de données
:width: 50%
:align: center
```
5. Au moyen d'un clic droit sur `stock.sqlite`, sélectionner
"Open Database".
```{figure} images/ouvrir.png
:alt: Ouvrir la base de données
:width: 50%
:align: center
```
6. En bas de la page à gauche est apparu "SQLITE EXPLORER", cliquer sur
"New Query".
```{figure} images/explorer.png
:alt: Nouvelle requête
:width: 40%
:align: center
```
7. Une nouvelle fenêtre est apparue, écrire la requête et sauvegarder.
```{figure} images/requete.png
:alt: Requête
:width: 90%
:align: center
```
8. Exécuter la requête, avec un clic droit et en sélectionnant "Run Query".
```{figure} images/executer.png
:alt: Requête
:width: 90%
:align: center
```
9. Répéter les points 6 à 8 pour chaque nouvelle requête.

(import)=
## Importation d'une base de donnée

1. [Créer une nouvelle base de données](#creation) points 1 à 5.
2. Télécharger et sauvegarder le fichier .sql dans le dossier de la base de
données.
3. Dans VSCode, ouvrir le fichier `.sql` importé et sélectionner "Run Query"
(clic droit).
```{figure} images/import.png
:alt: Lancer la requête d'une base de données importée
:width: 90%
:align: center
```



