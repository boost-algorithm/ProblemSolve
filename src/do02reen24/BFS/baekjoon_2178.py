import sys

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(sys.stdin.readline().rstrip())

visited = [[-1 for _ in range(m)] for _ in range(n)]
visited[0][0] = 1
visit = [(0,0)]
new_visit = []
while visit:
    x, y = visit.pop()
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if mx >= 0 and mx < n and my >=0 and my < m:
            if visited[mx][my] != -1 or board[mx][my] == "0": continue
            visited[mx][my] = visited[x][y] + 1
            new_visit.append((mx, my))
    if not visit:
        visit = new_visit
        new_visit = []
        
print(visited[n-1][m-1])