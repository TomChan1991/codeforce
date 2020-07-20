t = int(input())
for _ in range(t):
    n, r = [int(i) for i in input().split()]
    res = 0
    r = min(r, n)
    if n == r:
        print((1 + n - 1) * (n - 1 )// 2 + 1)
    else:
        print((1 + r) * r // 2)
  
    