// Copyright 2026 Caroline Blank <caro@c-space.org>
// SPDX-License-Identifier: CC-BY-NC-SA-4.0

export const {
    attrs, clip, gcd, initBoard, JXG, merge, render, withAxesLabels,
} = await tdoc.import('tdoc/jsxgraph.js');

// Defaults for use on screen media.
attrs.screen = [{
  axis: true, grid: true,
  defaultAxes: {
    x: {ticks: {minorTicks: 1}},
    y: {ticks: {minorTicks: 1}},
  },
  defaults: {
    arrow: {
      withlabel: true,
      fixed: true, highlight: false, showInfobox: false,
      strokeWidth: 2, strokeColor: JXG.palette.black,
      label: {anchorX: 'middle', anchorY: 'middle', position: '0.4fr left'},
    },
    circle: {
      fixed: true, highlight: false, showInfobox: false,
      strokeWidth: 2, strokeColor: JXG.palette.blue,
      label: {strokeColor: JXG.palette.blue},
    },
    curve: {
      fixed: true, highlight: false, showInfobox: false,
      strokeWidth: 2, strokeColor: JXG.palette.blue,
      label: {strokeColor: JXG.palette.blue},
    },
    functiongraph: {
      withLabel: true,
      fixed: true, highlight: false, showInfobox: false,
      label: {strokeColor: JXG.palette.blue},
    },
    line: {
      fixed: true, highlight: false, showInfobox: false,
      strokeWidth: 1, strokeColor: JXG.palette.black,
    },
    segment: {
      fixed: true, highlight: false, showInfobox: false,
      strokeWidth: 2, strokeColor: JXG.palette.black,
    },
    angle: {
      strokeWidth: 1, strokeColor: JXG.palette.black,
      fillColor: JXG.palette.black, fillOpacity: 0.2,
      label: {strokeColor: JXG.palette.black,
      anchorX: 'middle', anchorY: 'middle'},
    },
    point: {
      withLabel: false, size: 0, fixed: true,
      highlight: false, showInfobox: false,
      strokeWidth: 1, strokeColor: JXG.palette.black,
      fillColor: JXG.palette.black,
    },
    glider: {
      fixed: false, showInfobox: false, highlight: true,
      size: 2, strokewidth: 1,
      highlightStrokeWidth: 14, highlightStrokeOpacity: 0.2,
      highlightStrokeColor: JXG.palette.blue, highlightFillColor: JXG.palette.blue
    },
    orthogonalprojection: {
      withLabel: true, highlight: false, showInfobox: false,
      strokeColor: JXG.palette.black,
    },
    text: {
      fixed: true,
    },
  },
}];

// Defaults for use on print media.
attrs.print = [attrs.nonInteractive, {
  axis: true, grid: true,
  defaultAxes: {
    x: {ticks: {insertTicks: false, ticksDistance: 1, minorTicks: 0}},
    y: {ticks: {insertTicks: false, ticksDistance: 1, minorTicks: 0}},
  },
  defaults: {
    curve: {
      fixed: true, highlight: false, showInfobox: false,
      strokeWidth: 2, strokeColor: JXG.palette.black
    },
    arrow: {
      withLabel: true,
      fixed: true, highlight: false, showInfobox: false,
      strokeWidth: 2, strokeColor: JXG.palette.black,
      label: {anchorX: 'middle', anchorY: 'middle', position: '0.4fr left'},
    },
    circle: {
      fixed: true, highlight: false, showInfobox: false,
      strokeWidth: 2, strokeColor: JXG.palette.black,
      label: {strokeColor: JXG.palette.black},
    },
    curve: {
      fixed: true, highlight: false, showInfobox: false,
      strokeWidth: 2, strokeColor: JXG.palette.black,
      label: {strokeColor: JXG.palette.black},
    },
    functiongraph: {
      withLabel: true,
      fixed: true, highlight: false, showInfobox: false,
      label: {strokeColor: JXG.palette.black},
    },
    line: {
      fixed: true, highlight: false, showInfobox: false,
      strokeWidth: 1, strokeColor: JXG.palette.black,
    },
    segment: {
      fixed: true, highlight: false, showInfobox: false,
      strokeWidth: 2, strokeColor: JXG.palette.black,
    },
    orthogonalprojection: {
      withLabel: true, highlight: false, showInfobox: false,
      strokeColor: JXG.palette.black,
    },
    angle: {
      strokeWidth: 1, strokeColor: JXG.palette.black,
      fillColor: JXG.palette.black, fillOpacity: 0.2,
      label: {strokeColor: JXG.palette.black,
      anchorX: 'middle', anchorY: 'middle'},
    },
    point: {
      withLabel: false, size: 0, fixed: true,
      highlight: false, showInfobox: false,
      strokeWidth: 1, strokeColor: JXG.palette.black,
      fillColor: JXG.palette.black,
    },
  },
}];
