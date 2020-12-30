# 떡 먹는 호랑이

R3 = R2 + R1
R4 = R3 + R2 = R2 + R2 + R1 = 2R2 + R1
R5 = R4 + R3 = 2R3 + R2 = 2(R2 + R1) + R2 = 3R2 + 2R1
R6 = R5 + R4 = 2R4 + R3 = 2(2R2 + R1) + (R2 + R1) = 5R2 + 3R1

계수가 규칙이 있는듯!

1 1 2 3 5 8 13

피보나치로 증가

R3 = 1 1 >> 얘가 1 1으로 시작하니 반복 시작하면 될듯

```
import sys

def calculate(a, b, A, B):
    return a*A + b*B

D, K = map(int, sys.stdin.readline().rstrip().split())

FIBO = [1 for _ in range(D)]
for i in range(2, D):
    FIBO[i] = FIBO[i-1] + FIBO[i-2]

a, b = FIBO[D-3], FIBO[D-2]

def getResult():
    for i in range(1, K):
        for j in range(1, K):
            result = calculate(a, b, i, j)
            if(result > K): break
            if(result==K):
                return str(i)+'\n'+str(j)+'\n'

sys.stdout.write(getResult())
```

반복문 하나 줄이기
```
import sys

def calculate(a, b, A, B):
    return a*A + b*B

D, K = map(int, sys.stdin.readline().rstrip().split())

FIBO = [1 for _ in range(D)]
for i in range(2, D):
    FIBO[i] = FIBO[i-1] + FIBO[i-2]

a, b = FIBO[D-3], FIBO[D-2]

def getResult():
    for i in range(1, K):
        j = (K - a*i)/b
        if j.is_integer(): return str(i)+'\n'+str(int(j))+'\n'

sys.stdout.write(getResult())
```