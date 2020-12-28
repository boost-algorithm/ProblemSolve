# :fire: week12

## :ballot_box_with_check: 백준 2011

#### 틀렸습니다 (35%)

```python
import sys

def decodeNum():
    word = sys.stdin.readline().rstrip()
    length = len(word)

    sol = [1] * (length + 1)
    for i in range(1, length):
        prev = int(word[i-1]+word[i])
        now = int(word[i])
        if prev == 10 or prev == 20:
            sol[i+1] = sol[i-1]
        elif 11 <= prev and prev <= 26:
            sol[i+1] = (sol[i] % 1000000) + (sol[i-1] % 1000000)
        elif 1 <= now and now <= 9:
            sol[i+1] = sol[i]
        else: return 0
    return sol[length] % 1000000

print(int(decodeNum()))
```

- 숫자가 0인 경우를 예외처리해주고 1000000으로 나누는 부분을 수정함

## :ballot_box_with_check: 백준 2178

- 초기에 `visited = [[-1] * m] * n` 와 같이 초기화를 했더니 2차원 배열이 같은 값들을 참조하여 동시에 값이 변경되는 문제가 있었다. `visited = [[-1 for _ in range(m)] for _ in range(n)]`와 같이 초기화하여 해결할 수 있었다.

#### 런타임에러(72%)

```python
import sys

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(visit):
    new_visit = []
    while visit:
        x, y = visit.pop()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if mx >= 0 and mx < n and my >=0 and my < m:
                if visited[mx][my] != -1 or board[mx][my] == "0": continue
                visited[mx][my] = visited[x][y] + 1
                new_visit.append((mx, my))
    if len(new_visit) > 0: bfs(new_visit)

n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(sys.stdin.readline().rstrip())
visited = [[-1 for _ in range(m)] for _ in range(n)]
visited[0][0] = 1
bfs([(0,0)])
print(visited[n-1][m-1])
```

- 파이썬은 재귀호출 깊이에 제한이 있는데 이를 풀어주지 않아 생긴 문제 같았다.
- 좀 더 생각해보니 재귀호출을 사용하지 않고 문제를 해결할 수 있을 것 같아 코드를 수정하여 문제를 해결하였다.

## :ballot_box_with_check: 백준 20422

-

## :ballot_box_with_check: 백준 2644

-
