# 종이의 개수

- 첫 번째 시도 (메모리 초과)
```python
import sys
from collections import deque 

def conquer(arr):
    L = len(arr)
    A = L * L
    minus_one = 0
    zero = 0
    one = 0

    if A==1: return arr[0][0]

    for i in range(L):
        for j in range(L):
            if arr[i][j] == -1: minus_one += 1
            elif arr[i][j] == 0: zero += 1
            else: one += 1
    
    if minus_one==A: return -1
    elif zero==A: return 0
    elif one==A: return 1
    else: return 2

def divide(arr):
    L = len(arr)

    area = [deque() for i in range(9)]
    k = int(L/3)

    for i in range(0, k):
        area[0].append(arr[i][:k])
        area[1].append(arr[i][k:2*k])
        area[2].append(arr[i][2*k:])
    for i in range(k, 2*k):
        area[3].append(arr[i][:k])
        area[4].append(arr[i][k:2*k])
        area[5].append(arr[i][2*k:])
    for i in range(2*k, L):
        area[6].append(arr[i][:k])
        area[7].append(arr[i][k:2*k])
        area[8].append(arr[i][2*k:])

    return area

N = int(sys.stdin.readline())

paper = []
minus_one_paper = 0
one_paper = 0
zero_paper = 0

for i in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

queue = deque()
queue.append(paper)

while queue:
    target = queue.popleft()
    status = conquer(target)
    if status == 0: zero_paper +=1
    elif status == 1: one_paper += 1
    elif status == -1: minus_one_paper += 1
    else:
        queue.extend(divide(target))

sys.stdout.write(str(minus_one_paper)+'\n')
sys.stdout.write(str(zero_paper)+'\n')
sys.stdout.write(str(one_paper)+'\n')
```

- 두 번째 시도(시간초과)
```python
import sys
from collections import deque 

def conquer(arr):
    L = len(arr)
    A = L * L
    minus_one = 0
    zero = 0
    one = 0

    if A==1: return arr[0][0]

    for i in range(L):
        for j in range(L):
            if arr[i][j] == '-1': minus_one += 1
            elif arr[i][j] == '0': zero += 1
            else: one += 1
    
    if minus_one==A: return '-1'
    elif zero==A: return '0'
    elif one==A: return '1'
    else: return '2'

def divide(arr):
    L = len(arr)

    area = [deque() for i in range(9)]
    k = int(L/3)

    for i in range(0, k):
        area[0].append(arr[i][:k])
        area[1].append(arr[i][k:2*k])
        area[2].append(arr[i][2*k:])
    for i in range(k, 2*k):
        area[3].append(arr[i][:k])
        area[4].append(arr[i][k:2*k])
        area[5].append(arr[i][2*k:])
    for i in range(2*k, L):
        area[6].append(arr[i][:k])
        area[7].append(arr[i][k:2*k])
        area[8].append(arr[i][2*k:])

    return area

def f(arr):
    minus_one_paper = 0
    zero_paper = 0
    one_paper = 0

    status = conquer(arr)
    if status == '0': zero_paper +=1
    elif status == '1': one_paper += 1
    elif status == '-1': minus_one_paper += 1
    else:
        dividearr = divide(arr)
        for da in dividearr:
            result = f(da)
            minus_one_paper += result[0]
            zero_paper += result[1]
            one_paper += result[2]
    
    return [minus_one_paper, zero_paper, one_paper]

N = int(sys.stdin.readline())

paper = []

for i in range(N):
    paper.append(sys.stdin.readline().split())

papernum = f(paper)

sys.stdout.write(str(papernum[0])+'\n')
sys.stdout.write(str(papernum[1])+'\n')
sys.stdout.write(str(papernum[2])+'\n')
```

- 세 번째 시도(성공)
```python
import sys
from collections import deque 

def conquer(arr):
    L = len(arr)
    A = L * L

    if A==1: return arr[0][0]

    check = arr[0][0]

    for i in range(L):
        for j in range(L):
            if arr[i][j] != check: return "-2"
    
    return check

def divide(arr):
    L = len(arr)

    area = [deque() for i in range(9)]
    k = int(L/3)

    for i in range(0, k):
        area[0].append(arr[i][:k])
        area[1].append(arr[i][k:2*k])
        area[2].append(arr[i][2*k:])
    for i in range(k, 2*k):
        area[3].append(arr[i][:k])
        area[4].append(arr[i][k:2*k])
        area[5].append(arr[i][2*k:])
    for i in range(2*k, L):
        area[6].append(arr[i][:k])
        area[7].append(arr[i][k:2*k])
        area[8].append(arr[i][2*k:])

    return area

def f(arr):
    minus_one_paper = 0
    zero_paper = 0
    one_paper = 0

    status = conquer(arr)
    if status == '0': zero_paper +=1
    elif status == '1': one_paper += 1
    elif status == '-1': minus_one_paper += 1
    else:
        dividearr = divide(arr)
        for da in dividearr:
            result = f(da)
            minus_one_paper += result[0]
            zero_paper += result[1]
            one_paper += result[2]
    
    return [minus_one_paper, zero_paper, one_paper]

N = int(sys.stdin.readline())

paper = []

for i in range(N):
    paper.append(sys.stdin.readline().split())

papernum = f(paper)

sys.stdout.write(str(papernum[0])+'\n')
sys.stdout.write(str(papernum[1])+'\n')
sys.stdout.write(str(papernum[2])+'\n')
```