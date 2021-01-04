import sys
import pprint
from collections import deque

def printArr(arr):
	print('[')
	for i in range(0,len(arr)):
		print('[',end="")
		for j in range(0,len(arr[0])):
			print(arr[i][j])
		print(']')
	
	print(']')

def check_zero(arr):
	for i in arr:
		for j in i:
			if 0 in j:
				return True

def after_moment(new_q, i,j,k):
	try:
		if arr[i][j][k+1] == 0: 
			arr[i][j][k+1] = 1
			new_q.append([i,j,k+1])
	except:
		pass

	try:
		if arr[i][j][k-1] == 0 and k > 0:
			arr[i][j][k-1] = 1
			new_q.append([i,j,k-1])
	except:
		pass

	try:
		if arr[i][j+1][k] == 0:
			arr[i][j+1][k] = 1
			new_q.append([i,j+1,k])
	except:
		pass

	try:
		if arr[i][j-1][k] == 0 and j > 0:
			arr[i][j-1][k] = 1
			new_q.append([i,j-1,k])
	except:
		pass

	try:
		if arr[i+1][j][k] == 0:
			arr[i+1][j][k] = 1
			new_q.append([i+1,j,k])
	except:
		pass       

	try:
		if arr[i-1][j][k] == 0 and i > 0:
			arr[i-1][j][k] = 1
			new_q.append([i-1,j,k])
	except:
		pass   

	return new_q

def bfs(q):
	new_q = deque()
	while q:
		i, j, k = q.popleft()
		after_moment(new_q, i, j, k)
	
	printArr(arr)
	print(new_q)
	return new_q

def calc(q):
	count = 0
	while q:
		q = bfs(q)
		count += 1

	if check_zero(arr):
		return print(-1)
	
	return print(count-1)

if __name__ == "__main__":
	inputs = list(map(int,sys.stdin.readline().strip().split()))
	m = inputs[0]
	n = inputs[1]
	h = inputs[2]

	arr = []
	for j in range(0,h):
		temp_arr = []
		
		for i in range(0,n):
			inputs = list(map(int,sys.stdin.readline().strip().split()))
			temp_arr.append(inputs)

		arr.append(temp_arr)

	q = deque()

	for i in range(0,h):
		for j in range(0,n):
			for k in range(0,m):
				if arr[i][j][k] == 1:
					q.append([i,j,k])

	calc(q)
