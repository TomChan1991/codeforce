import sys

inpy = [int(x) for x in sys.stdin.read().split()]
print(inpy)
t = inpy[0]
for _i in range(t):
    a, b, n = inpy[_i * 3 + 1: _i * 3 + 4]
    s = 0
    while a < n or b < n:
        a, b = a + b , max(a, b)
        # print(a, b)
        s += 1
    print(s)