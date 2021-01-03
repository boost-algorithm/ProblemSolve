import sys

N = int(sys.stdin.readline())

score_list = []
for _ in range(N):
  score_list.append(int(sys.stdin.readline()))

def get_dp_3(a,b,c,d):
  max = a+b+d
  if a+c+d > max:
    max = a+c+d
  
  if b+c > max:
    max = b+c
  
  return max

def get_max(a,b):
  if a>b:
    return a

  return b

def calc(score_list):
  dp = [0]*301
  dp[0] = score_list[0]
  if N==1 :
    print(dp[0])
    return

  dp[1] = score_list[1] + score_list[0]
  if N==2 :
    print(dp[1])
    return 

  dp[2] = get_max(score_list[0],score_list[1]) + score_list[2]
  if N==3 :
    print(dp[2])
    return

  dp[3] = get_dp_3(score_list[0],score_list[1],score_list[2],score_list[3])
  if N==4 :
    print(dp[3])
    return

  print(dp[0],dp[1],dp[2],dp[3])
  for i in range(4, N):
    dp[i] = get_max(dp[i-2], dp[i-3]+score_list[i-1])+score_list[i]
    print(i, dp[i])
  print(dp[len(score_list)-1])
  return

calc(score_list)