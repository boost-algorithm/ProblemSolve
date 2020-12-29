package boj1010_다리놓기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int t;
    static int n, m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            int max = Math.max(n, m - n);
            int min = Math.min(n, m - n);

            long tmp = 1;
            for (int i = m; i >= max + 1; i--) {
                tmp *= i;
            }

            long res = tmp / getFactorial(min);
            System.out.println(res);
        }

    }

    static long getFactorial(int n) {
        long res = 1;
        while (n > 0) {
            res *= n--;
        }
        return res;
    }


}
