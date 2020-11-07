import sys

T = int(sys.stdin.readline())
D = [[0, 0, 0] for _ in range(T)]
S = []

for _ in range(T):
    S.append(list(map(int, sys.stdin.readline().split())))

D[0] = S[0]

for i in range(1, T):
    D[i][0] = S[i][0] + min(D[i-1][1], D[i-1][2])
    D[i][1] = S[i][1] + min(D[i-1][0], D[i-1][2])
    D[i][2] = S[i][2] + min(D[i-1][0], D[i-1][1])

sys.stdout.write(str(min(D[T-1])))