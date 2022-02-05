# 9

# [Finished in 355ms]
for i in range(1000):
	for j in range(i + 1,1000):
		if i**2 + j**2 > (1000 - i - j)**2:
			continue
		if i**2 + j**2 == (1000 - i - j)**2 and j != 1000 - i - j:
			print(i,j,(1000 - i - j))
			print(i*j*(1000 - i - j))
			exit(0)