from z3 import *

A = Bool("A")
B = Bool("B")
C = Bool("C")
D = Bool("D")

s = Solver()
s.add(A == And(D, B), Implies(C, B), Not(Or(A, B, Not(D))), Or(And(Not(A), C), D))

print(s.check())
print(s.model())

# answer:
# sat
# [A = False, D = True, B = False, C = False]