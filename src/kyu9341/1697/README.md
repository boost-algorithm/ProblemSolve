# Problem 1697

## 숨바꼭질

### 문제 링크
<https://www.acmicpc.net/problem/1697>


### solve
- x + 1, x - 1, x * 2 로 bfs

### 코드 설명
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static final int MAX = 100000;
    static int n, k;
    static boolean check[] = new boolean[MAX + 1];
    static int sec[] = new int[MAX + 1];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        Queue<Integer> q = new LinkedList<>();

        q.add(n);
        check[n] = true;
        sec[n] = 0;

        while(!q.isEmpty()) {
            int cur = q.poll();

            if (check[k]) break;

            if (cur * 2 <= MAX && !check[cur * 2]) {
                check[cur * 2] = true;
                sec[cur * 2] = sec[cur] + 1;
                q.add(cur * 2);
            }

            if (cur + 1 <= MAX && !check[cur + 1]) {
                check[cur + 1] = true;
                sec[cur + 1] = sec[cur] + 1;
                q.add(cur + 1);
            }

            if (cur - 1 >= 0 && !check[cur - 1]) {
                check[cur - 1] = true;
                sec[cur - 1] = sec[cur] + 1;
                q.add(cur - 1);
            }
        }

        System.out.println(sec[k]);

    }

}

```
