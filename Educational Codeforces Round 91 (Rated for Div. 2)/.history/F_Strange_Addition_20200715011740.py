n, m = [int(i) for i in input().split()]
s = input()
s = list(int(i) for i in s)
for i in range(m):
    a, b = [int(i) for i in input().split()]
    s[a - 1] = b
    res = 0
    prec, p, pp = 9, 1, 1, 0
    for c in reversed(s):
        cur = c * p
        (c * 10 + prec)   
