// Copyright 2026 Caroline Blank <caro@c-space.org>
// SPDX-License-Identifier: CC-BY-NC-SA-4.0

import {Runner, UserError} from './exec.js';

const largeur = 20;

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
        const text = blocks.join('');
        const encodage = text.trim().split(/[\n, ]/);
        console.log(encodage);
        const svg = this.generer(encodage);
        this.output.render('001', svg);
    }

    generer(encodage) {
        switch (encodage[0]) {
        case "P1": return this.genererPBM(encodage);
        case "P2": return this.genererPGM(encodage);
        case "P3": return this.genererPPM(encodage);
        default: throw new UserError("Erreur dans le format.");
        }
    }

    genererPBM(encodage) {
        const nb_meta = 3;
        const w = largeur * encodage[1], h = largeur * encodage[2];
        if (encodage.length !== encodage[1] * encodage[2] + nb_meta) {
            throw new UserError(`\
Le nombre de données ne correspond pas aux dimensions de l'image annoncée.`);
        }
        let svg = `\
<svg class="pnm" width="${w}" height="${h}"\
 xmlns="http://www.w3.org/2000/svg">`;
        for (let j = 0; j < encodage[2]; j++) {
            for (let i = 0; i < encodage[1]; i++) {
                let couleur = encodage[nb_meta + j * encodage[1] + i] === '1' ?
                              '#000000':'#ffffff';
                svg += `\
<rect x="${i * largeur}" y="${j * largeur}" width="${largeur}"\
 height="${largeur}" fill="${couleur}"/>`;
            }
        }
        svg += '</svg>';
        return svg;
    }

    genererPGM(encodage) {
        const nb_meta = 4;
        const w = largeur * encodage[1], h = largeur * encodage[2];
        if (encodage.length !== encodage[1] * encodage[2] + nb_meta) {
            throw new UserError(`\
Le nombre de données ne correspond pas aux dimensions de l'image annoncée.`);
        }
        let svg = `\
<svg class="pnm" width="${w}" height="${h}"\
 xmlns="http://www.w3.org/2000/svg">`;
        for (let j = 0; j < encodage[2]; j++) {
            for (let i = 0; i < encodage[1]; i++) {
                let nuance = Math.round(encodage[nb_meta + j * encodage[1] + i]
                                        * 255 / encodage[3]);
                let couleur = `rgb(${nuance} ${nuance} ${nuance})`;
                svg += `\
<rect x="${i * largeur}" y="${j * largeur}" width="${largeur}"\
 height="${largeur}" fill="${couleur}"/>`;
            }
        }
        svg += '</svg>';
        return svg;
    }

    genererPPM(encodage) {
        const nb_meta = 4;
        const w = largeur * encodage[1], h = largeur * encodage[2];
        if (encodage.length !== encodage[1] * encodage[2] * 3 + nb_meta) {
            throw new UserError(`\
Le nombre de données ne correspond pas aux dimensions de l'image annoncée.`);
        }
        let svg = `\
<svg class="pnm" width="${w}" height="${h}"\
 xmlns="http://www.w3.org/2000/svg">`;
        for (let j = 0; j < encodage[2]; j++) {
            for (let i = 0; i < encodage[1]; i++) {
                let index = nb_meta + j * encodage[1] * 3 + i * 3;
                let couleur = `\
rgb(${encodage[index] * 255 / encodage[3]}\
 ${encodage[index + 1] * 255 / encodage[3]}\
 ${encodage[index + 2] * 255 / encodage[3]})`;
                svg += `\
<rect x="${i * largeur}" y="${j * largeur}" width="${largeur}"\
 height="${largeur}" fill="${couleur}"/>`;
            }
        }
        svg += '</svg>';
        return svg;
    }
}

Runner.apply(PnmRunner);  // Background
