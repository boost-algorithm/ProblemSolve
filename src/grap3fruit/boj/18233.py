import sys
from itertools import combinations
import copy

N, P, E = list(map(int,sys.stdin.readline().strip().split()))

members = []
for i in range(0,N):
  min, max = list(map(int,sys.stdin.readline().strip().split()))
  temp_set = set([])

  if min > E:
    continue

  if max > E:
    max = E

  for i in range(min,max+1):
    temp_set.add(i)
  members.append(temp_set)

print(members)

cases = []
for i in range(0,len(members)):
	cases.append(i)

combination_cases = list(combinations(cases,P))

print(combination_cases)

# n중 포문 생성.
def iter_func(case, count):
  if count == 0: #가장 깊은 스택
    sum_dic = dict()
    for i in members[case[len(case)-count-1]]:
      sum_dic[i] = [i]
    return sum_dic

  sum_dic = iter_func(case, count-1)

  temp_dic = copy.deepcopy(sum_dic)
  for i in members[case[len(case)-count-1]]:
    for key, value in sum_dic.items():
      try:
        if len(temp_dic[i+key]) == len(case): #이미 해당 key가 차있으면 넘어감
          continue
        if sum(temp_dic[i+key]+i) == i+key:
          temp_dic[i+key].append(i)
      except:
        newlist = list(value)
        newlist.append(i)
        temp_dic[i+key] = newlist
      
      if i+key == E and len(temp_dic[i+key]) == len(case): #현재 i+key 키가 E와 같고, 차있으면 바로 리턴.
        return temp_dic
    # print(temp_dic)
  
  return temp_dic

def getResult(case, value):
	result = []
	for i in range(0,N):
		result.append(0)

	for i in range(0,len(case)):
		result[case[i]] = value[len(case)-i-1]
	
	return result

flag = False
for case in combination_cases:
  case_dic = iter_func(case, len(case)-1)
  # print(case_dic)
  if E in case_dic.keys():
    if len(case_dic[E]) == len(case) :
      print(case)
      print(case_dic[E])
      flag = True
      
      print(getResult(case, case_dic[E]))
      # break
    
if flag == False:
  print(-1)

