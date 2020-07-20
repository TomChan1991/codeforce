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
        if x / k > y:
            cur =  x + (r - l + 1 - k) * y
        else:            
            cur = (r - l + 1) // k * x + (r - l + 1) % k * y
        if res:
            res = min(res, cur)
        else:
            res = cur
    return res

while i < len(a) and j < len(b):
    # print(a[i], b[j], 'ab')
    if a[i] == b[j]:
        xx = remove(prei + 1, i - 1)
        if (xx == None):
            break
        res += xx
        prei = i
        j += 1
    i += 1
    # print(i, j)
# print(j)
if j == len(b):
    xx = remove(prei + 1, len(a) - 1)
    # print(xx)
    if xx == None:
        print(-1)
    else:
        print(res + xx)
else:
    print(-1)




