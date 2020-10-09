import sys
from collections import deque 

def conquer(arr):
    L = len(arr)
    A = L * L

    if A==1: return arr[0][0]

    check = arr[0][0]

    for i in range(L):
        for j in range(L):
            if arr[i][j] != check: return "-2"
    
    return check

def divide(arr):
    L = len(arr)

    area = [deque() for i in range(9)]
    k = int(L/3)

    for i in range(0, k):
        area[0].append(arr[i][:k])
        area[1].append(arr[i][k:2*k])
        area[2].append(arr[i][2*k:])
    for i in range(k, 2*k):
        area[3].append(arr[i][:k])
        area[4].append(arr[i][k:2*k])
        area[5].append(arr[i][2*k:])
    for i in range(2*k, L):
        area[6].append(arr[i][:k])
        area[7].append(arr[i][k:2*k])
        area[8].append(arr[i][2*k:])

    return area

def f(arr):
    minus_one_paper = 0
    zero_paper = 0
    one_paper = 0

    status = conquer(arr)
    if status == '0': zero_paper +=1
    elif status == '1': one_paper += 1
    elif status == '-1': minus_one_paper += 1
    else:
        dividearr = divide(arr)
        for da in dividearr:
            result = f(da)
            minus_one_paper += result[0]
            zero_paper += result[1]
            one_paper += result[2]
    
    return [minus_one_paper, zero_paper, one_paper]

N = int(sys.stdin.readline())

paper = []

for i in range(N):
    paper.append(sys.stdin.readline().split())

papernum = f(paper)

sys.stdout.write(str(papernum[0])+'\n')
sys.stdout.write(str(papernum[1])+'\n')
sys.stdout.write(str(papernum[2])+'\n')