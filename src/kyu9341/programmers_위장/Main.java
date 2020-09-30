package programmers42578;

import java.util.HashMap;

public class Solution {

    static HashMap<String, Integer> map = new HashMap<>();

    public int solution(String[][] clothes) {
        int answer = 1;
        for (int i = 0; i < clothes.length; i++) {
            if (map.get(clothes[i][1]) == null) map.put(clothes[i][1], 1);
            else map.put(clothes[i][1], map.get(clothes[i][1]) + 1);
        }
        for (String key : map.keySet()) answer *= map.get(key) + 1;
        answer--;
        return answer;
    }

}
