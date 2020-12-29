import sys
from datetime import datetime, timedelta

def trainInput(n, result, alpha):
    for _ in range(n):
        [inputStartTime, inputEndTime] = list(sys.stdin.readline().strip().split())
        startTime = list(map(int, inputStartTime.split(':')))
        endTime = list(map(int, inputEndTime.split(':')))

        start = datetime(2020, 11, 14, startTime[0], startTime[1])
        end = datetime(2020, 11, 14, endTime[0], endTime[1])

        result.append([start, end, alpha, True])

def trainsInput(NA, NB):
    result = []
    trainInput(NA, result, 'A')
    trainInput(NB, result, 'B')

    result.sort()
    return result

def getStartTrains(L, T):
    S = {"A": 0, "B": 0}
    Ttime = timedelta(minutes=T)

    for i, trainTime in enumerate(L):
        if not trainTime[3]: continue
        trainTime[3] = False
        S[trainTime[2]] += 1

        checkTime = trainTime[1] + Ttime
        checkStation = trainTime[2]

        for j in range(i+1, len(L)):
            if L[j][3] and checkTime <= L[j][0] and checkStation != L[j][2]:
                L[j][3] = False
                checkTime = L[j][1] + Ttime
                checkStation = L[j][2]

    return [S["A"], S["B"]]

def case(caseID):
    T = int(sys.stdin.readline())
    [NA, NB] = list(map(int, sys.stdin.readline().strip().split()))
    L = trainsInput(NA, NB)
    [SA, SB] = getStartTrains(L, T)

    sys.stdout.write("Case #" + str(caseID) +": " + str(SA) + " " + str(SB) + "\n")
    

# 테스트 케이스 개수 N
N = int(sys.stdin.readline())

for i in range(1, N+1):
    case(i)