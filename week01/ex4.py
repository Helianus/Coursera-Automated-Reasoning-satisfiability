from z3 import *

A = Int("A")
B = Int("B")
C = Int("C")

A = 98798798987987987987987923423
B = 763429999988888888887364578645

s = Solver()
#s.add(C + C == (87*A + 93*B))
s.add(simplify(C + C == (87*A + 93*B)))

print(s.check())
print(s.model())

# answer:
# sat
# [C = 39797242755460810810739927575893]