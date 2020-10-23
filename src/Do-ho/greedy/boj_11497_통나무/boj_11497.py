import sys
from collections import deque

def diff(a, b):
    return abs(a-b)

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    tongtree = list(map(int, sys.stdin.readline().split()))
    newtongtree = deque()
    tongtree.sort()
    
    for item in tongtree:
        topIdx = len(newtongtree)
        if topIdx <= 1: newtongtree.append(item)
        else:
            if newtongtree[0] > newtongtree[topIdx-1]: newtongtree.append(item)
            else: newtongtree.appendleft(item)
    
    maxDiff = diff(newtongtree[0], newtongtree[1])
    for idx in range(N-1):
        value = diff(newtongtree[idx], newtongtree[idx+1])
        if maxDiff < value: maxDiff = value
    
    print(maxDiff)