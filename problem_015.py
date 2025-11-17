# Lattice Paths

# How many such routes are there through a 20x20 grid

import sympy as sp

ROW = 20
COL = 20

# We have to move 20 times down and 20 times right
# (ROW+COL)! / ROW! / COL!
print(sp.binomial(ROW + COL, ROW))
