import sys
inpy = [int(x) for x in sys.stdin.read().split()]
t = inpy[0]
index = 1
for _ in range(t):
    n, m = inpy[index], inpy[index + 1]
    index += 2
    a, b = [0] * m, [[0, 0] for _ in range(m)]
    for i in range(m):
        a[i] = inpy[index]
        b[i] = (inpy[index + 1], inpy[index])
        index += 2
    a.sort(reverse=True)
    b.sort(reverse=True)
    res, cur, j = 0, 0, 0
    for i in range(m):
        while j < m and n > 0 and b[i][0] < a[j]:
            cur += a[j]
            j += 1
            n -= 1
        if n == 0:
            break
        if b[i][1] > b[i][0]:
            res = max(res, cur + b[i][0] * n)
        else:
            res = max(res, cur + b[i][1] + b[i][0] * (n - 1))
        
    print(res)
    print(a, b)
    