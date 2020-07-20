line = input()
t = int(line)
for _ in range(t):
    line = input()
    one, zero = line.count('1'), line.count('0')
    cnt = min(one, zero)
    if cnt % 2:
        print('DA')
    else:
        print('NET')