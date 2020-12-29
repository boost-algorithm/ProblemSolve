# :fire: week7

## :ballot_box_with_check: 백준 1094

- list를 사용하지 않고 풀고 싶었는데 잘안돼서 그냥 list로 풀었다.
- 스터디 고찰: 비트마스크를 써서 풀면 코드가 훨씬 간결함을 알게 되었다.

## :ballot_box_with_check: 백준 14889

- c++의 permutation을 쓰면 쉬울 것 같아 c++로 해결하였다.
- 스터디 고찰 : python의 경우 combination을 써서 풀 수 있음을 알게 되었다.

## :ballot_box_with_check: 백준 18233

#### 틀렸습니다. (86%)

```c++
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, p, e;
    cin >> n >> p >> e;
    vector<pair<int,int>> member;
    vector<int> isGift(n);
    for (int i = 0; i < n; i++) {
        int min, max;
        cin >> min >> max;
        member.push_back(make_pair(min, max));
        if ((n - i) <= p) isGift[i] = 1;
    }
    do {
        int min = 0, max = 0;
        int sol[20] = { 0, };
        for (int i = 0; i < n; i++) {
            if (isGift[i] == 0) continue;
            min += member[i].first;
            max += member[i].second;
            sol[i] = member[i].first;
        }
        int remain = e - min;
        if (min <= e && max >= e) {
            for (int i = 0; i < n; i++) {
                if (isGift[i] == 0) continue;
                int diff = member[i].second - member[i].first;
                if (diff < remain) {
                    remain -= diff;
                    sol[i] += diff;
                }
                else {
                    sol[i] += remain;
                    break;
                }
            }
            for (int i = 0; i < n; i++) cout << sol[i] << " ";
            return 0;
        }
    } while (next_permutation(isGift.begin(), isGift.end()));
    cout << -1 << endl;
    return 0;
}
```

#### 틀렸습니다 (3%)

```python
import sys
from itertools import combinations

def rubberDuck():
    n, p, e = map(int, sys.stdin.readline().rstrip().split())
    member = []
    for _ in range(n):
        minDuck, maxDuck = map(int, sys.stdin.readline().rstrip().split())
        member.append([minDuck, (maxDuck-minDuck)])
    user = [i for i in range(n)]
    combList = list(combinations(user, p))

    for comb in combList:
        sol = [0] * n
        remain = e
        for i in comb:
            sol[i] = member[i][0]
            remain -= member[i][0]
        if remain < 0: continue
        for i in comb:
            if remain > member[i][1]:
                sol[i] += member[i][1]
                remain -= member[i][1]
            else:
                sol[i] += remain
                break
        return ' '.join(map(str,sol))
    return -1
print(rubberDuck())
```

- `return ' '.join(map(str,sol))`의 조건을 검사해주지 않아 틀렸음을 알게되었다.

```python
if remain == 0:
    return ' '.join(map(str,sol))
```

위 처럼 인형을 모두 알맞게 나누어주었는지 검사해주어 해결할 수 있었다.

## :ballot_box_with_check: 백준 1194
