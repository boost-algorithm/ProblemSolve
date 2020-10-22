import sys

def diff(a, b):
    return a-b

[N, K] = map(int, sys.stdin.readline().split())

coinKinds = []

for _ in range(N):
    coinKinds.append(int(sys.stdin.readline()))

coinKinds.sort()

count = 0
while K!=0:
    mindiff = diff(K, coinKinds[0])
    minIdx = 0
    for idx, coinKind in enumerate(coinKinds):
        value = diff(K, coinKind)
        if value < 0: break
        if mindiff > value:
            mindiff = value
            minIdx = idx
    count += K//coinKinds[minIdx]
    K -= coinKinds[minIdx] * (K//coinKinds[minIdx])
    

print(count)