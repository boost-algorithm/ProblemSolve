import sys
from queue import PriorityQueue

que = PriorityQueue()

N = int(sys.stdin.readline())

for i in range(N):
    x = int(sys.stdin.readline())
    if(x!=0): que.put((abs(x), x))
    else:
        if que.empty(): print(0)
        else: print(que.get()[1])