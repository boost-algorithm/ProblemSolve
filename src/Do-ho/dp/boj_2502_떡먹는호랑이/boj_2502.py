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