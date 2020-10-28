def lcm(a, b, next):
	num = a
	while not num % b == 0:
		num += a
	if next == 0: 
		return num
	return lcm(num, next, next - 1)

print(lcm(20, 19, 18))