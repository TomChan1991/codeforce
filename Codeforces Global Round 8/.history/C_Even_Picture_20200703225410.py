import sys
inpy = [int(x) for x in sys.stdin.read().split()]
n = inpy[0]
print(3 * n + 4)
x, y = 0, 0
for i in range(n + 1):
    print(x, y)
    print(x + 1, y)
    print(x, y + 1)
    x, y = x + 1, y + 1
print(x, y)
    
