import sys

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split(' '))
    coin = []
    ans = 0
    for _ in range(n):
        coin.append(int(sys.stdin.readline()))
    while coin:
        money = coin.pop()
        quotient = int(k / money)
        k -= quotient * money
        ans += quotient
    print(ans)