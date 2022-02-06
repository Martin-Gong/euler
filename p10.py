# 10

p = [1] * 2000000
p[0] = 0
p[1] = 0

s = 0

for val in range(1, 2000000):
	if p[val] == 0:
		continue
	s += val
	for i in range(val, 2000000, val):
		p[i] = 0

print(s)


# "Brute Force"
# [Finished in 1008.4s]
# primes = [2]

# currentNum = 3

# while True:
# 	if currentNum > 20000000:
# 		break
# 	isPrime = True
# 	for p in primes:
# 		if currentNum % p == 0:
# 			isPrime = False
# 			break
# 	if isPrime:
# 		primesFound += 1
# 		primes.append(currentNum)
# 	currentNum += 2

# print(sum(primes))
