import sys

def check_word(word):
  arr = []
  for idx, val in enumerate(word):
    if not val in arr:
      arr.append(val)
    elif val in arr:
      if word[idx-1] == val:
        continue
      return 0
  
  return 1

n = int(sys.stdin.readline().strip())
words = []
answer = 0

for i in range(0, n):
  answer += check_word((sys.stdin.readline().strip().split())[0])

print(answer)