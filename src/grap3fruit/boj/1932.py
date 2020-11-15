import sys
import itertools
N = int(sys.stdin.readline())

data = []
for _ in range(N):
  data.append(list(map(int,sys.stdin.readline().strip().split())))

print("data:",data)

def chain(*iterables): # 참조 : https://winterj.me/list_of_lists_to_flatten/
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element

a = list(itertools.chain(*data))
print("a:",a)

def calc(data, a):

  dp = [0]*501
  dp[0] = a[0]

  if N == 1:
    return (dp[0])
    

  dp[1] = a[0] + a[1]
  dp[2] = a[0] + a[2]

  if N == 2:
    return max(dp[1], dp[2])

  a_index = 0

  for i, row in enumerate(data) :
    print(i)
    if i == 0:
      continue

    for j, el in enumerate(row):
      a_index += 1
      if j == 0 :
        dp[a_index] = dp[a_index-i] + a[a_index]
        continue

      if j == len(row)-1:
        dp[a_index] = dp[a_index-i-1] + a[a_index]
        continue

      dp[a_index] = max(dp[a_index-i-1] + a[a_index], dp[a_index-i]+a[a_index])
      
  return(max(dp))
      
print(calc(data ,a))