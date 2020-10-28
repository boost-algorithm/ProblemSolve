# :fire: week8

주제 : Dynamic programming

## :ballot_box_with_check: 백준 9095

- python으로 쉽게 풀 수 있었다. 이전에 작성했던 c++코드를 보니 아래와 같이 푸는 방법도 있었다.

```c++
#include <stdio.h>
int d[11];
int main() {
    d[0] = 1;
    for (int i=1; i<=10; i++) {
        if (i-1 >= 0) {
            d[i] += d[i-1];
        }
        if (i-2 >= 0) {
            d[i] += d[i-2];
        }
        if (i-3 >= 0) {
            d[i] += d[i-3];
        }
    }
    int t;
    scanf("%d",&t);
    while (t--) {
        int n;
        scanf("%d",&n);
        printf("%d\n",d[n]);
    }
}
```

## :ballot_box_with_check: 백준 11727

## :ballot_box_with_check: 백준 12865
