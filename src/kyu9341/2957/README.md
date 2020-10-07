# Problem 2957

## 이진 탐색 트리

### 문제 링크
<https://www.acmicpc.net/problem/2346>


### solve
- 단순히 노드 클래스를 만들고 문제에서 주어진 대로 삽입 연산을 구현하니까 시간초과가 난다.
- 졸리니까 일단 잔다..ㅜ


### 코드 설명
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int n;
    static int c = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        Node root = new Node(Integer.parseInt(br.readLine()));
        for (int i = 0; i < n - 1; i++) {
            int x = Integer.parseInt(br.readLine());
            insert(x, root);
            System.out.println(c);
        }
    }

    static void insert(int x, Node node) {
        c++;
        if (x < node.data) {
            if (node.left == null) node.left = new Node(x);
            else insert(x, node.left);
        }
        else {
            if (node.right == null) node.right = new Node(x);
            else insert(x, node.right);
        }
    }

    static class Node {
        int data;
        Node left;
        Node right;

        public Node(int data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }
}

```
