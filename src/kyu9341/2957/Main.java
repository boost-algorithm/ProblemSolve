package boj2957;

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
