# :fire: week2

## :ballot_box_with_check: 백준 11286
#### 틀렸습니다.

```python
import sys

class Num(object):
    def __init__(self, n):
        self.positive = 0
        self.negative = 0

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    absStack = {}
    min = -1
    for i in range(n):
        command = int(sys.stdin.readline())
        if command == 0:
            if min == -1:
                print(0)
                continue
            if absStack[min].negative > 0:
                print('-'+str(min))
                absStack[min].negative -= 1
            else:
                print(min)
                absStack[min].positive -= 1
            if absStack[min].negative < 1 and absStack[min].positive < 1:
                del absStack[min]
                if len(absStack) == 0:
                    min = -1
                    continue
                for key in absStack.keys():
                    min = key
                    break
        else:
            absValue = abs(command)
            if not absValue in absStack:
                absStack[absValue] = Num(absValue)
            if command < 0:
                absStack[absValue].negative += 1
            else:
                absStack[absValue].positive += 1
            if absValue < min or min < 0:
                min = absValue
```
틀린 이유 key가 순서대로 저장된다고 생각하여 진행하였는데 생각해보니까 삽입 순이기 때문에 고쳐줄 필요가 있었다.

```python
for key in absStack.keys():
    min = key
    break
```

`Num` 클래스를 만들어서 진행했는데 굳이 필요없을 것 같아 제거 후 코딩을 진행하였다.

#### 시간초과

```python
import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    absStack = {}
    minValue = -1
    for i in range(n):
        command = int(sys.stdin.readline())
        if command == 0:
            if minValue == -1:
                print(0)
                continue

            index = minValue * -1
            if not index in absStack:
                index = minValue
            absStack[index] -= 1
            print(abs(index))
            if absStack[index] < 1:
                del absStack[index]
                if len(absStack) == 0:
                    minValue = -1
                    continue
                minValue = abs(min(list(absStack.keys()), key=abs))
        else:
            if not command in absStack:
                absStack[command] = 1
            else:
                absStack[command] += 1
            if abs(command) < minValue or minValue < 0:
                minValue = abs(command)
```
시간초과가 발생했는데 아마도 `if not index in absStack` 또는 `minValue = abs(min(list(absStack.keys()), key=abs))` 이런 식으로 값을 찾는 부분 때문인 것 같다.

#### + 두번째 시간초과

프로그래머스 위장문제를 풀고 `if not command in absStack:` 을 `if absStack.get(command) == None:` 으로 고쳤으나 결과가 달라지지 않았다.

#### 맞았습니다.

문제를 잘못이해해서 heap을 구현하지 않았음을 깨달았다. python에 `heapq` 라는 자료구조가 있음을 알게 되었고 이를 이용해서 문제를 풀었다.

## :ballot_box_with_check: 프로그래머스 위장

쉽게 풀 수 있었다. dict 객체에서 `dict.get(key)` 를 통해 해당 키가 있는지 검사할 수 있음을 알게 되었다.

```python
if clothesMap.get(c[1]) == None:
    clothesMap[c[1]] = []
clothesMap[c[1]].append(c[0])
```

이런 식으로 key를 검사하도록 코드를 작성하였다.

## :ballot_box_with_check: 백준 1991

python은 `end`를 통해 print문의 끝을 지정해줄 수 있다. `print(index, end='')` 를 통해 결과를 한 줄에 출력하도록 했다. (기본 값 `\n` )

## :ballot_box_with_check: 백준 2957(1주차 연장)