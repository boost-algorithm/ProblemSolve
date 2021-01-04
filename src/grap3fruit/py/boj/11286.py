import heapq
import sys

# n = 18
# x = [1,
# -1,
# 0,
# 0,
# 0,
# 1,
# 1,
# -1,
# -1,
# 2,
# -2,
# 0,
# 0,
# 0,
# 0,
# 0,
# 0,
# 0]

n = int(sys.stdin.readline().strip())
heap = []
x = []
for i in range(0, n):
  x.append(int(sys.stdin.readline().strip()))

for i in range(0,n):
  if x[i] == 0:
    if len(heap) == 0:
      print(0)
      continue
    
    print(heapq.heappop(heap)[1])
    continue
  if x[i] != 0:
    heapq.heappush(heap,(abs(x[i]),x[i]))
