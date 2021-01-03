import sys

N, K = list(map(int,sys.stdin.readline().strip().split()))

coins = []
for i in range(N):
  coins.append(int(sys.stdin.readline()))

coins.sort(reverse=True)
print(coins)

count = 0
for coin in coins:
  value = int(K/coin)
  
  if value >= 1:
    count += value
    K = K-(value*coin)

print(count)