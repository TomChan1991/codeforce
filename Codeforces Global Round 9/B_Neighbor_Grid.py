import sys
inpy = [int(x) for x in sys.stdin.read().split()]
t = inpy[0]
index = 1
for _i in range(t):
    n, m = inpy[index], inpy[index + 1]
    index += 2
    grid = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            grid[i][j] = inpy[index]
            index += 1   
    if grid[0][0] > 2 or grid[0][-1] > 2 or grid[-1][0] > 2 or grid[-1][-1] > 2:
        print('NO')
        
        continue
    grid[0][0], grid[0][-1], grid[-1][0], grid[-1][-1] = 2, 2, 2, 2
    flag = True
    for i in range(1, m - 1):
        if grid[0][i] > 3 or grid[-1][i] > 3:
            print('NO')
            flag = False
            break
        grid[0][i], grid[-1][i] = 3, 3
    
    if not flag:
        continue

    for i in range(1, n - 1):
        if grid[i][0] > 3 or grid[i][-1] > 3:
            print('NO')
            flag = False
            break
        grid[i][0], grid[i][-1] = 3, 3
    
    if not flag:
        continue
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if grid[i][j] > 4:
                print('No')
                flag = False
                break
            grid[i][j] = 4
        if not flag:
            break
    if not flag:continue
    print('YES')
    for i in range(n):
        for j in range(m):
            print(grid[i][j], end=' ')
        print()
    