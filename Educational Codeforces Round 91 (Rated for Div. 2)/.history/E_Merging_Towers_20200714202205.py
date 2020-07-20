import sys
inpy = [int(x) for x in sys.stdin.read().split()]
n, m = inpy[0], inpy[1]
belong = inpy[2: 2 + n]

qur = []
for i in range(m - 1):
    qur.append((inpy[i * 2 + 2 + n], inpy[i * 2 + 3 + n]))

memo = [0] * (n - 1)
contianed = [set() for _ in range(m + 1)]
res = 0
for i in range(n -1):
    if belong[i] != belong[i+1]:
        memo[i] = 1
        res += 1
    

print(res)
for i, j in qur:

