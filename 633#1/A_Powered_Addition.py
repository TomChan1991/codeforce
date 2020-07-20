import math
n = input()
n = int(n)
for i in range(n):
    l = int(input())
    x = input()
    arr = x.split(' ')
    minV = -(1<<32)
    res = 0
    for j in arr:
        j = int(j)
        if j < minV:
            t = math.ceil((math.log2(minV - j + 1)))
            res = max(t, res)
        else: minV = j
    print(res)
            