# 25

import sys

sys.setrecursionlimit(10000)

def fib(i, prev, cur, targLen):
    if len(str(cur)) == targLen:
        print(f'{cur}\n{i}')
    else:
        fib(i + 1, cur, prev + cur, targLen)

fib(2, 1, 1, 1000)
    