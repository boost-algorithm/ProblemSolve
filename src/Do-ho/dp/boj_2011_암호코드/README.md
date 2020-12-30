# 암호코드

탑다운으로 생각해서 적용해봄 재귀 너무 많이 도는 듯..
```런다임 에러```

```
import sys

def isDivision(n):
    return n>=10 and n<=26

def DP(n, l):
    if (l<=0): return 0
    if (l==1): return 1
    if (l==2):
        if(isDivision(int(n[:l]))): return 2
        return 1
    if(isDivision(int(n[l-2:l]))): return DP(n, l-1) + DP(n, l-2)
    return DP(n, l-1)

N = sys.stdin.readline().strip()
L = len(N)

print(DP(N, L)%1000000)
```

바텀 업으로 풀어보자....

D(n) = D(n-1) + D(n-2) (분기가 될 경우)
D(n) = D(n-1) (분기가 되지 않을 경우)

입력이 0인것도 처리...

반례 찾기...
1. 100일때 -> 0
2. 36036일때 -> 0

0앞에 1개나 2개가 잘못되면 안됨

100