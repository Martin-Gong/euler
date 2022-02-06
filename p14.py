# 14

d = {0: 0, 1: 1}

def itemInCollatz (num):
	if num in d:
		return d[num]
	if num == 0:
		return None
	if num % 2 == 0:
		return itemInCollatz(int(num / 2)) + 1
	else:
		return itemInCollatz(3 * num + 1) + 1

rec = 0
recNum = 0

for i in range(1,1000000):
	d[i] = itemInCollatz(i)
	if d[i] > rec:
		rec = d[i]
		recNum = i

print(recNum)


# [Finished in 39.0s]
# def itemInCollatz (num):
# 	if num == 0:
# 		return None
# 	if num == 1:
# 		return 1
# 	if num % 2 == 0:
# 		return itemInCollatz(num / 2) + 1
# 	else:
# 		return itemInCollatz(3 * num + 1) + 1

# rec = 0
# recNum = 0

# for i in range(1,1000000):
# 	if itemInCollatz(i) > rec:
# 		rec = itemInCollatz(i)
# 		recNum = i

# print(recNum)
