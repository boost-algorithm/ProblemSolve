import sys

n = int(sys.stdin.readline())

D = [0 for _ in range(n+2)]
D[1] = 1
D[2] = 3

for i in range(3, n+1):
    D[i] = D[i-1] + 2*D[i-2]

print(D[n]%10007)