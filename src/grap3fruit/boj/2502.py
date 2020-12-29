import sys
D, K = list(map(int, input().split()))
dp = [0]*(D+1)

dp[1] = 'a'
dp[2] = 'b'

idx = 3

while True:
    dp[idx] = dp[idx-2] + dp[idx-1]

    if idx == D:
        print(dp)
        break

    idx += 1

count_A = dp[D].count('a')
count_B = dp[D].count('b')

def calc(count_A, count_B):
    for i in range(1, K):
        for j in range(1, K):
            if (count_A * j + count_B * i) == K:
                print(j)
                print(i)
                return


calc(count_A, count_B)
