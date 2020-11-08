import sys

def get_mCn(N, M):
  mom = N
  mom_index = N
  child = M
  child_index = M

  for _ in range(M-1):
    
    mom = mom * (mom_index-1)
    mom_index -= 1

  while child_index > 1:
    child = child * (child_index-1)
    child_index -= 1

  return(int(mom/child))

T = int(sys.stdin.readline())

for _ in range(T):
  N, M = list(map(int,sys.stdin.readline().strip().split()))
  print(get_mCn(M, N))

