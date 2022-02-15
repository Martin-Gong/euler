# 22

import csv
import os


ref = []

with open(os.path.join(os.path.dirname(__file__), 'p022.in')) as file:
    for i in next(csv.reader(file, delimiter=',')):
        ref.append(i)

ref.sort()
print(sum((i + 1) * sum(ord(c) - 64 for c in str(val)) for i, val in enumerate(ref)))