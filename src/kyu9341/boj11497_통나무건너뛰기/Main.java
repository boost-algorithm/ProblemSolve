package boj11497_통나무건너뛰기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int t;
    static int n;
    static Deque<Integer> dq = new ArrayDeque<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        while (n-- > 0) {
            t = Integer.parseInt(br.readLine());
            ArrayList<Integer> list = new ArrayList<>(t);
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < t; i++) {
                int cur = Integer.parseInt(st.nextToken());
                list.add(cur);
            }

            list.sort(null);

            while (list.size() > 0) {
                dq.addLast(list.remove(list.size() - 1));
                if (list.size() == 0) break;
                dq.addFirst(list.remove(list.size() - 1));
            }

            int max = 0;
            int prev = dq.getLast();

            while (!dq.isEmpty()) {
                int cur = dq.pollFirst();
                int diff = Math.abs(prev - cur);
                if (max < diff) max = diff;
                prev = cur;
            }

            System.out.println(max);

        }
    }
}
