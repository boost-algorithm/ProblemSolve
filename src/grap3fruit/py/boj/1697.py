from collections import deque
import sys 

n, k = map(int,sys.stdin.readline().strip().split())

def get_possible(data):
	return [data-1, data+1, data*2]

def bfs(q, visited):
	new_q = deque()
	while q :
		current = q.popleft()
		visited[current] = 1
		for el in get_possible(current):
			if k == el :
				return True

			if el > 100000 or el < 0:
				continue

			if visited[el] == 0 :
				new_q.append(el)
				visited[el] = 1
		
	return new_q

def calc(root):
	if root == k:
		return print(0)

	q = deque()
	q.append(root)

	visited = [0]*100001
	count = 0
	while q:
		q = bfs(q, visited)
		count += 1
		if q == True:
			return print(count)

calc(n)