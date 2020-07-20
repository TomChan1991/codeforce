import sys
inpy = [int(x) for x in sys.stdin.read().split()]
n, m, x, k, y  = inpy[0:5]
a, b = inpy[5:5+n], inpy[5+n:]
memo = {0: 0}
i, j = 0, 0
while i < n:
    

