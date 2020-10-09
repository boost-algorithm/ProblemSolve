import sys
from collections import deque 

def conquer(arr):
    L = len(arr)
    A = L * L
    white = 0
    blue = 0

    if A==1: return arr[0][0]

    for i in range(L):
        for j in range(L):
            if arr[i][j] == 0: white += 1
            else: blue += 1
    
    if white==A: return 0
    elif blue==A: return 1
    else: return -1

def divide(arr):
    L = len(arr)

    area1 = deque()
    area2 = deque()
    area3 = deque()
    area4 = deque()

    for i in range(0, int(L/2)):
        area1.append(arr[i][:int(L/2)])
        area2.append(arr[i][int(L/2):])
    for i in range(int(L/2), L):
        area3.append(arr[i][:int(L/2)])
        area4.append(arr[i][int(L/2):])

    return [area1, area2, area3, area4]

N = int(sys.stdin.readline())

paper = []
white_paper = 0
blue_paper = 0

for i in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

queue = deque()
queue.append(paper)

while queue:
    target = queue.popleft()
    status = conquer(target)
    if status == 0: white_paper +=1
    elif status == 1: blue_paper += 1
    else:
        queue.extend(divide(target))

print(white_paper)
print(blue_paper)