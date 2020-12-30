package boj1149_RGB거리;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    final static  int MAX = 1000;
    final static int RED = 0;
    final static int GREEN = 1;
    final static int BLUE = 2;

    static int n;
    static int d[][] = new int[MAX + 1][3];
    static int cost[][] = new int[MAX + 1][3];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            cost[i][RED] = Integer.parseInt(st.nextToken());
            cost[i][GREEN] = Integer.parseInt(st.nextToken());
            cost[i][BLUE] = Integer.parseInt(st.nextToken());
        }

        d[1][RED] = cost[1][RED];
        d[1][GREEN] = cost[1][GREEN];
        d[1][BLUE] = cost[1][BLUE];

        for (int i = 1; i <= n; i++) {
            d[i][RED] = Math.min(d[i - 1][GREEN], d[i - 1][BLUE]) + cost[i][RED];
            d[i][GREEN] = Math.min(d[i - 1][RED], d[i - 1][BLUE]) + cost[i][GREEN];
            d[i][BLUE] = Math.min(d[i - 1][GREEN], d[i - 1][RED]) + cost[i][BLUE];
        }

        int min = Math.min(d[n][RED], Math.min(d[n][GREEN], d[n][BLUE]));
        System.out.println(min);

    }
}
