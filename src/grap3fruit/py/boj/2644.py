import sys

N = int(sys.stdin.readline())
A, B = map(int,sys.stdin.readline().strip().split())
M = int(sys.stdin.readline())

dic = {}
for _ in range(M):
  parent, child = map(int,sys.stdin.readline().strip().split())
  try:
    if dic[parent] :
      dic[parent].append(child)
  except :
    dic[parent] = [child]
print(dic)

def dps(root, target, result):
  try:
    if dic[root]:
      if target in dic[root]:
        result.add(root)
        result.add(target)
        return True

      for el in dic[root]:
        target_flag = dps(el, target, result)
        if target_flag == True:
          result.add(root)
          return True

  except:
    return False


def solution(N, A, B, M, dic):
  for parent in dic :
    result_A = set([parent])
    result_B = set([parent])
    dps(parent, A, result_A)
    dps(parent, B, result_B)

    if (A in result_A) and (B in result_B):
      intersec = result_A & result_B
      return abs(len(result_A - intersec) + len(result_B - intersec))
    
  return -1
       
print(solution(N, A, B, M, dic))