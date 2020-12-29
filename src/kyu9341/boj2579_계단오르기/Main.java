package boj2579_계단오르기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static final int MAX = 300;
    static int d[][] = new int[MAX + 1][3];
    static int score[] = new int[MAX + 1];
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        for (int i = 1; i <= n; i++) score[i] = Integer.parseInt(br.readLine());

        d[1][1] = score[1];
        d[1][2] = score[1];

        for (int i = 2 ; i<= n; i++) {
            d[i][1] = d[i - 1][2] + score[i];
            d[i][2] = Math.max(d[i - 2][1] + score[i], d[i - 2][2] + score[i]);
        }

        System.out.println(Math.max(d[n][1], d[n][2]));

    }
}
