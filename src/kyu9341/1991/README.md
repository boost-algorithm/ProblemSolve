# Problem 1991

## 트리 순회

### 문제 링크
<https://www.acmicpc.net/problem/1991>


### solve
- 항상 A부터 차례로 입력되고 최대 26개이기 때문에 26개의 Node배열을 만들어 0 : A, 1 : B ... 로 대응시켜 사용하였다.
- 자식 노드가 없는 경우 -1, 있는 경우면 해당 문자의 아스키 코드 값을 저장하고, dfs로 각각 전위 순회, 중위 순회, 후위 순회를 구현했다.

### 코드 설명
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static Node[] tree = new Node[26];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            char root = st.nextToken().charAt(0);
            char left = st.nextToken().charAt(0);
            char right = st.nextToken().charAt(0);
            tree[root - 'A'] = new Node(left == '.' ? -1 : left, right == '.' ? -1 : right);
        }
        preorder('A');
        System.out.println();
        inorder('A');
        System.out.println();
        postorder('A');

    }
    static void preorder(int root) {
        if (root == -1) return;
        System.out.print((char)root);
        preorder(tree[root - 'A'].left);
        preorder(tree[root - 'A'].right);
    }

    static void inorder(int root) {
        if (root == -1) return;
        inorder(tree[root - 'A'].left);
        System.out.print((char)root);
        inorder(tree[root - 'A'].right);
    }

    static void postorder(int root) {
        if (root == -1) return;
        postorder(tree[root - 'A'].left);
        postorder(tree[root - 'A'].right);
        System.out.print((char)root);
    }

    static class Node {
        int left;
        int right;
        Node (int left, int right){
            this.left = left;
            this.right = right;
        }
    }
}
```
