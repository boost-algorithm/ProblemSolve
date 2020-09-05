N = int(input())

inputString = input().split(' ')
numArr = []
queue = []
idx = 0

for i in range(N):
    numArr.append(str(i+1))

queue.append(numArr.pop(0))
inputString.pop(0)
idx = ((idx + int(inputString[idx])) + len(numArr)) % len(numArr)
print(idx)
while(len(numArr)!=0):
    popData = numArr.pop(idx)
    idx = ((idx + (int(inputString[idx])-1)) + len(numArr)) % len(numArr)
    inputString.pop(idx)
    queue.append(popData)

print('<'+', '.join(queue)+'>')


# 움직이는거 queue로 하면 될 듯했는데.. 졸려서 잤어요...