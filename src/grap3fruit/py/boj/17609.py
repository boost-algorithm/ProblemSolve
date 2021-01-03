import sys 

def checkPD2(data, start_idx, l_r_flag):
  N = len(data)
  left = 0
  right = 0

  if l_r_flag == 'left':
    left = 1
  if l_r_flag == 'right':
    right = 1

  for i in range(start_idx, int(N/2)):
    if data[i+left] != data[N-i-1-right] :
      return 2
  return 1

def checkPD1(data):
  N = len(data)

  for i in range(0, int(N/2)):
    if data[i] != data[N-i-1] :
      result = checkPD2(data, i, 'left')
      if result == 1 :
        return 1
      result = checkPD2(data, i, 'right')
      return result

  return 0

N = int(sys.stdin.readline())

for _ in range(N) :
	data = sys.stdin.readline().strip()
	print(checkPD1(data))

