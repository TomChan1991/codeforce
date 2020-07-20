line = input()
t = int(line)
for _ in range(t):
    line = input()
    cnt_one = line.count('1')
    if cnt_one == 0 or cnt_one == len(line):
        print(line)
    else:
        print(('10' * len(line)))
