# 15

# Combinatorics
# [Finished in 185ms]
paths = 1

for i in range(1, 21):
	paths *= (20 + i) / i

print(round(paths))