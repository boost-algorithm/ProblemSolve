import sys

T = int(sys.stdin.readline())
S = [0 for _ in range(T)]
D = [0 for _ in range(T)]

for i in range(T):
    S[i] = int(sys.stdin.readline())

D[0] = S[0]
if T>1: D[1] = S[1] + D[0]
if T>2: D[2] = max(S[0]+S[2], S[1]+S[2])

for i in range(3, T):
    D[i] = max(S[i] + S[i-1] + D[i-3], S[i] + D[i-2])

print(D[T-1])