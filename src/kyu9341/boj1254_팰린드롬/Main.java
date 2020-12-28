package boj1254_팰린드롬;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static String S;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        S = br.readLine();
        int ans = 0;

        for (int i = 0; i < S.length(); i++) {
            if (checkPalindrome(S, i)) {
               ans = S.length() + i;
               break;
            }
        }
        System.out.println(ans);

    }

    static boolean checkPalindrome(String s, int start) {
        int end = s.length() - 1;
        for (int i = start; i <= end; i++) {
            if (s.charAt(i) != s.charAt(end + start - i)) return false;
        }
        return true;
    }
}
