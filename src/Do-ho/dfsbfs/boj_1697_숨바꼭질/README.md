# 숨바꼭질

##### 1. 재귀를 통한 풀이

```python
import sys

maxCount = 100001

def search(start, end, count):
    global maxCount
    if(count>=maxCount):
        return
    if start==end:
        if maxCount>=count:
            maxCount = count
        return
    elif (end*2)<=start:
        return
    elif start<=-1:
        return
    else:
        if start==0:
            search(start+1, end, count+1)
        if start < end:
            search(start*2, end, count+1)
            search(start+1, end, count+1)
            search(start-1, end, count+1)
        else:
            count += end-start
            return

[N, K] = map(int, sys.stdin.readline()[:-1].split(' '))
search(N, K, 0)

print(maxCount)
```
- 해당 풀이는 재귀의 호출이 너무 많아 런타임이 나옴



##### 2. bfs를 통한 풀이

```python
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
```

- bfs를 통해 가장 먼저 찾아지는 카운트를 활용