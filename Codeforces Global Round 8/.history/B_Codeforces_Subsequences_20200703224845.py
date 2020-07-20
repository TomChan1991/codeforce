import sys
inpy = [int(x) for x in sys.stdin.read().split()]
n = inpy[0]
print(3 * n + 2)
print(0, 1)
for i in range(n):
    print(i + 1, 0)
    print(i + 1, 1)
    print(i + 1, 2)
print(n + 1, 1)
