---
layout: post
title: "백준 1107번 리모컨"
subtitle: "Baekjoon algorithm"
date: 2020-02-26 09:51:12
author: kwon
categories: algorithm
tags:
	- Algorithm
---
# Problem 1107

## 리모컨

### 문제
요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

### 입력
첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)

### 출력
예제와 같이 요세푸스 순열을 출력한다.

### 문제 링크
<https://www.acmicpc.net/problem/1158>

### 예제 입력 1
7 3

### 예제 출력 1
<3, 6, 2, 7, 5, 1, 4>

### solve
- 큐를 사용하여 n개의 원소를 큐에 넣어준다.
- 원의 형태를 한 번 이동할 때 큐의 맨 앞의 원소를 빼서 맨 뒤에 넣어주는 방식으로 구현한다.
- 큐가 빌 때까지 k번 이동하고 원소 하나를 제거하는 것을 반복하고, 제거되는 원소를 차례로 출력한다.

### 코드 설명
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int n, k;
    static Queue<Integer> queue = new LinkedList<>();
    static ArrayList<Integer> res = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= n; i++) queue.add(i);

        while (!queue.isEmpty()) {
            for (int i = 0; i < k - 1; i++) queue.add(queue.poll());
            res.add(queue.poll());
        }

        StringBuilder sb = new StringBuilder();
        sb.append("<");
        for (int i = 0; i < res.size(); i++) {
            sb.append(res.get(i));
            if (i != res.size() - 1) sb.append(", ");
            else sb.append(">");
        }
        System.out.println(sb);
    }
}
```
