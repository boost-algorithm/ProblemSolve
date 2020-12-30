import sys
from itertools import combinations

def rubberDuck():
    n, p, e = map(int, sys.stdin.readline().rstrip().split())
    member = []
    for _ in range(n):
        minDuck, maxDuck = map(int, sys.stdin.readline().rstrip().split())
        member.append([minDuck, (maxDuck-minDuck)])
    user = [i for i in range(n)]
    combList = list(combinations(user, p))
    
    for comb in combList:
        sol = [0] * n
        remain = e
        for i in comb:
            sol[i] = member[i][0]
            remain -= member[i][0]
        if remain < 0: continue
        for i in comb:
            if remain > member[i][1]:
                sol[i] += member[i][1]
                remain -= member[i][1]
            else:
                sol[i] += remain
                remain = 0
                break
        if remain == 0:
            return ' '.join(map(str,sol))
    return -1
print(rubberDuck())
