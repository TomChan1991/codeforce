import sys
line = input()
t = int(line)
for _ in range(t):
    line = input()
    n = int(line)
    line = input()
    need = [int(i) for i in line.split(' ')]
    line = input()
    station =[int(i) for i in line.split(' ')]
    flag = True
    xmax, cur, x = station[-1], 0, station[-1]
    for i in range(n - 1):
        cur = cur + station[i] - need[i]
        if cur < 0:
            xmax += cur
            x += cur
            cur = 0
        cur = min(cur, station[i])
        xmax = min(xmax, station[i] - cur)
        if xmax < 0:
            flag = False
            break
    if flag and x + cur >= need[-1]:
        print('YES')
    else:
        print('NO')

            
            

