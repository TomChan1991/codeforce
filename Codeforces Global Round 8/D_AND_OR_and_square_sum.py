import sys
inpy = [int(x) for x in sys.stdin.read().split()]
n = inpy[0]
memo = [0] * 21

for i in inpy[1:]:
    num = i
    for j in range(21):
        if num & 1:
            memo[j] += 1
        num = num >> 1

res = 0
for i in range(n):
    cur, x = 0, 1
    for j in range(21):
        if memo[j] > 0:
            memo[j] -= 1
            cur += x
        x = x << 1
    res += cur ** 2
print (res)


    
