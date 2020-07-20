import sys
inpy = [int(x) for x in sys.stdin.read().split()]
n, m = inpy[0], inpy[1]
index = 2
grid = [[] for _ in range(n)]
for i in range(n):
    x = grid[index]
    index += 1
    for j in range(x):
        grid[i].append(inpy[index], inpy[index + 1])
        index += 1

start = [0] * n
