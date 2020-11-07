import sys

D = [[0 for _ in range(30)] for _ in range(30)]

def f(i, j):
    if j<i: return 0
    if i==1: return j
    if i==j: return 1
    return D[i][j-1] + D[i-1][j-1]

for i in range(30):
    for j in range(30):
        D[i][j] = f(i, j)

T = int(sys.stdin.readline())

for _ in range(T):
    [N, M] = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(D[N][M])+"\n")