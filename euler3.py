# 3

# [Finished in 134ms]
const = 600851475143

def printPrimeFactors():
	global const
	while True:
		for f in range(3,const):
			if const % f == 0:
				print(f)
				const = int(const / f)
				break
			if f == const - 1:
				print(const)
				return

printPrimeFactors()
