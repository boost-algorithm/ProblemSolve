# w[i] > j  D[i][j] = D[i-1][j]
# w[i] <= j D[i][j] = max(V[i] + D[i-1][j-w[i]] , D[i-1][j])

import sys

[N, K] = map(int, sys.stdin.readline().strip().split())

B = []
D = [[0 for _ in range(K)] for _ in range(N)]

for _ in range(N):
    B.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(N):
    if i==1:
        D[i][B[0][0]] = B[0][1]
        continue
    for j in range(K):
        