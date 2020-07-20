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
    lp, rp = a[l - 1] if l > 0 else 0, a[r + 1] if r + 1 < len(a) else 0
    maxV = max(a[l:r + 1])
    res = None
    if maxV < max(lp, rp):
        res = (r - l + 1) * y

    if r - l + 1 >= k:
        cur = (r - l + 1) // k * x + (r - l + 1) % k * y
        print(cur, (r - l + 1) )
        if res:
            res = min(res, cur)
        else:
            res = cur
    return res

while i < len(a) and j < len(b):
    # print(a[i], b[j], 'ab')
    if a[i] == b[j]:
        x = remove(prei + 1, i - 1)
        print(prei + 1, i - 1, x)
        if (x == None):
            break
        res += x
        prei = i
        j += 1
    i += 1
    # print(i, j)
print('c')
if j == len(b):
    print('d')
    x = remove(prei + 1, len(a) - 1)
    print(x)
    if (x == None):
        print(-1)
    else:
        print(res + x)
else:
    print(-1)




