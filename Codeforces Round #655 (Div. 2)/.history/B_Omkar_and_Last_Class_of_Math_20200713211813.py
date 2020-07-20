import sys
import math
inpy = [int(x) for x in sys.stdin.read().split()]
t = inpy[0]
for _t in range(t):
    n = inpy[_t + 1]
    if n % 2 == 0:
        print(n // 2, n // 2)
        continue
    s = math.sqrt(n)
    i = 3
    while i <= s:
        if n % i == 0:
            print(n // i, n - n // i)
            break
        i += 2
    if n % i != 0:
        print(1, n - 1)
    



