line = '4 3'
n, k  = (int(i) for i in line.split(' '))
if k >= n:
    print(0)
    exit()
C = [1]
for i in range(n):
    C.append(1)
    for j in range(i, 0, -1):   
        C[j] = C[j] + C[j-1]
memo = [[-1] * (k + 1) for _ in range(n+1)]
for i in range(n + 1):


    for j in range(k  + 1):        
        