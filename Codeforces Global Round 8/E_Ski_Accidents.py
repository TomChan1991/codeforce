import sys
import collections
inpy = [int(x) for x in sys.stdin.read().split()]
t = inpy[0]
index = 1
for _ in range(t):
    n, m = inpy[index:index + 2]
    index += 2
    fro = [set() for _ in range(n + 1)]
    for i in range(m):
        x, y = inpy[index:index + 2]
        index += 2
        fro[x].add(y)
    print(fro)
    
    for j in range(1, n + 1):
        que = collections.deque()
        exist, de, re = set(), set(), set()
        for i in range(j, n + 1):
            if not que and i not in exist:
                que.append(i)
            else:
                continue
            while que:
                x = que.popleft()
                print('x', x)
                if x in exist or x in de:
                    continue
                flag = True
                for j in fro[x]:
                    if j in re:
                        flag = False
                if flag:
                    exist.add(x)
                    for j in fro[x]:
                        que.append(j)
                        re.add(j)
                else:
                    de.add(x)
            print('e', exist)
            if len(exist) > n * 3 / 7:
                break
        if len(exist) > n * 3 / 7:
            for i in range(1, n + 1):
                if i not in exist:
                    print(i, end=' ')
            print()
            break



