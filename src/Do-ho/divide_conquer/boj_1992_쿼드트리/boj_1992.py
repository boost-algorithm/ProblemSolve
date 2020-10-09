import sys
from collections import deque 

def conquer(arr):
    L = len(arr)
    A = L * L
    one = 0
    zero = 0

    if A==1: return arr[0][0]

    for i in range(L):
        for j in range(L):
            if arr[i][j] == '1': one += 1
            else: zero += 1
    
    if one==A: return '1'
    elif zero==A: return '0'
    else: return '-1'

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

def quad(arr):
    result = ""
    status = conquer(arr)

    if status == '0': result += "0"
    elif status == '1': result += "1"
    else:
        result += "("
        dividearr = divide(arr)
        for da in dividearr:
            result += quad(da)
        result += ")"
    return result

N = int(sys.stdin.readline())

video = []

for i in range(N):
    value = sys.stdin.readline()
    video.append(value)

sys.stdout.write(quad(video))