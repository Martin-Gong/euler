# 28
# It can be found that the sum for any circular level (4 numbers),
# where number 1 is level 1, is given by 4(1+4(l-1)(2l+3))+12(l-1)
# which expands to 16 - 28l + 16l^2

print(1 + sum(16 - 28*l + 16*l**2 for l in range(2, 502)))