import sys

T = int(sys.stdin.readline())

D = [0 for _ in range(12)]
D[1] = 1
D[2] = 2
D[3] = 4

for i in range(4, 12):
    D[i] = D[i-3] + D[i-2] + D[i-1]

for _ in range(T):
    n = int(sys.stdin.readline())
    sys.stdout.write(str(D[n])+'\n')