n = int(input())
if n < 4:
    print(0)
    exit()
memo = [0] * n 
print(n // 2)
for i in range(0, n - 1, 2):
    memo[i] = 1
    print(i + 1, end=' ')
k = n // 2
for _i in range(10000):
    x = int(input())
    for i in range(x, x + k):
        memo[i % n] = 0
    ml, xs = 0, 0
    l, s = 0, 0
    for 

