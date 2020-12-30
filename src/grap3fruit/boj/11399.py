import sys

# n = int(sys.stdin.readline())
# arr = list(map(int,sys.stdin.readline().strip().split()))

arr = [3,1,4,3,2]

arr.sort()
print(arr)

acc = 0
new_arr = []
for el in arr:
  acc += el
  new_arr.append(acc)

print(sum(new_arr))