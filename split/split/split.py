inpu = input()
x = inpu.split('ftp')
for i in x:
    yy = 'ftp' + i
    y = yy.split('http')
    f = True
    for j in y:
        if f:
            print(j)
            f = False
        else:
            print('http' + j)