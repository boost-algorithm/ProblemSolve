import sys
from collections import deque

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline())

r = {}

for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    try: r[x].append(y)
    except: r[x] = [y]
    try: r[y].append(x)
    except: r[y] = [x]

def dfs():
    q = deque()
    q.append((a, 0))
    visited = [False for _ in range(n+1)]

    while(q):
        target, chon = q.pop()
        if(target == b):
            return chon
        for item in r[target]:
            if(visited[item]): continue
            q.append((item, chon+1))
            visited[item] = True
    return -1

print(dfs())