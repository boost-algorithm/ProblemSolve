import sys
import copy
from itertools import combinations
from collections import deque

[N, M] = list(map(int, sys.stdin.readline().split()))
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
alphabet = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5
}

myMap = []
myCheck = [[[False for _ in range(64)] for _ in range(M)] for _ in range(N)]

for _ in range(N):
    myMap.append(list(sys.stdin.readline()[:-1]))

# 맵 중 민식이 위치 찾기 (민식이는 무조건 있다)
def findMinsik():
    for i in range(len(myMap)):
        for j in range(len(myMap[0])):
            if myMap[i][j]=='0':
                return (i, j, 0, 0)

def findMoon():
    queue = deque()
    queue.append(findMinsik())
    myCheck[queue[0][0]][queue[0][1]][0] = True
    while queue:
        target = queue.popleft()
        for direction in directions:
            nr = target[0] + direction[0]
            nc = target[1] + direction[1]
            nk = copy.deepcopy(target[2])

            if nr >= N or nr < 0 or nc >= M or nc < 0: continue
            if myMap[nr][nc] == '1': return target[3] + 1
            if myMap[nr][nc] == '#' or myCheck[nr][nc][nk]: continue
            if myMap[nr][nc].isupper():
                if nk == 0 or (nk >> alphabet[myMap[nr][nc]]) % 2 != 1: continue
            if myMap[nr][nc].islower():
                uA = myMap[nr][nc].upper()
                if nk == 0 or (nk >> alphabet[uA]) % 2 != 1: nk += pow(2,alphabet[uA])

            myCheck[nr][nc][nk] = True
            queue.append((nr, nc, nk, target[3]+1))
    return -1
    
print(findMoon())