import sys

def fibonacci(x):
    if x < 2: return 1
    if data[x] != 0: return data[x]
    else:
        data[x] = fibonacci(x-1) + fibonacci(x-2)
        return data[x]

d, k = map(int, sys.stdin.readline().split())
data = [0] * d

f1 = fibonacci(d-3)
f2 = fibonacci(d-2)
for a in range(1, int(k/2) + 1):
    sub = k - (f1 * a)
    b = int(sub/f2)
    if (f1 * a) + (f2 * b) == k: 
        print(a)
        print(b)
        break