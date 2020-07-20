import sys
import bisect
class Node:
    def __init__(self, left, right):
        super().__init__()
        self.nl, self.nr = None, None
        self.l, self.r = left, right
        self.arr = [[] for _ in range(2)]
        self.type = 1
        self.time = 0
inpy = [x for x in sys.stdin.read().split()]
n, q = int(inpy[0]), int(inpy[1])
s = inpy[2]

def nor(c):
    if c == '<':
        return '>'
    return '<'
def build(l, r):
    node = Node(l, r)
    if l == r:
        node.arr[0] = [s[l - 1], s[l - 1], 1]
        node.arr[1] = [nor(s[l]), nor(s[l - 1]), 1]
        return node
    mid = (l + r) // 2
    node.nl, node.nr = build(l, mid, mid + 1, r)


    





        
