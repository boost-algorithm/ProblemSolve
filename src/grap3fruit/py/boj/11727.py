import sys

N = int(sys.stdin.readline())

dp = [0]*1002
dp[1] = 1
dp[2] = 3

index = 2
while True:
  if N == 1:
    print(dp[1])
    break

  if index == N:
    print(dp[N]%10007)
    break
  
  index += 1
  dp[index] = dp[index-1] + dp[index-2] + dp[index-2]
  