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
x = (n - 1) // 2
odd, even = 0, 0
for i in range(1, n, 2): # x
    odd += nums[i]
for i in range(0, n, 2): # x + 1
    even += nums[i]
res = even
even -= nums[-1]
for i in range(n):
    cur = 



