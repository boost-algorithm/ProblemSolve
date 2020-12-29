import sys
sys.setrecursionlimit(300000)

def findSum(count, n):
    ans = 0
    for i in range(1, 4):
        if count == n:
            ans += 1
            break
        elif count > n:
            return 0
        ans += findSum(count + i, n)
    return ans

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        print(findSum(0, n))