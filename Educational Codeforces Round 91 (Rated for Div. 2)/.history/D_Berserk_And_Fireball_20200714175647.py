import sys
inpy = [int(x) for x in sys.stdin.read().split()]
n, m, x, k, y  = inpy[0:5]
a, b = inpy[5:5+n], inpy[5+n:]
prei = -1
i, j = 0, 0
res = 0
while i < len(a) and j < len(b):
    print(i, j)
    if a[i] == b[j]:
        flag = True
        maxV = 0
        for j in range(prei + 1, i):
            maxV = max(maxV, a[j])
        minMana = None
        if max(a[prei] if prei > 0 else 0, a[i]) > minMana:
            minMana = y * (i - prei - 1)
            print('a')
        if i - prei > k:
            minMana = min(((i - prei - 1) // k) * x + ((i - prei - 1) % k) * y, minMana)
        if not minMana:
            break
        res += minMana
        prei = i
        j += 1
    i += 1
if j == len(b):
    for j in range(prei + 1, len(a)):
            maxV = max(maxV, a[j])
    minMana = None
    if a[prei] > minMana:
        minMana = y * (i - prei - 1)
    if i - prei > k:
        minMana = min(((i - prei - 1) // k) * x + ((i - prei - 1) % k) * y, minMana)
    if not minMana:
        print(-1)
    else:
        print(res + minMana)
else:
    print(-1)




