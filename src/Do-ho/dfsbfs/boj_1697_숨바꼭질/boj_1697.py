import sys

checkList = [False for i in range(100001)]

def search(start, end):
    global checkList

    queue = [(start, 0)]

    while len(queue)!=0:
        target = queue.pop(0)
        if target[0] > 100000 or target[0] < 0: continue
        if checkList[target[0]]: continue

        checkList[target[0]] = True

        if target[0] == end:
            print(target[1])
            break

        queue.append((target[0]*2, target[1] + 1))
        queue.append((target[0]-1, target[1] + 1))
        queue.append((target[0]+1, target[1] + 1))

[N, K] = map(int, sys.stdin.readline()[:-1].split(' '))

search(N, K)