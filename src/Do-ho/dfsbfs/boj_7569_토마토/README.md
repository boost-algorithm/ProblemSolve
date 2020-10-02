# 토마토

1. 입력 중에 0이 없으면 0 반환
2. 안익은 토마토에 대해서 돌면서 가장 가까운 1까지의 최단 경로 구하기
    - 만약 1을 못찾으면 1반환
    - 최단 경로 중 방문했던 곳은 방문 인해도 됨. (아마도..?)
    - 결국 최단 경로가 가장 큰 것이 답이 될듯

- 1번째풀이 [시간 초과]
```python
import sys

directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

[M, N, H] = map(int, sys.stdin.readline()[:-1].split(' '))

tomato = []

for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int, sys.stdin.readline()[:-1].split(' '))))
    tomato.append(tmp)

def function():
    underripeTomatos = []
    isAllRipeTomatos = True

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k] == 0:
                    underripeTomatos.append((i, j, k))
                    isAllRipeTomatos = False

    if isAllRipeTomatos: return 0

    days = 0 # 아무 값

    while(len(underripeTomatos)!=0):
        visited = []
        target = underripeTomatos.pop(0)
        if target not in visited:
            tmp = isExistGoodTomato(target, visited)
            if tmp == 0: return -1
            if days <= tmp: days = tmp
            
    return days

def isExistGoodTomato(underripeTomato, parentvisited):
    visited = []
    queue = [(underripeTomato, 1)]
    while len(queue) != 0:
        tmp = queue.pop(0)
        target = tmp[0]
        count = tmp[1]
        if target not in visited:
            visited.append(target)
            for direction in directions:
                x = target[2] + direction[2]
                y = target[1] + direction[1]
                z = target[0] + direction[0]

                if x<0 or y<0 or z<0 or x>=M or y>=N or z>=H: continue
                elif tomato[z][y][x] == 1: return count
                elif tomato[z][y][x] == -1: continue
                else:
                    if (x, y, z) not in parentvisited: parentvisited.append((x, y, z))
                    queue.append(((z, y, x), count + 1))
    return 0

print(function())
```

- 2번째풀이 [시간 초과]
  - 느낌 상 visited에 대한 탐색 비용이 많이 들어서 그런 것 같아서 배열 마킹 방법으로 변경

```python
import sys

directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

[M, N, H] = map(int, sys.stdin.readline()[:-1].split(' '))

tomato = []

for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int, sys.stdin.readline()[:-1].split(' '))))
    tomato.append(tmp)

def function():
    underripeTomatos = []
    isAllRipeTomatos = True

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k] == 0:
                    underripeTomatos.append((i, j, k))
                    isAllRipeTomatos = False

    if isAllRipeTomatos: return 0

    days = 0 # 아무 값

    while(len(underripeTomatos)!=0):
        visited = [[[False for i in range(M)] for i in range(N)] for i in range(H)]
        target = underripeTomatos.pop(0)
        if not visited[target[0]][target[1]][target[2]]:
            tmp = isExistGoodTomato(target, visited)
            if tmp == 0: return -1
            if days <= tmp: days = tmp
            
    return days

def isExistGoodTomato(underripeTomato, parentvisited):
    visited = [[[False for i in range(M)] for i in range(N)] for i in range(H)]
    queue = [(underripeTomato, 1)]
    while len(queue) != 0:
        tmp = queue.pop(0)
        target = tmp[0]
        count = tmp[1]
        if not visited[target[0]][target[1]][target[2]]:
            visited[target[0]][target[1]][target[2]] = True
            for direction in directions:
                x = target[2] + direction[2]
                y = target[1] + direction[1]
                z = target[0] + direction[0]

                if x<0 or y<0 or z<0 or x>=M or y>=N or z>=H: continue
                elif tomato[z][y][x] == 1: return count
                elif tomato[z][y][x] == -1: continue
                else:
                    if not parentvisited[z][y][x]: parentvisited[z][y][x] = True
                    queue.append(((z, y, x), count + 1))
    return 0

print(function())
```

- 3번째풀이 [시간 초과]
  - 그래도 같아서.. 뭐가 문제지... ㅠㅠㅠ
  - pop(0)의 비용은 얼마일까 보니 O(n) 그래서 나온 것이 ```deque.popleft()```

```python
import sys
from collections import deque

directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

[M, N, H] = map(int, sys.stdin.readline()[:-1].split(' '))

tomato = []

for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int, sys.stdin.readline()[:-1].split(' '))))
    tomato.append(tmp)

def function():
    underripeTomatos = deque()
    isAllRipeTomatos = True

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k] == 0:
                    underripeTomatos.append((i, j, k))
                    isAllRipeTomatos = False

    if isAllRipeTomatos: return 0

    days = 0 # 아무 값

    while(len(underripeTomatos)!=0):
        visited = [[[False for i in range(M)] for i in range(N)] for i in range(H)]
        target = underripeTomatos.popleft()
        if not visited[target[0]][target[1]][target[2]]:
            tmp = isExistGoodTomato(target, visited)
            if tmp == 0: return -1
            if days <= tmp: days = tmp
            
    return days

def isExistGoodTomato(underripeTomato, parentvisited):
    visited = [[[False for i in range(M)] for i in range(N)] for i in range(H)]
    queue = deque()
    queue.append((underripeTomato, 1))
    
    while len(queue) != 0:
        tmp = queue.popleft()
        target = tmp[0]
        count = tmp[1]
        if not visited[target[0]][target[1]][target[2]]:
            visited[target[0]][target[1]][target[2]] = True
            for direction in directions:
                x = target[2] + direction[2]
                y = target[1] + direction[1]
                z = target[0] + direction[0]

                if x<0 or y<0 or z<0 or x>=M or y>=N or z>=H: continue
                elif tomato[z][y][x] == 1: return count
                elif tomato[z][y][x] == -1: continue
                else:
                    if not parentvisited[z][y][x]: parentvisited[z][y][x] = True
                    queue.append(((z, y, x), count + 1))
    return 0

print(function())
```

- 4번째 풀이 [성공 ㅠㅠ]

  - 알고리즘의 변화
  - 그냥 익혀보자 안익은거 찾지말아보자
  - 위의 복잡도가 은근 큰 것 같다....

  ```python
  import sys
  from collections import deque
  
  directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
  
  [M, N, H] = map(int, sys.stdin.readline().split())
  
  tomato = []
  
  for i in range(H):
      tmp = []
      for j in range(N):
          tmp.append(list(map(int, sys.stdin.readline().split())))
      tomato.append(tmp)
  
  def function():
      ripeTomatos = deque()
      visited = [[[False for i in range(M)] for i in range(N)] for i in range(H)]
  
      for i in range(H):
          for j in range(N):
              for k in range(M):
                  if tomato[i][j][k] == 1:
                      ripeTomatos.append((i, j, k, 0))
  
      day = 0
  
      while ripeTomatos:
          z, y, x, day = ripeTomatos.popleft()
          if tomato[z][y][x]==0: tomato[z][y][x] = 1
          for dx, dy, dz in directions:
              nx, ny, nz = x+dx, y+dy, z+dz
              if nx<0 or ny<0 or nz<0 or nx>=M or ny>=N or nz>=H: continue
              if tomato[nz][ny][nx] == 0:
                  if not visited[nz][ny][nx]:
                      ripeTomatos.append((nz, ny, nx, day+1))
                      visited[nz][ny][nx] = True
      
      for i in range(H):
          for j in range(N):
              for k in range(M):
                  if tomato[i][j][k] == 0:
                      return -1
                      
      return day
  
  sys.stdout.write(str(function()))
  ```



위에서 리팩토링을 많이 했는데 다음 게시물을 참고함 [[참고](https://www.acmicpc.net/blog/view/70)]