import sys
from collections import deque

D = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, sys.stdin.readline().strip().split())
MAZE = deque()
for _ in range(N): MAZE.append(sys.stdin.readline().strip())

q = deque()
visited = [[False for _ in range(M)] for _ in range(N)]
q.append((0,0,1))
visited[0][0] = True

while q:
    tx, ty, moves = q.popleft()
    if(tx == N-1 and ty == M-1):
        sys.stdout.write(str(moves)+'\n')
        break
    for DIR in D:
        nx, ny = [tx + DIR[0], ty + DIR[1]]
        if(nx < 0 or nx >= N or ny < 0 or ny >= M): continue
        if(MAZE[nx][ny] == '0' or visited[nx][ny]): continue
        q.append((nx, ny, moves+1))
        visited[nx][ny] = True