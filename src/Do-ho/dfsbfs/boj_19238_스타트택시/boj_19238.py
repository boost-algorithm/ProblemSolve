import sys

# N : 활동 영역(가로 * 세로)
# M : 승객의 수
# fuel : 처음 소지한 연료
[N, M, fuel] = map(int, sys.stdin.readline()[:-1].split(' '))

road = []

# 길 입력
for i in range(N):
    appendArr = list(map(int, sys.stdin.readline()[:-1].split(' ')))
    road.append(appendArr)

# 택시 처음 좌표 입력
[taxiX, texiY] = map(int, sys.stdin.readline()[:-1].split(' '))

# 손님 위치 및 목적지 입력
for i in range(M):
    cus = list(map(int, sys.stdin.readline()[:-1].split(' ')))
    road[cus[0]-1][cus[1]-1] = i+2
    road[cus[2]-1][cus[3]-1] = -(i+2)

print(road)

def dfs(startPoint, endPoint):
    num = 0

    # if(startPoint[0]>=endPoint[0]):
    

    return num