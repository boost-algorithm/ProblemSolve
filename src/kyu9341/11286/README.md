# Problem 11286

## 절대값 힙

### 문제 링크
<https://www.acmicpc.net/problem/11286>


### solve

- 우선순위 큐를 활용하여 절대값이 작은 수에 가장 높은 우선순위를 주어 구현했다.
    - 이 때, 절대값이 같은 경우 더 작은 수가 우선이 되는 것을 고려한다.

### 코드
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {

    static int n;
    static PriorityQueue<Integer> pq = new PriorityQueue<>(new Comparator<Integer>() {
        @Override
        public int compare(Integer o1, Integer o2) {
            if (Math.abs(o1) == Math.abs(o2)) return o1 > o2 ? 1 : -1;
            return Math.abs(o1) > Math.abs(o2) ? 1 : -1;
        }
    });

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(br.readLine());
            if (x == 0) {
                if (pq.isEmpty()) sb.append("0" + '\n');
                else sb.append(pq.poll().toString() + '\n');
            }
            else pq.add(x);
        }
        System.out.println(sb);
    }
}
```
