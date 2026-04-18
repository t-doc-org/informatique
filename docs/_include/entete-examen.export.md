% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

<style>
.exam-header {
  margin-top: 0;
  grid-template-columns: 5fr 1fr;
  gap: 4rem;
}
table.points > thead > tr > th {
  min-width: 3rem;
}
</style>

````{list-grid}
:class: exam-header
- Nom, prénom: {leader}`.`
- Note:
````
```{flex-table}
:class: points grid align-left
{t=h}|{.l}Question   |{points=label}|Total
{t=b}|{t=h .l}Points |{points=value}|{points=sum}
     |{t=h .l}Obtenus|{points=empty}|
```
