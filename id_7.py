primes = [2]

currentNum = 3

primesFound = 1

while True:
	if primesFound == 10001:
		break
	state = True
	for p in primes:
		if currentNum % p == 0:
			state = False
			break
	if state:
		primesFound += 1
		primes.append(currentNum)
	currentNum += 2

print(primes)
print(primes[-1])