# 12

# [Finished in 4.3s]
def divsNum (num):
	counter = 0
	if (num**(1/2) == int(num**(1/2))):
		counter += 1
	for i in range(1,int(num**(1/2))):
		if num % i == 0:
			counter += 2
	return counter


num = 1
nextNum = 2

while True:
	if divsNum(num) > 500:
		print(num)
		break
	num += nextNum
	nextNum += 1
