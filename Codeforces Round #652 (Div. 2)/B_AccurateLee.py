import collections

t = int(input())
for _i in range(t):
    n = int(input())
    s = input()
    i, j = 0, 0
    for c in s:
        if c == '0':
            i += 1
        else:
            break
    for c in reversed(s):
        if c == '1':
            j += 1
        else:
            break
    if i + j == len(s):
        print(s)
    else:
        print('0' * (i + 1) + '1' * j)


    
