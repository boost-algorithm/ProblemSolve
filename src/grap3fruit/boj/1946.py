import sys 

def check_score(score_list):
  count = 0
  
  for i in range(0,len(score_list)-1):
    check = False
    for j in range(i+1, len(score_list)):
      print(i,j, score_list[i][1], score_list[j][1])
      if score_list[i][1] > score_list[j][1]: #[i][0]은 [j][0]보다 항상 큰 상태, 여기서 [1] 마저 크면,
        print(i,j)
        check = True
        count += 1
        break

  return count


if __name__ == "__main__":
  T = int(sys.stdin.readline())
  for i in range(T):
    N = int(sys.stdin.readline())
    score_list = []
    for j in range(N):
      score_list.append(list(map(int,sys.stdin.readline().strip().split())))

    score_list.sort(reverse=True)
    print(score_list)
    print("Score:", N - check_score(score_list))

