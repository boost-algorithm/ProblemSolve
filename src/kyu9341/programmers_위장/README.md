# 프로그래머스 - 위장

### 문제 링크
<https://programmers.co.kr/learn/courses/30/lessons/42578>


### solve
- 해시 맵을 이용하여 각각 종류별로 몇 개의 의상이 있는지 기록한다.
- 의상의 종류별로 입을 수도 있고 입지 않는 경우도 있으므로 (각 의상의 종류 + 1)을 모두 곱한다.
- 의상을 하나도 입지 않은 경우는 없으므로 마지막에 -1을 해주어야 한다.

### 코드
```java
package programmers42578;

import java.util.HashMap;

public class Solution {

    static HashMap<String, Integer> map = new HashMap<>();

    public int solution(String[][] clothes) {
        int answer = 1;
        for (int i = 0; i < clothes.length; i++) {
            if (map.get(clothes[i][1]) == null) map.put(clothes[i][1], 1);
            else map.put(clothes[i][1], map.get(clothes[i][1]) + 1);
        }
        for (String key : map.keySet()) answer *= map.get(key) + 1;
        answer--;
        return answer;
    }

}
```
