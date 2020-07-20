import sys
inpy = [x for x in sys.stdin.read().split()]
n, m = int(inpy[0]), int(inpy[1])
s = list(int(i) for i in inpy[2])
index = 3
for i in range(m):
    a, b = int(inpy[index]), int(inpy[index + 1])
    index += 2
    s[a - 1] = b
    # print(s)
    pre, p, pp = 9, 1, 0
    for c in reversed(s):
        # print(p, pp, 'p')
        cur = (c + 1) * p
        # print(cur)
        if c == 1:
            cur += max(19 - (c * 10 + pre), 0) * pp
        pre = c
        pp, p = p, cur
    print(p)
