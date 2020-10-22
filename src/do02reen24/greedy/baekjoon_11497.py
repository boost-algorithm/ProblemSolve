import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        log = list(map(int, sys.stdin.readline().split(' ')))
        log.sort()
        level = log[1] - log[0]
        lastLevel = log[n-1] - log[n-2]
        if lastLevel > level: level = lastLevel
        for i in range(0, n - 2):
            tempLevel = log[i+2] - log[i]
            if tempLevel > level: level = tempLevel
        print(level)