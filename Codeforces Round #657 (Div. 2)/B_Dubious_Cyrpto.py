import sys
inpy = [int(x) for x in sys.stdin.read().split()]
t = inpy[0]
index = 1
for _ in range(t):
    l, r, m = inpy[index:index + 3]
    index += 3
    for i in range(l, r + 1):
        rest = m % i
        if rest <= (r - l) and m // i > 0:
            print(i, l + rest, l)
            break
        elif i - rest <= (r - l):
            print(i, l, l + i - rest)
            break
    