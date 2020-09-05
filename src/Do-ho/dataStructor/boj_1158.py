N, K = map(int, input().split())

numArr = []
queue = []
idx = 0

for i in range(N):
    numArr.append(str(i+1))

while(len(numArr)!=0):
    idx = (idx + (K-1)) % len(numArr)
    popData = numArr.pop(idx)
    queue.append(popData)

print('<'+', '.join(queue)+'>')