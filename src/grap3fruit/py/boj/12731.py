import sys
import copy

def getMinValueFromStr(time_str = "12:35"):
  hour = int(time_str[0]+time_str[1])
  min = int(time_str[3]+time_str[4])
  return hour*60 + min

def calc(backup_na, backup_nb, T):
  print("check1: ", backup_na, backup_nb)
  na_arr = copy.deepcopy(backup_na)
  nb_arr = copy.deepcopy(backup_nb)

  count_na = len(backup_na)
  count_nb = len(backup_nb)
  for na_el in na_arr : # NA가 먼저 돌때, NB해당되는게있으면,
    min = na_el[0] - T # NA[1] 응 내가 먼저 NB 가져갈게~ 해서 NB 빼줘야함. 다음 NA들이 착각 안하도록 ㅇㅇ
    for nb_el in nb_arr:
      print("na_el:",na_el[0]," nb_el:", nb_el[1])
      if min >= nb_el[1] :
        nb_arr.remove(nb_el)
        count_na -= 1
        break

  na_arr = backup_na
  nb_arr = backup_nb
  for nb_el in nb_arr :
    min = nb_el[0] - T 
    for na_el in na_arr:
      if min >= na_el[1] :
        na_arr.remove(na_el)
        count_nb -= 1
        break

  return [count_na, count_nb]


def main():
  N = int(sys.stdin.readline())

  for x in range(N):
    T = int(sys.stdin.readline()) # 회차시간
    NA, NB = list(map(int,sys.stdin.readline().strip().split()))

    na_arr = []
    nb_arr = []

    for i in range(NA):
      temp_arr = list(map(str,sys.stdin.readline().strip().split()))
      min = getMinValueFromStr(temp_arr[0])
      max = getMinValueFromStr(temp_arr[1])
      na_arr.append([min,max])
      print(i, min, max)

    for i in range(NB):
      temp_arr = list(map(str,sys.stdin.readline().strip().split()))
      min = getMinValueFromStr(temp_arr[0])
      max = getMinValueFromStr(temp_arr[1])
      nb_arr.append([min,max])
      print(i, min, max)

    print(NA,NB)
    print(na_arr, nb_arr)
    na_arr.sort()
    nb_arr.sort()

    result_NA, result_NB = calc(na_arr, nb_arr, T)

    print("Case #{}:".format(x+1), result_NA, result_NB)

main()
