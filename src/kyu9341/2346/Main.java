package boj2346;

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
