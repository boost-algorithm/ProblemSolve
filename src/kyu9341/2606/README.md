# Problem 2606

## 바이러스

### 문제 링크
<https://www.acmicpc.net/problem/2606>

### solve
- 먼저 컴퓨터를 모두 연결시킨 후 dfs로 1번 컴퓨터와 연결된 컴퓨터를 모두 구한다.

### 코드 설명
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    static int n, m;
    static ArrayList<ArrayList<Integer>> net = new ArrayList<>();
    static boolean check[];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        check = new boolean[n + 1];

        for (int i = 0; i <= n; i++) {
            net.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            net.get(u).add(v);
            net.get(v).add(u);
        }

        dfs(1);

        int cnt = 0;
        for (int i = 1; i <= n; i++) {
            if (check[i]) cnt++;
        }

        System.out.println(cnt - 1);
    }

    static void dfs(int node) {
        if (check[node]) return;
        check[node] = true;

        for (int i = 0; i < net.get(node).size(); i++) {
            int next = net.get(node).get(i);
            if (!check[next]) {
                dfs(next);
            }
        }
    }
}

```
