import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    res = [1 , 1]
    for i in range(2, n + 1):
        res.append(res[i-1] + res[i-2] + res[i-2])
        res[i] = int(res[i] % 10007)
    print(res[n])