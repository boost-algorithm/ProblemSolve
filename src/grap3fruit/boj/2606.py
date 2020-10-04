import sys
from collections import deque

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

datas = []

for i in range(0,m):
  datas.append(list(map(int,list(sys.stdin.readline().strip().split()))))

dic = {}
for value in datas:
  try: 
    if len(dic[value[0]]) != 0 :
      dic[value[0]].add(value[1])
  except :
    dic[value[0]] = set([value[1]])

for value in datas:
  try: 
    if len(dic[value[1]]) != 0 :
      dic[value[1]].add(value[0])
  except :
    dic[value[1]] = set([value[0]])

print(dic)
visited = set()
def dfs_recursive(root, dic):
  visited.add(root)

  for key, values in dic.items():
    if key == root :
      for value in values :
        if value in visited:
          continue
        visited.add(value)
        dfs_recursive(value, dic)

def dfs_stack(root, dic):
  stack = [root]

  while stack :
    root = stack.pop()

    for key, values in dic.items():
      if key == root :
        for value in values :
          if value in visited:
            continue
          visited.add(value)
          stack.append(value)

def bfs_queue(root, dic):
  queue = deque()
  queue.append(root)

  while queue :
    root = queue.popleft()

    for key, values in dic.items():
      if key == root :
        for value in values :
          if value in visited:
            continue
          visited.add(value)
          queue.append(value)

bfs_queue(1,dic)
print(visited)