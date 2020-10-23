package boj1946_신입사원;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

    static int t;
    static int n;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            n = Integer.parseInt(br.readLine());
            ArrayList<Person> people = new ArrayList<>();

            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                int document = Integer.parseInt(st.nextToken());
                int interview = Integer.parseInt(st.nextToken());
                people.add(new Person(document, interview));
            }

            Collections.sort(people);

            int cnt = 0;
            int target = people.get(0).interview;
            for (int i = 1; i < n; i++) {
                if (target < people.get(i).interview) cnt++;
                else target = people.get(i).interview;
            }

            System.out.println(n - cnt);
        }
    }

    static class Person implements Comparable<Person>{
        int document;
        int interview;

        public Person(int document, int interview) {
            this.document = document;
            this.interview = interview;
        }

        @Override
        public int compareTo(Person o) {
            if (this.document == o.document) return this.interview - o.interview;
            return this.document - o.document;
        }
    }
}
