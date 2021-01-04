import sys
from collections import deque

data = sys.stdin.readline().strip()

def checkPD(data):
	N = len(data)

	if N % 2 == 0:
		if data[int(N/2)] != data[int(N/2)-1] :
			return False
		
		for i in range(0, int(N/2)):
			if data[i] != data[N-i-1] :
				return False

		return True

	if N % 2 == 1:
		for i in range(0, int(N/2)):
			if data[i] != data[N-i-1] :
				return False

		return True

# print(checkPD(['a','b','b','c','a']))

# deq = deque(['a','b','c','b', 'a'])
# print(checkPD(deq))

def calc(data):
	N = len(data)
	if N == 1:
		print(1)
		return

	count = N
	add_string = deque([])
	for i in range(0, N):
		PD = deque(data)
		PD.extend(add_string)

		if checkPD(PD):
			print(count, PD)
			return

		add_string.appendleft(data[i])
		count += 1

calc(data)