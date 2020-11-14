import sys

n = int(sys.stdin.readline())

D = [[0 for _ in range(n)] for _ in range(n)]

def f(idx):
    return 0

triangle = []

for i in range(n):
    triangle.append(list(map(int, sys.stdin.readline().strip().split())))

D[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(i+1):
        try: D[i][j] = triangle[i][j] + max(D[i-1][j-1], D[i-1][j])
        except: D[i][j] = triangle[i][j] + D[i-1][j]
        
print(max(D[n-1]))