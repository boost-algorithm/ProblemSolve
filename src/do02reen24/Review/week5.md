# :fire: week5

## :ballot_box_with_check: 백준 1697

#### 메모리 초과

```python
import sys

n, k = map(int, sys.stdin.readline().split())

board = {}
board[n] = 0
queue = []
newQueue = []
count = 1
queue.append(n)
while queue:
    index = queue.pop()
    if board.get(index-1) == None:
        newQueue.append(index-1)
        board[index-1] = count
    if board.get(index+1) == None:
        newQueue.append(index+1)
        board[index+1] = count
    if board.get(index*2) == None:
        newQueue.append(index*2)
        board[index*2] = count
    if board.get(k):
        print(board[k])
        break
    if not queue:
        queue = newQueue
        newQueue = []
        count += 1
```

`dict` 자료구조를 사용하고 max 범위를 걸어주지 않아 생긴 에러인듯 하다.

#### 틀렸습니다.

```c++
#include <iostream>
#include <queue>

using namespace std;
const int MAX_RANGE = 2000000;
int visit[MAX_RANGE];

int main() {
    int n, k;
    cin >> n >> k;
    queue<int> q;
    queue<int> q2;
    visit[n] = -1;
    q.push(n);
    int count = 1;

    while (!q.empty()) {
        int index = q.front();
        q.pop();
        if (index - 1 >= 0) {
            if (visit[index - 1] == 0) {
                q2.push(index - 1);
                visit[index - 1] = count;
            }
        }
        if (index + 1 < MAX_RANGE) {
            if (visit[index + 1] == 0) {
                q2.push(index + 1);
                visit[index + 1] = count;
            }
        }
        if (index * 2 < MAX_RANGE) {
            if (visit[index * 2] == 0) {
                q2.push(index * 2);
                visit[index * 2] = count;
            }
        }
        if (visit[k] != 0) {
            cout << visit[k] << '\n';
            break;
        }
        if (q.empty()) {
            q = q2;
            q2 = queue<int>();
            count++;
        }
    }
    return 0;
}
```

## :ballot_box_with_check: 백준 2606

map 과 list를 활용하여 쉽게 풀었다.

## :ballot_box_with_check: 백준 7569

6가지 방향에 대해 검사를 해주고 예외 조건들을 확인하는 식으로 해결하였다.