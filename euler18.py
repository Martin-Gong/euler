# 18

def findMax (path, index, layer, amount):
    if layer == len(nums) - 1:
        return amount + nums[layer][index + path]
    return max(findMax(0, index + path, layer + 1, amount + nums[layer][index + path]), findMax(1, index + path, layer + 1, amount + nums[layer][index + path]))

f = open('euler18.in')
nums = []

for line in f.readlines():
    nums += [[int(x) for x in line.split()]]

print(findMax(0, 0, 0, 0))
