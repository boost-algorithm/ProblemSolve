package boj11286;

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
