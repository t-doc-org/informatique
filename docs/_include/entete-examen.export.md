% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

<style>
table.points > thead > tr > th {
  min-width: 3rem;
}
</style>

````{list-grid} 5fr 1fr
:style: gap: 4rem;
- Nom, prénom: {leader}`.`
- Note:
````
```{flex-table} grid points align-left
{t=h}|{.l}Question   |{points=label}|Total
{t=b}|{t=h .l}Points |{points=value}|{points=sum}
     |{t=h .l}Obtenus|{points=empty}|
```
