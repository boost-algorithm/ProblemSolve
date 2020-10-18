import sys
from itertools import combinations

[N, P, E] = map(int, sys.stdin.readline().split())

peoples = [i for i in range(N)]

combs = []
for comb in list(combinations(peoples, P)):
    combs.append(comb)

peopleDolls = []
for _ in range(N):
    data = sys.stdin.readline().split()
    peopleDolls.append({'min': int(data[0]), 'max': int(data[1])})

def f():
    global combs
    for comb in combs:
        result = [0 for _ in range(N)]
        total = 0
        for i in comb:
            total += peopleDolls[i]['min']
            result[i] = peopleDolls[i]['min']
        
        if total>E: continue
        elif total==E: return result
        
        # E-total은 남은 인형 개수
        for i in comb:
            remainTotalDoll = E - total
            remainCombDoll = peopleDolls[i]['max'] - peopleDolls[i]['min']
            
            if remainTotalDoll >= remainCombDoll:
                result[i] += remainCombDoll
                total += remainCombDoll
                remainTotalDoll -= remainCombDoll
            else:
                result[i] += remainTotalDoll
                total += remainTotalDoll
                remainTotalDoll = 0
                
            if remainTotalDoll==0: return result
    return [-1]

for i in f():
    sys.stdout.write(str(i) + ' ')