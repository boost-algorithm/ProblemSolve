# Problem 2346

## 풍선 터뜨리기

### 문제
N개의 풍선이 있다. 각 풍선 안에는 -N부터 N까지의 수가 적혀있는 종이가 들어 있다. 이 풍선들을 다음과 같은 규칙으로 터뜨린다.

우선, 제일 처음에는 1번 풍선을 터뜨린다. 다음에는 풍선 안에 있는 종이를 꺼내어 그 종이에 적혀있는 값만큼 이동하여 다음 풍선을 터뜨린다. 양수가 적혀 있을 경우에는 오른쪽으로, 음수가 적혀 있을 때는 왼쪽으로 이동한다. 풍선은 원형으로 놓여 있다고 생각한다. 즉, 1번 풍선의 왼쪽에 N번 풍선이 있고, N번 풍선의 오른쪽에 1번 풍선이 있는 것이다. 이동할 때에는 이미 터진 풍선은 빼고 생각한다.

예를 들어 다섯 개의 풍선 안에 차례로 3, 2, 1, -3, -1이 적혀 있었다고 하자. 이 경우 3이 적혀 있는 1번 풍선, -3이 적혀 있는 4번 풍선, -1이 적혀 있는 5번 풍선, 1이 적혀 있는 3번 풍선, 2가 적혀 있는 2번 풍선의 순서대로 터지게 된다.

### 입력
첫째 줄에 자연수 N(1≤N≤1,000)이 주어진다. 다음 줄에는 차례로 각 풍선 안의 종이에 적혀 있는 수가 주어진다. 편의상 0은 적혀있지 않다고 가정하자.

### 출력
첫째 줄에 터진 풍선의 번호를 차례로 나열한다.

### 문제 링크
<https://www.acmicpc.net/problem/2346>


### solve
- 풍선이 원형으로 놓여 있고, 풍선의 번호에 따라 좌, 우로 이동하기 때문에 덱을 사용했다.
- balloon 클래스를 만들어 풍선의 번호와 적힌 숫자를 담는다.
- 좌측으로 이동하는 경우 - 덱의 맨 뒤 원소를 맨 앞으로 이동
- 우측이로 이동하는 경우 - 덱의 맨 앞 원소를 맨 뒤로 이동
  - 이 때, 현재 풍선을 터트린 뒤 이동하기 때문에 우측으로 이동하는 경우는 한 번 덜 이동한다.
- 풍선을 터뜨릴 때마다 해당 풍선의 번호를 기록한다.

### 코드 설명
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

    static Deque<Balloon> dq = new ArrayDeque<>();
    static int n;
    static Balloon[] balloon;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        balloon = new Balloon[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            dq.add(new Balloon(i, Integer.parseInt(st.nextToken())));
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            Balloon cur = dq.pollFirst();
            sb.append(cur.num);
            if (i != n - 1) sb.append(" ");
            if (cur.count < 0) moveLeft(-cur.count);
            else moveRight(cur.count);
        }
        System.out.println(sb);
    }

    static void moveLeft(int num) {
        for (int i = 0; i < num; i++) {
            if (!dq.isEmpty()) dq.addFirst(dq.pollLast());
        }
    }

    static void moveRight(int num) { // 우측으로 이동하는 경우는 한번 덜 이동 - 터트린 풍선은 개수 count
        for (int i = 0; i < num - 1; i++) {
            if (!dq.isEmpty()) dq.addLast(dq.pollFirst());
        }
    }

    static class Balloon {
        int num;
        int count;
        public Balloon(int num, int count) {
            this.num = num;
            this.count = count;
        }
    }

}

```
