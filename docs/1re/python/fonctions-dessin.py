# Copyright 2026 Caroline Blank <caro@c-space.org>
# SPDX-License-Identifier: CC-BY-NC-SA-4.0

from tdoc import svg

def creation_image(largeur, hauteur, couleur):
    global img
    img = svg.Image(largeur, hauteur, stroke='black',
                    style='width: 100%; height: 100%;')
    rectangle(0, 0, largeur, hauteur, couleur)

def rectangle(x, y, largeur, hauteur, remplissage, bord="transparent"):
    img.rect(x, y, largeur, hauteur, stroke=bord, fill=remplissage)

def triangle(point_1, point_2, point_3, remplissage, bord="transparent"):
    img.polygon(point_1, point_2, point_3, stroke=bord, fill=remplissage)

def cercle(centre_x, centre_y, rayon, remplissage, bord="transparent"):
    img.circle(centre_x, centre_y, rayon, stroke=bord, fill=remplissage)

def ellipse(centre_x, centre_y, rayon_x, rayon_y, remplissage,
            bord="transparent"):
    img.ellipse(centre_x, centre_y, rayon_x, rayon_y, stroke=bord,
                fill=remplissage)

def ligne(x1, y1, x2, y2, couleur, epaisseur):
    img.line(x1, y1, x2, y2, stroke=svg.Stroke(couleur, width=epaisseur))

def texte(x, y, texte, couleur, taille):
    font = f"font: bold italic {taille}px serif"
    img.text(x, y, texte, stroke='transparent', fill=couleur, style=font)
