import sys
import collections

T = int(sys.stdin.readline())
for i in range(T):
  deq = collections.deque([])
  N = int(sys.stdin.readline())
  datas = list(map(int,sys.stdin.readline().strip().split()))
  datas.sort(reverse=True)

  count = 0
  for data in datas:
    if count % 2 == 0:
      deq.append(data)
    if count % 2 == 1:
      deq.appendleft(data)
    
    count += 1

  print(deq)
  max_gap = 0
  for j in range(-1, N-1):
    gap = abs(deq[j]-deq[j+1])
    if gap > max_gap:
      max_gap = gap
  
  print(max_gap)
