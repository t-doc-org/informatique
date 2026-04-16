/* Copyright 2026 Caroline Blank <caro@c-space.org> */
/* SPDX-License-Identifier: CC-BY-NC-SA-4.0 */

export const [{
    gcd, initBoard, JXG, merge, nonInteractive, template, withAxesLabels,
}] = await tdoc.imports('tdoc/jsxgraph.js');

// Defaults for use on screen media.
export const screen = [{
    axis: true, grid: true,
    defaultAxes: {
        x: {ticks: {minorTicks: 1}},
        y: {ticks: {minorTicks: 1}},
    },
    defaults: {
        arrow: {
            strokeWidth: 2, strokeColor: JXG.palette.black,
        },
        circle: {
            strokeWidth: 2, strokeColor: JXG.palette.blue,
            label: {strokeColor: JXG.palette.blue},
        },
        curve: {
            strokeWidth: 2, strokeColor: JXG.palette.blue,
            label: {strokeColor: JXG.palette.blue},
        },
        functiongraph: {
            label: {strokeColor: JXG.palette.blue},
        },
        line: {
            strokeWidth: 1, strokeColor: JXG.palette.black,
        },
        point: {
            size: 1.5,
            strokeWidth: 1, strokeColor: JXG.palette.black,
            fillColor: JXG.palette.black,
        },
    },
}];

// Defaults for use on print media.
export const print = [nonInteractive, {
    axis: true, grid: true,
    defaultAxes: {
        x: {ticks: {insertTicks: false, ticksDistance: 1, minorTicks: 0}},
        y: {ticks: {insertTicks: false, ticksDistance: 1, minorTicks: 0}},
    },
    defaults: {
        curve: {strokeColor: JXG.palette.black, strokeWidth: 2},
        point: {
            name: '', size: 2,
            strokeWidth: 1, strokeColor: JXG.palette.black,
            fillColor: JXG.palette.black,
        },
    },
}];
