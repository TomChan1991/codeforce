import sys
inpy = [int(x) for x in sys.stdin.read().split()]
n, m, x, k, y  = inpy[0:5]
a, b = inpy[5:5+n], inpy[5+n:]
# print(a, b)
prei = -1
i, j = 0, 0
res = 0
def remove(l, r):
    if l > r:
        return 0
    lp, rp = a[l - 1] if l > 0 else 0, a[r + 1]
    maxV = max(a[l:r + 1])
    res = None
    if maxV < max(lp, rp):
        res = (r - l + 1) * y
    if r - l + 1 >= k:
        cur = (r - l + 1) // k * x + (r - l + 1) % k * y
        if res:
            res = max(res, cur)
        else:
            res = cur
    return res

while i < len(a) and j < len(b):
    # print(a[i], b[j], 'ab')
    if a[i] == b[j]:
        x = remove(prei + 1, i - 1)
        if (x == None):
            break
        res += x
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




