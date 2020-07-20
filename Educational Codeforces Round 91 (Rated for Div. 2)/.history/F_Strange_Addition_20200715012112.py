n, m = [int(i) for i in input().split()]
s = input()
s = list(int(i) for i in s)
print(s)
for i in range(m):
    a, b = [int(i) for i in input().split()]
    s[a - 1] = b
    pre, p, pp = 9, 1, 1, 0
    for c in reversed(s):
        cur = (c + 1) * p
        cur += max(19- (c * 10 + pre) , 0) * pp
        pre = c
        pp, p = p, cur
    print(p)
