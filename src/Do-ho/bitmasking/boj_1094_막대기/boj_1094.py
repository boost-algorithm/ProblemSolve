import sys

X = int(sys.stdin.readline())

count = 0
while(X!=0):
    if X%2==1: count += 1
    X = X >> 1

sys.stdout.write(str(count))