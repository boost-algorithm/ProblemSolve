import sys
from collections import deque

directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

[M, N, H] = map(int, sys.stdin.readline()[:-1].split(' '))

tomato = []

for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int, sys.stdin.readline()[:-1].split(' '))))
    tomato.append(tmp)

def function():
    underripeTomatos = deque()
    isAllRipeTomatos = True

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k] == 0:
                    underripeTomatos.append((i, j, k))
                    isAllRipeTomatos = False

    if isAllRipeTomatos: return 0

    days = 0

    while underripeTomatos:
        visited = [[[False for i in range(M)] for i in range(N)] for i in range(H)]
        target = underripeTomatos.popleft()
        if not visited[target[0]][target[1]][target[2]]:
            tmp = isExistGoodTomato(target, visited)
            if tmp == 0: return -1
            if days <= tmp: days = tmp
            
    return days

def isExistGoodTomato(underripeTomato, parentvisited):
    visited = [[[False for i in range(M)] for i in range(N)] for i in range(H)]
    queue = deque()
    queue.append((underripeTomato, 1))

    while queue:
        tmp = queue.popleft()
        target = tmp[0]
        count = tmp[1]
        if not visited[target[0]][target[1]][target[2]]:
            visited[target[0]][target[1]][target[2]] = True
            for direction in directions:
                x = target[2] + direction[2]
                y = target[1] + direction[1]
                z = target[0] + direction[0]

                if x<0 or y<0 or z<0 or x>=M or y>=N or z>=H: continue
                elif tomato[z][y][x] == 1: return count
                elif tomato[z][y][x] == -1: continue
                else:
                    if not parentvisited[z][y][x]: parentvisited[z][y][x] = True
                    if not visited[z][y][z]: queue.append(((z, y, x), count + 1))
    return 0

sys.stdout.write(str(function()))