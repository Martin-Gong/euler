# 7

# [Finished in 4.8s]
primes = [2]

currentNum = 3
primesFound = 1

while True:
	if primesFound == 10001:
		break
	isPrime = True
	for p in primes:
		if currentNum % p == 0:
			isPrime = False
			break
	if isPrime:
		primesFound += 1
		primes.append(currentNum)
	currentNum += 2

print(primes)
print(primes[-1])