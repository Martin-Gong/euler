# 24

from math import factorial

n = list(range(10))
f = []

left = 1000000

for i in range(9):
    if left % factorial(9 - i) == 0:
        f += [n.pop(int(left / factorial(9 - i)) - 1)]
    else:
        f += [n.pop(int(left / factorial(9 - i)))]
    left = left % factorial(9 - i)

f += n

print(f)