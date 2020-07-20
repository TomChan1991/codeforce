import sys
inpy = [int(x) for x in sys.stdin.read().split()]
n, m = inpy[0], inpy[1]
t = inpy[2: 2 + n]
qur = []
for i in range(m - 1):
    qur.append((inpy[i * 2 + 2 + n], inpy[i * 2 + 3 + n]))

