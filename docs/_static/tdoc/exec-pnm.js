// Copyright 2026 Caroline Blank <caro@c-space.org>
// SPDX-License-Identifier: CC-BY-NC-SA-4.0

import {Runner, UserError} from './exec.js';

const largeur = 20;

const formats = {
    'P1': {
        nb_meta: 3,
        vpp: 1,
        couleur: (encodage, index) => {
            return encodage[index] === '1' ? '#000000':'#ffffff';
        },
    },
     'P2': {
        nb_meta: 4,
        vpp: 1,
        couleur: (encodage, index) => {
            const n = nuance(encodage[index], encodage[3]);
            return `#${n}${n}${n}`;
        },
     },
     'P3': {
        nb_meta: 4,
        vpp: 3,
        couleur: (encodage, index) => {
                return `\
#${nuance(encodage[index], encodage[3])}\
${nuance(encodage[index + 1], encodage[3])}\
${nuance(encodage[index + 2], encodage[3])}`;
        },
     },
};

function nuance(v, max) {
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
        const w = largeur * encodage[1], h = largeur * encodage[2];
        if (encodage.length !== encodage[1] * encodage[2] * vpp + nb_meta) {
            throw new UserError(`\
Le nombre de données ne correspond pas aux dimensions de l'image annoncée.`);
        }
        let svg = `\
<svg class="pnm" width="${w}" height="${h}"\
 xmlns="http://www.w3.org/2000/svg">`;
        for (let j = 0; j < encodage[2]; j++) {
            for (let i = 0; i < encodage[1]; i++) {
                const index = nb_meta + vpp * (j * encodage[1] + i);
                svg += `\
<rect x="${i * largeur}" y="${j * largeur}" width="${largeur}"\
 height="${largeur}" fill="${couleur(encodage, index)}"/>`;
            }
        }
        svg += '</svg>';
        return svg;
    }
}

Runner.apply(PnmRunner);  // Background
