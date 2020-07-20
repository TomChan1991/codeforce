class node:
    def __init__(self):
        self.all = set()
        self.order = []

nodes = set()
n = node()
n.all.add(1)
nodes.add(n)
print(nodes)


# line = input()
# t = int(line)
# for _ in range(t):
#     line = input()
#     n = int(line)
#     num = []
#     for i in range(n - 1):
#         line = input()
#         temp = line.split(' ')
#         num.append(set([int(i) for i in temp[1:]]))
#     res, usingNum = [], set()
#     used, using = [False] * (n - 1), 0
#     while (using < n - 1):
#         for i in range(n - 1):
#             if used[i]: continue
#             if not res: 
#                 res.append(num[i])
#                 using, used[i] = using + 1, True
#                 usingNum.update(num[i])
#                 continue
#             same = usingNum & num[i]
#             if not same: continue
#             new = num[i] - same
#             rm = usingNum  - same
#             if not rm:
#                 res = 

#     print(num)
