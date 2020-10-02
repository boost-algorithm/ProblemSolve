# :fire: week3

## :ballot_box_with_check: 백준 1316

map을 활용하여 쉽게 풀었다.

## :ballot_box_with_check: 프로그래머스 60057

문자열 길이 / 2 만큼 반복문을 돌면서 가장 짧을 때를 찾아주었는데 어떻게 하면 더 효율을 높일 수 있을지 고민해보면 좋을 것 같다.

## :ballot_box_with_check: 프로그래머스 ​17685

#### 시간초과 (18/22)

```python
def solution(words):
    answer = 0
    searchDict = {}
    for word in words:
        for i in range(len(word)):
            w = word[:i+1]
            if searchDict.get(w):
                searchDict[w] += 1
            else:
                searchDict[w] = 1

    for word in words:
        length = len(word)
        for i in range(length):
            if i+1 == length:
                answer += length
                break
            w = word[:i+1]
            if searchDict[w] == 1:
                answer += i+1
                break
    return answer
```

#### 시간초과(18/22)

``` python
def solution(words):
    answer = 0
    searchDict = {}
    for word in words:
        for i in range(len(word)):
            w = word[:i+1]
            if searchDict.get(w):
                searchDict[w] += 1
            else:
                searchDict[w] = 1

    for word in words: // 1
        length = len(word)
        minAnswer = searchDict[word]
        ans = length
        for i in range(length - 2, -1, -1):
            w = word[:i+1]
            if minAnswer == 1 and searchDict[w] == minAnswer:
                ans = i + 1
            elif searchDict[w] < minAnswer:
                minAnswer = searchDict[w]
                ans = i + 1
            else:
                break
        answer += ans
    return answer
```

1번 제출때와 다르게 뒤에서부터 검사하면 시간을 줄일 수 있지 않을까 했는데 똑같은 경우에서 시간초과가 발생했다. 로직 자체를 다른 방향으로 접근해야하는 것 같다.

# :fire: 추가문제

## :ballot_box_with_check: 백준 9012

`brackets = sys.stdin.readline().rstrip()` 에서 rstrip을 꼭 해줘야 했다. 안해줄 경우 공백도 stack에 들어가 연산이 1회 더 수행됐다.

## :ballot_box_with_check: 백준 1874

#### 틀렸습니다.

```python
import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline())
    stack = []
    number = 1
    result = []
    for _ in range(t):
        n = int(sys.stdin.readline())
        while True:
            if number > t:
                print("NO")
                sys.exit(1) 
            if not stack:
                stack.append(number)
            else:
                top = stack[-1]
                if top < n:
                    number += 1
                    stack.append(number)
                else:
                    stack.pop()
                    result.append('-')
                    if top == n:
                        break
                    continue
            result.append('+')
    for r in result:
        print(r)
```

백준 사이트에서는  `sys.exit(0)` 을 써야 오류로 간주되지 않는다고 한다. 나는 `sys.exit(1)` 을 썼다. 새로 제출한 코드는 알고리즘을 바꾸긴 했으나 전체 동작이 동일하므로 아마 exit 함수 때문에 첫번째 시도 때 틀린 것 같다.

## :ballot_box_with_check: 백준 10799

`for i in range(0, len(brackets)):` 의 중간에서 i += 1이 안먹었다. 해결책을 몰라 일단 해당 경우를 skip하는 형태로 코드를 변경하여 제출하였다. python 문법을 좀 더 찾아봐야겠다.