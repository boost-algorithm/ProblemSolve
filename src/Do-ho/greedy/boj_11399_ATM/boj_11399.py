import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().strip().split()))

P.sort()

Psum = 0
offset = 0

for item in P:
    offset += item
    Psum += offset

sys.stdout.write(str(Psum) + '\n')