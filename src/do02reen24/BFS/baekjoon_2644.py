import sys

n = int(sys.stdin.readline())
p1, p2 = map(lambda data: int(data)-1, sys.stdin.readline().split())
relation = [[] for _ in range(n)]
m = int(sys.stdin.readline())
for _ in range(m):
    parent, children = map(lambda data: int(data)-1, sys.stdin.readline().split())
    relation[parent].append(children)
    relation[children].append(parent)
cost = [-1 for _ in range(n)]
cost[p1] = 0
count = 1
queue = [p1]
new_queue = []
while queue:
    person = queue.pop()
    for p in relation[person]:
        if cost[p] != -1: continue
        cost[p] = count
        new_queue.append(p)
    if not queue:
        queue = new_queue
        new_queue = []
        count = count + 1
print(cost[p2])