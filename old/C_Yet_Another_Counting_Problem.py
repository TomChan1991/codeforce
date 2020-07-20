import math
line = input()
t = int(line)
for _ in range(t):
    line = input()
    a, b, q = (int(i) for i in line.split(' '))
    g = a * b // math.gcd(a, b)
    memo = [0] * (g)
    for i in range(1, g):
        if (i % a) % b != (i % b) % a:
            memo[i] = memo[i-1] + 1
        else:
            memo[i] = memo[i - 1]
    for i in range(q):
        line = input()
        l, r = (int(i) for i in line.split(' '))
        l -= 1
        res = r // (g) * memo[-1] + memo[r % (g)]
        res -= l // (g) * memo[-1] + memo[l % (g)]
        print(res)


