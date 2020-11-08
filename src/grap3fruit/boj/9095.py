import sys

T = int(sys.stdin.readline())
N_list = []
for _ in range(T):
  N_list.append(int(sys.stdin.readline()))

dp = [0]*11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for N in N_list:
  if N <= 3:
    print(dp[N])
    continue
  
  index = 4
  while True:
    dp[index] = dp[index-1] + dp[index-2] + dp[index-3]
    if index == N:
      print(dp[index])
      break 
    
    index += 1