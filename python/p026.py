# 26

def getRecurLen(n):
    seq = {}
    rem = 1 % n
    i = 1

    while(rem not in seq):
        seq[rem] = i
        rem = (10 * rem) % n
        if rem == 0:
            return 0
        i += 1
    
    return len(seq) - seq[rem] + 1

rec = 0

for d in range(1, 1000):
    n = getRecurLen(d)
    if n > rec:
        rec = d

print(rec)
