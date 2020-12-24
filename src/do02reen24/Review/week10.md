# :fire: week10

주제 : Dynamic programming

## :ballot_box_with_check: 백준 1010

- 다리가 겹칠 수 없기 때문에 오른쪽 다리에서 k 개를 선택하고 차례로 이어주면 된다. python의 combination 을 직접 불러 길이를 계산하는 방법도 있었지만, factorial을 쓰는 것이 더 빠를 것 같아 factorial로 구현하였다.

## :ballot_box_with_check: 백준 2579

- 마지막 칸에 도착하는 방법은 두가지가 있다. i-2, i-1, i번째 칸에 대해 oxo, xoo 로 선택하는 것이다.
- 각 경우 중 더 큰 값을 선택하며 다음칸으로 넘어가도록 구현하였다.

## :ballot_box_with_check: 백준 1149

- 문제가 dynamic-programming인 것을 고려하여 각 r, g, b에 대해 최소값을 누적하여 관리하는 리스트를 생성하여 해결하였다.
