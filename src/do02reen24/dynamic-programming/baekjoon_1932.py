import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    triangle = []
    best = []
    for i in range(n):
        triangle.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
        best.append([0] * (i+1))
    best[0][0] = triangle[0][0]
    for i in range(1, n):
        best[i][0] = triangle[i][0] + best[i-1][0]
        for k in range(1, i):
            best[i][k] = triangle[i][k] + max(best[i-1][k-1], best[i-1][k])
        best[i][i] = triangle[i][i] + best[i-1][i-1]
    print(max(best[n-1]))
