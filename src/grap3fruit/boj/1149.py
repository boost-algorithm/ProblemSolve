import sys

N = int(sys.stdin.readline())

data = []
for _ in range(N):
  RGB = list(map(int,sys.stdin.readline().strip().split()))
  data.append(RGB)

print(data)

def get_min(datum):
  min = [datum[0],'R']
  if datum[1] < min[0]:
    min = [datum[1],'G']
  if datum[2] < min[0]:
    min = [datum[2],'B']
  return min

def get_min_dp_n_1(dp_N_1, a_N):
  result = []
  if dp_N_1[1] == 'R':
    if a_N[1] < a_N[2] :
      return [dp_N_1[0] + a_N[1],'G']
    return [dp_N_1[0] + a_N[2],'B']

  elif dp_N_1[1] == 'G':
    if a_N[0] < a_N[2] :
      return [dp_N_1[0] + a_N[0],'R']
    return [dp_N_1[0] + a_N[2],'B']

  elif dp_N_1[1] == 'B':
    if a_N[0] < a_N[1] :
      return [dp_N_1[0] + a_N[0],'R']
    return [dp_N_1[0] + a_N[1],'G']

def get_min_n_1_n_2(color, a_N_1, a_N):
  result = []
  min = 2001
  if color == 'R':
    if a_N_1[1] + a_N[0] < min : # G + R
      min = a_N_1[1] + a_N[0]
      result = [min, 'R']
    if a_N_1[1] + a_N[2] < min : # G + B
      min = a_N_1[1] + a_N[2]
      result = [min, 'B']
    if a_N_1[2] + a_N[0] < min : # B + R
      min = a_N_1[2] + a_N[0]
      result = [min, 'R']
    if a_N_1[2] + a_N[1] < min : # B + G
      min = a_N_1[2] + a_N[1]
      result = [min, 'G']

  min = 2001
  if color == 'G':
    if a_N_1[0] + a_N[1] < min : # R + G
      min = a_N_1[0] + a_N[1]
      result = [min, 'G']
    if a_N_1[0] + a_N[2] < min : # R + B
      min = a_N_1[0] + a_N[2]
      result = [min, 'B']
    if a_N_1[2] + a_N[1] < min : # B + G
      min = a_N_1[2] + a_N[1]
      result = [min, 'G']
    if a_N_1[2] + a_N[0] < min : # B + R
      min = a_N_1[2] + a_N[0]
      result = [min, 'R']

  min = 2001
  if color == 'B':
    if a_N_1[0] + a_N[1] < min : # R + G
      min = a_N_1[0] + a_N[1]
      result = [min, 'G']
    if a_N_1[0] + a_N[2] < min : # R + B
      min = a_N_1[0] + a_N[2]
      result = [min, 'B']
    if a_N_1[1] + a_N[0] < min : # G + R
      min = a_N_1[1] + a_N[0]
      result = [min, 'R']
    if a_N_1[1] + a_N[2] < min : # G + B
      min = a_N_1[1] + a_N[2]
      result = [min, 'B']

  return result

# print(get_min_n_1_n_2('R', [26,40,83],[49,60,57]))
  

def get_min_dp_n_2(dp_N_2, a_N_1, a_N):
  result = []

  result = get_min_n_1_n_2(dp_N_2[1], a_N_1, a_N)
  result[0] += dp_N_2[0]
  print("n-2",result)
  return result

# print(get_min_n_1([26,'R'], [49,60,70]))

def calc():
  dp = [0]*1001

  dp[0] = get_min(data[0])
  if N == 1:
    return dp[0][0]

  dp[1] = min(get_min_dp_n_1([data[0][0],'R'], data[1]),get_min_dp_n_1([data[0][1],'G'], data[1]),get_min_dp_n_1([data[0][2],'B'], data[1]))
  if N == 2:
    return dp[1][0]

  for i in range(2, N):
    test1 = get_min_dp_n_2(dp[i-2], data[i-1], data[i])
    test2 = get_min_dp_n_1(dp[i-1], data[i])
    print(test1, test2)
    dp[i] = min(test1, test2)
    # dp[i] = min(get_min_dp_n_2(dp[i-2], data[i-1], data[i]), get_min_dp_n_1(dp[i-1], data[i]))
  
  print(dp)
  return dp[N-1][0]

print(calc())
