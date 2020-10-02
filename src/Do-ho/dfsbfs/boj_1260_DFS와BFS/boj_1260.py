import sys

def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            if n in graph:
                queue += sorted(graph[n] - set(visited))
    return visited

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                stack += sorted(graph[n] - set(visited), reverse=True)
    return visited

[N, M, V] = map(int, sys.stdin.readline()[:-1].split(' '))

tree = {}

for i in range(N+1):
    tree[i] = set()

for i in range(M):
    [startPoint, endPoint] = list(map(int, sys.stdin.readline()[:-1].split(' ')))
    tree[startPoint].add(endPoint)
    tree[endPoint].add(startPoint)

print(" ".join(map(str, dfs(tree, V))))
print(" ".join(map(str, bfs(tree, V))))
