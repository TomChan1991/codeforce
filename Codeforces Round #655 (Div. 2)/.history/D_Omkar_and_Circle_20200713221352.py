import sys
inpy = [int(x) for x in sys.stdin.read().split()]
n = inpy[0]
nums = inpy[1:]
if n == 1:
    print(inpy[1])
    exit()
if n == 3:
    print(sum(inpy[1:]) - min(inpy[1:]))
    exit()
# pick one
pick, nopick, picktwo = nums[1], nums[0], 0
for i in nums[2:-1]:
    x, y, z = pick, nopick, picktwo
    pick = y + i
    nopick = x
    picktwo = max(z, x + i)

pick, nopick = 0, 0
for i in nums[1:]:
    x, y, z = pick, nopick, picktwo
    pick = y + i
    nopick = x
    picktwo = max(z, x + i)