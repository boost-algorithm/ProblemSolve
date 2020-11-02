import sys
from math import factorial

def combination(n, c):
    return int(factorial(n) / (factorial(n-c) * factorial(c)))

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split(' '))
        ans = combination(m,n)
        print(ans)
