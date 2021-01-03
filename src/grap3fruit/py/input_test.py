import sys 
from collections import deque
#n, m = map(int,sys.stdin.readline().strip().split())
#num = list(map(int,sys.stdin.readline().strip().split()))

#
#datas = list(map(int,sys.stdin.readline().strip().split()))

#print(num[0]*num[1])


## case ##
# 5
# 3 2 1 -3 -1 

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().strip().split()))


## case ##
# 1 2 3 4 5

num_list = list(map(int, input().split()))

## case ##
# abcd
# 3
# P x
# L
# P y

input_data = sys.stdin.readline().strip()
cmd_count = int(sys.stdin.readline().strip())
cmd = []

for i in range(0, cmd_count):
  cmd.append(list(sys.stdin.readline().strip().split()))