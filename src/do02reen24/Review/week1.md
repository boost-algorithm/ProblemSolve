# :fire: week1

## :ballot_box_with_check: 백준 1158

파이썬으로 알고리즘을 (거의 처음)준비하면서 입력을 받는 것부터 찾아보았다. `input()` 이라는 기능이 있긴 하지만 `sys.stdin.readline()` 을 쓰는 것이 좋다고 한다.

## :ballot_box_with_check: 백준 1406

런타임 에러 →  해결

#### 런타임 오류가 발생했던 코드

```python
import sys

if __name__ == '__main__':
    string = list(sys.stdin.readline().rstrip())
    cursor = len(string)
    
    n = int(sys.stdin.readline().rstrip())
    for i in range(0, n):
        command = list(sys.stdin.readline().split())
        if command[0] == 'L' and cursor != 0:
            cursor -= 1
        elif command[0] == 'D' and cursor != len(string):
            cursor += 1
        elif command[0] == 'B' and cursor != 0:
            string.pop(cursor - 1)
        elif command[0] == 'P':
            string.insert(cursor, command[1])
            cursor += 1

    print(''.join(string))
```

처음엔 돌아만 가면 된다고 생각해서 효율을 고려하지 못한 것 같다. 아래 링크에서 힌트를 얻어 문제를 해결할 수 있었다.

[https://www.acmicpc.net/board/view/54572﻿](https://www.acmicpc.net/board/view/54572)

`linked list`를 만들어 해결하려햇으나 코드가 너무 복잡하고 길어지는 것 같아, `stack `2개를 활용하여 문제를 해결할 수 있었다.

## :ballot_box_with_check: 백준 2346

1158번과 비슷하여 쉽게 풀었다.

## :ballot_box_with_check: 백준 2957

런타임 에러 → 시간초과 → 메모리 초과

### 런타임 에러

```python
import sys

class Node(object):
    def __init__(self, n):
        self.n = n
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, n, node):
        if self.root == None:
            self.root = Node(n)
        else:
            self.count += 1
            if node.n < n:
                if node.left == None:
                    newNode = Node(n)
                    node.left = newNode           
                else:
                    self.insert(n, node.left)
            else:
                if node.right == None:
                    newNode = Node(n)
                    node.right = newNode  
                else:
                    self.insert(n, node.right)
        return self.root, self.count

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    bst = BinarySearchTree()
    node = None

    for i in range(0, N):
        n = int(sys.stdin.readline().rstrip())
        node, count = bst.insert(n, node)
        print(count)
```

파이썬은 재귀 호출에 한계가 있다고 한다. 따라서 재귀 호출이 많이 된다면 이를 늘려줄 필요가 있다.

```python
import sys
sys.setrecursionlimit(300000)
```

위 코드를 추가하여 런타임 에러를 해결 할 수 있었다.

### 시간 초과

런타임 에러를 해결했더니 시간 초과가 발생했다. `python`의 컴파일이 오래걸리기 때문인 경우가 많다고 한다. `pypy3`를 쓰면 빠르게 컴파일 된다고 하여 `pypy3`로 다시 제출해봤다.

### 메모리 초과

`pypy3`로 제출하니까 메모리 초과가 발생했다. 알고리즘 자체에 문제가 있다고 판단해서 코드를 고치기로 했다. 문제의 설명을 그대로 구현하면 `O(n^2)`이라고 한다.



## :pencil2: 고찰

### 잘했던 것, 좋았던 것, 도전 해볼 점, 계속할 것

* 블로그에 찾아봤던 내용을 정리하는 것은 잘한 것 같다. 다 기억할 수 없기 때문에 정리해놓고 찾아보면 좋을 것 같다. 앞으로도 계속 쓸 계획이다.
* 하루에 문제를 몰아서 풀지 않고 나눠서 풀었다. (물론 해결을 못한 것도 있지만...)

### 잘못했던 것, 아쉬운 것, 부족한 것, 개선방향

* 언어의 동작 원리를 꼼꼼하게 알아보고 사용할 필요가 있는 것 같다. 이전까지는 c++을 사용해서 알고리즘을 풀었었는데 python에서는 동작원리가 달라 논리가 비슷함에도 불구하고 에러가 발생하는 경우가 있었다.
* python으로 입력받는 부분이 낯설어 보고 따라치고 있는데 외우기 위한 노력을 해야 할 것 같다.
* 전 날 친구들과 약속에서 너무 신나게 노는 바람에 늦게 일어나 참여를 못했다. 첫 날의 실수를 만회하기 위해서라도 앞으로는 더욱 열심히 참여해야겠다.

### 기타

* python이 논리를 바로바로 생각하기 쉬워서 좋긴 하나 아직은 c++이 더 익숙한 것 같다. python으로 좀 더 진행해보고 어떤 언어로 코딩테스트를 준비할지 결정해야겠다.