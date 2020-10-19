import sys
from itertools import combinations

n = int(sys.stdin.readline())
arr = []

for i in range(0,n):
  arr.append(list(map(int,sys.stdin.readline().strip().split())))
# n = 6

cases = []
for i in range(1,n+1):
	cases.append(i)

# 전체 케이스 구하는 함수
def get_cases(n, cases):
	combination_cases = list(combinations(cases,int(n/2)))
	teamA_cases = []

	for case in combination_cases:
		if case[0] == 1 :
			teamA_cases.append(case)

	result = []
	for teamA in teamA_cases:
		teamB = (set(cases) - set(teamA))
		result.append([set(teamA), teamB])
	
	return result

cases = get_cases(n, cases)
print(cases)

# 사람 a,b 능력치 합
def get_sum(a,b,arr):
	return arr[a-1][b-1] + arr[b-1][a-1]

# print(get_sum(4,6,arr))

# 팀내 능력치 합 구하는 함수
def get_team_sum(team, arr):
	sum = 0
	for members in list(combinations(team,2)):
		# print(members)
		sum += get_sum(members[0], members[1], arr)

	return sum

# print(get_team_sum({1,2,3}, arr))

def calc(cases, arr):
	min = 1000

	for case in cases:
		teamA_sum = get_team_sum(case[0], arr)
		teamB_sum = get_team_sum(case[1], arr)

		current_min = abs(teamA_sum - teamB_sum)
		# print(case, current_min)
		if current_min < min :
			min = current_min

	return min

print(calc(cases, arr))