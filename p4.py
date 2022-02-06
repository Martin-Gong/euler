# 4

def isPalin(n):
	return str(n)[::-1] == str(n)

curMax = 1

for i in range(1000, 1, -1):
	for j in range(1000, i, -1):
		if isPalin(i * j) and i * j > curMax:
			curMax = i * j
			print(curMax)
