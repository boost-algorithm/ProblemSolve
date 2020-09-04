package boj1158;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int n, k;
    static Queue<Integer> queue = new LinkedList<>();
    static ArrayList<Integer> res = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= n; i++) queue.add(i);

        while (!queue.isEmpty()) {
            for (int i = 0; i < k - 1; i++) queue.add(queue.poll());
            res.add(queue.poll());
        }

        StringBuilder sb = new StringBuilder();
        sb.append("<");
        for (int i = 0; i < res.size(); i++) {
            sb.append(res.get(i));
            if (i != res.size() - 1) sb.append(", ");
            else sb.append(">");
        }
        System.out.println(sb);
    }
}

