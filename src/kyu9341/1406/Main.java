package boj1406;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    static String str;
    static int m;
    static Stack<Character> left = new Stack<>();
    static Stack<Character> right = new Stack<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        str = br.readLine();
        for (int i = 0; i < str.length(); i++) left.push(str.charAt(i));

        m = Integer.parseInt(br.readLine());
        for (int i = 0; i < m; i++) {
            String command = br.readLine();
            if (command.charAt(0) == 'L' && !left.isEmpty()) right.push(left.pop());
            else if (command.charAt(0) == 'D' && !right.isEmpty()) left.push(right.pop());
            else if (command.charAt(0) == 'B' && !left.isEmpty()) left.pop();
            else if (command.charAt(0) == 'P') left.push(command.charAt(2));
        }

        while(!left.isEmpty()) right.push(left.pop());
        StringBuilder sb = new StringBuilder();
        while(!right.isEmpty()) sb.append(right.pop());
        System.out.println(sb);
    }
}
