import sys
inpy = [int(x) for x in sys.stdin.read().split()]
n, m, x, k, y  = inpy[0:5]
a, b = inpy[5:5+n], inpy[5+n:]
print(a, b)
prei = -1
i, j = 0, 0
res = 0
while i < len(a) and j < len(b):
    if a[i] == b[j]:
        # print(i, j, 'equal')
        flag = True
        maxV = 0
        for k in range(prei + 1, i):
            maxV = max(maxV, a[k])
        minMana = None
        if max(a[prei] if prei >= 0 else 0, a[i]) > maxV:
            minMana = y * (i - prei - 1)
        if i - prei > k:
            minMana = min(((i - prei - 1) // k) * x + ((i - prei - 1) % k) * y, minMana if minMana else 999999999999999999)
        if minMana == None:
            break
        res += minMana
        prei = i
        j += 1
    i += 1
    # print(i, j)
if j == len(b):
    maxV = 0
    for j in range(prei + 1, len(a)):
        maxV = max(maxV, a[j])
    minMana = None
    if a[prei] > maxV:
        minMana = y * (len(a) - prei - 1)
    if i - prei > k:
        minMana = min(((len(a) - prei - 1) // k) * x + ((len(a) - prei - 1) % k) * y, minMana)
    if minMana == None:
        print(-1)
    else:
        print(res + minMana)
else:
    print(-1)




