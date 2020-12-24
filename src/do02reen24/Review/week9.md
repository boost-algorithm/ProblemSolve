# :fire: week9

주제 : Dynamic programming

## :ballot_box_with_check: 백준 9095

- python으로 쉽게 풀 수 있었다. 이전에 작성했던 c++코드를 보니 아래와 같이 푸는 방법도 있었다.

```c++
#include <stdio.h>
int d[11];
int main() {
    d[0] = 1;
    for (int i=1; i<=10; i++) {
        if (i-1 >= 0) {
            d[i] += d[i-1];
        }
        if (i-2 >= 0) {
            d[i] += d[i-2];
        }
        if (i-3 >= 0) {
            d[i] += d[i-3];
        }
    }
    int t;
    scanf("%d",&t);
    while (t--) {
        int n;
        scanf("%d",&n);
        printf("%d\n",d[n]);
    }
}
```

## :ballot_box_with_check: 백준 11727

- 이전에 공부했던 내용을 찾아봐서 풀었다.
- 컴퓨터의 나머지 연산: 컴퓨터의 정수는 저장할 수 있는 범위가 지정되어 있기 때문에 답을 M으로 나눈 나머지를 출력하라는 문제가 등장한다.
  - (A+B) mod M = ((A mod M) + (B mod M)) mod M
  - (AXB) mod M = ((A mod M) X (B mod M)) mod M
  - (A-B) mod M = ((A mod M) - (B mod M)) mod M
  - 나누기는 성립하지 않는다.

## :ballot_box_with_check: 백준 12865

#### 시간초과

```python
import sys

def pickObject(index, sumW, sumV, isPick):
    global backpack, ans
    if index >= n: return
    if sumW > k: return
    if sumW <= k and sumV > ans: ans = sumV
    w = 0
    v = 0
    if isPick:
        w, v = backpack[index]
    pickObject(index + 1, sumW + w, sumV + v, True)
    pickObject(index + 1, sumW + w, sumV + v, False)

n, k = map(int, sys.stdin.readline().split(' '))
ans = 0
backpack = []
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split(' '))
    backpack.append((w, v))

pickObject(0, 0, 0, True)
pickObject(0, 0, 0, False)

print(ans)
```

- 재귀로 풀지 않고 논리적인 생각을 통해 앞의 결과 중 더 큰 것을 골라야함을 알았다.
