import math
import collections
line = input()
test = int(line)
memo = {}
con = ['00', '10', '11', '01']
for _ in range(test):
    line = input()
    n = int(line)
    if n <= 4:
        print(n)
        continue
    n = n - 1
    if n in memo:
        print(memo[n])
        continue
    a, b = n // 3, n % 3
    l = math.ceil(math.log2(3 * a + 2) / 2) - 1
    base = 4 ** l
    a -= (4**l - 1) // 3
    # base = 1
    # while a >= base:
    #     a -= base
    #     base *= 4
    f = base + a 
    if b == 0:
        print(f)
        continue
    res  = collections.deque(['10'])
    base = base // 4
    while base >= 1:
        x = a // base
        a = a % base
        res.append(con[x])
        base = base // 4
    # res += memo2[a]
    s = int(''.join(res), base=2)
    if b == 1:
        memo[n+1] = f ^ s 
        print(s)
    else:
        memo[n-1] = s 
        print(f ^ s)
    






   