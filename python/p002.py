# 2

num0 = 1
num1 = 2
total = 0

while num1 < 4000000:
	if num1 % 2 == 0:
		total += num1
	t = num1
	num1 = num0 + num1
	num0 = t

print(total)
