import sys

def bfs(graph, start):
    visited = []
    queue = [start]

    while len(queue)!=0:
        target = queue.pop(0)
        if target not in visited:
            visited.append(target)
            for item in graph[target]:
                queue.append(item)
    return len(visited)-1

computerNum = int(sys.stdin.readline()[:-1])
lineNum = int(sys.stdin.readline()[:-1])
graph = {}

for i in range(lineNum):
    [node1, node2] = map(int, sys.stdin.readline()[:-1].split(' '))
    try: graph[node1].append(node2)
    except: graph[node1] = [node2]
    
    try: graph[node2].append(node1)
    except: graph[node2] = [node1]

print(bfs(graph, 1))