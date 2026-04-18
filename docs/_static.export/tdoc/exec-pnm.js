// Copyright 2026 Caroline Blank <caro@c-space.org>
// SPDX-License-Identifier: CC-BY-NC-SA-4.0

import {strToInt} from './core.js';
import {Runner, UserError} from './exec.js';

const largeur = 20;

const formats = {
    'P1': {
        nb_meta: 3,
        vpp: 1,
        couleur: (encodage, index, max) => {
            const v = strToInt(encodage[index]);
            if (v === undefined || (v !== 0 && v !== 1)) {
                throw new UserError("Valeur de pixel non valide.");
            }
            return v === 1 ? '#000000':'#ffffff';
        },
    },
     'P2': {
        nb_meta: 4,
        vpp: 1,
        couleur: (encodage, index, max) => {
            const n = nuance(encodage[index], max);
            return `#${n}${n}${n}`;
        },
     },
     'P3': {
        nb_meta: 4,
        vpp: 3,
        couleur: (encodage, index, max) => {
                return `\
#${nuance(encodage[index], max)}\
${nuance(encodage[index + 1], max)}\
${nuance(encodage[index + 2], max)}`;
        },
     },
};

function nuance(v, max) {
    v = strToInt(v);
    if (v === undefined || v < 0 || v > max) {
        throw new UserError("Valeur de pixel non valide.");
    }
    return Math.round(v * 255 / max).toString(16).padStart(2, '0');
}

class PnmRunner extends Runner {
    static name = 'pnm';

    constructor(node) {
        super(node);
        this.output = this.sectionedOutput();
    }

    addControls(controls) {
        if (this.when === 'click' || (this.editable && this.when !== 'never')) {
            this.runCtrl = controls.appendChild(this.runControl());
        }
        super.addControls(controls);
    }

    async run(run_id) {
        this.replaceOutputs();
        const blocks = [];
        for (const {code} of this.codeBlocks()) blocks.push(code);
        this.output.render('001', this.generer(blocks.join('')));
    }

    generer(text) {
        const encodage = text.trim().split(/[\n ]+/);
        const {nb_meta, vpp, couleur} = formats[encodage[0]] ?? {};
        if (!nb_meta) throw new UserError("Erreur dans le format.");
        const w = strToInt(encodage[1]);
        if (w === undefined || w <= 0) {
            throw new UserError("Largeur non valide.");
        }
        const h = strToInt(encodage[2]);
        if (h === undefined || h <= 0) {
            throw new UserError("Hauteur non valide.");
        }
        let max;
        if (nb_meta > 3) {
            max = strToInt(encodage[3]);
            if (max === undefined || max <= 0) {
                throw new UserError("Valeur maximale non valide.");
            }
        }
        if (encodage.length !== w * h * vpp + nb_meta) {
            throw new UserError(`\
Le nombre de données ne correspond pas aux dimensions de l'image annoncée.`);
        }
        const svg = [`\
<svg class="pnm" width="${w * largeur}" height="${h * largeur}"\
 xmlns="http://www.w3.org/2000/svg">`];
        for (let j = 0; j < h; j++) {
            for (let i = 0; i < w; i++) {
                const index = nb_meta + vpp * (j * w + i);
                svg.push(`\
<rect x="${i * largeur}" y="${j * largeur}" width="${largeur}"\
 height="${largeur}" fill="${couleur(encodage, index, max)}"/>`);
            }
        }
        svg.push('</svg>');
        return svg.join('');
    }
}

Runner.apply(PnmRunner);  // Background
