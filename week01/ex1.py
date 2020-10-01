from z3 import *

a = Int("a")
b = Int("b")
c = Int("c")
d = Int("d")

s = Solver()
s.add(2*a > b+c, 2*b > c+d, 2*c > 3*d, 3*d > a+c)
print(s.check())
print(s.model())

# answer:
# sat
# [c = 32, a = 30, b = 27, d = 21]
