import sys
from collections import deque

directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

[M, N, H] = map(int, sys.stdin.readline().split())

tomato = []

for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int, sys.stdin.readline().split())))
    tomato.append(tmp)

def function():
    ripeTomatos = deque()
    visited = [[[False for i in range(M)] for i in range(N)] for i in range(H)]

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k] == 1:
                    ripeTomatos.append((i, j, k, 0))

    day = 0

    while ripeTomatos:
        z, y, x, day = ripeTomatos.popleft()
        if tomato[z][y][x]==0: tomato[z][y][x] = 1
        for dx, dy, dz in directions:
            nx, ny, nz = x+dx, y+dy, z+dz
            if nx<0 or ny<0 or nz<0 or nx>=M or ny>=N or nz>=H: continue
            if tomato[nz][ny][nx] == 0:
                if not visited[nz][ny][nx]:
                    ripeTomatos.append((nz, ny, nx, day+1))
                    visited[nz][ny][nx] = True
    
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k] == 0:
                    return -1
                    
    return day

sys.stdout.write(str(function()))