class Node:
    l, r = 0, 0
    index = -1
    con = {}
    lc, rc = None, None

import sys
import collections
arr = [int(x) for x in sys.stdin.read().split()]
n, q = arr[0], arr[1]
memo = [0] * (n+1)
