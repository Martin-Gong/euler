# 27
# isPrime() takes reference from https://stackoverflow.com/a/15285588/8828580

import numpy as np

def isPrime(n):
  if n == 2 or n == 3: return True
  if abs(n) < 2 or n % 2 == 0 or n % 3 == 0: return False

  r = int(n ** 0.5)
  f = 5

  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True    

def getPrimeList(n):
    p = [1] * n
    p[0] = 0
    p[1] = 0

    for val in range(1, n):
        if p[val] == 0: continue
        for i in range(2 * val, n, val): p[i] = 0

    return list(val for val in range(n) if p[val] == 1)

recLen = 0
recNums = [0, 0]

pList = getPrimeList(1000)
pList = list(np.negative(pList)) + pList

for a in range(-999, 1000):
    for b in pList:
        if abs(b) < recLen: continue
        n = 1
        while isPrime(abs(n**2 + a * n + b)):
            if n > recLen:
                recLen = n
                recNums = [a, b]
            n += 1

print(recLen, recNums)
print(recNums[0] * recNums[1])
