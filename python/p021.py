# 21

def getFactorSums(num):
    factors = [1]
    for i in range(2, num):
       if num % i == 0:
           factors += [i]
    return sum(factors)

ref = []

s = 0
for i in range(10000):
    if getFactorSums(getFactorSums(i + 1)) == i + 1 and i + 1 != getFactorSums(i + 1):
        s += getFactorSums(i + 1)

print(s)

### Originally thought question asked to preserve repetition. A weird labeling algorithm that also works...

# for i in range(10000):
#     if getFactorSums(getFactorSums(i + 1)) == i + 1 and i + 1 != getFactorSums(i + 1):
#         ref.append([i + 1, getFactorSums(i + 1), 1])
#     else:
#         ref.append([i + 1, getFactorSums(i + 1), 0])

# print(sum(n for n, s, i in ref if i == 1))
