from z3 import *

f = Function("f", IntSort(), IntSort())

s = Solver()
s.add(2*f(1) > f(2)+f(3), 2*f(2) > f(3) + f(4), 2*f(3) > 3*f(4), 3*f(4) > f(1) + f(3))

print(s.check())
print(s.model())

# answer:
# sat
# [f = [1 -> 30, 2 -> 27, 4 -> 21, else -> 32]]

print(s.model().evaluate(f(1)))
# answer: 30

print(s.model().evaluate(f(2)))
# answer: 27

print(s.model().evaluate(f(3)))
# answer: 32

print(s.model().evaluate(f(4)))
# answer: 21