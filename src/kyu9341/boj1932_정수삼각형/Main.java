package boj1932_정수삼각형;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    final static int MAX = 500;
    static int n;
    static int tri[][] = new int[MAX + 1][MAX + 1];
    static int d[][] = new int[MAX + 1][MAX + 1];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= i; j++) {
                tri[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        d[1][1] = tri[1][1];

        for (int i = 2; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                d[i][j] = Math.max(d[i - 1][j - 1], d[i - 1][j]) + tri[i][j];
            }
        }

        int ans = 0;

        for (int i = 1; i <= n; i++) {
            ans = Math.max(ans, d[n][i]);
        }

        System.out.println(ans);
    }

}
