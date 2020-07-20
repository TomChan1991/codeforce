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
    print(a, b)
    