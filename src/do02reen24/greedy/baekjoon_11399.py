import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
p.sort()

ans = 0
waitSum = 0

for num in p:
    waitSum = waitSum + num
    ans = ans + waitSum
print(ans)
