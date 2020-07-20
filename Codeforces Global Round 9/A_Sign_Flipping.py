import sys
inpy = [int(x) for x in sys.stdin.read().split()]
t = inpy[0]
index = 1
for _i in range(t):
    n = inpy[index]
    index += 1
    for i in range(n):
        if i % 2 == 0:
            print(abs(inpy[index]), end=' ')
        else:
            print(-abs(inpy[index]), end=' ')
        index += 1
    print()