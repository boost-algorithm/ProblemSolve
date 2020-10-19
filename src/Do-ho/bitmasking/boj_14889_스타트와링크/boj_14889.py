import sys
from itertools import combinations

def getTeamStats(comb):
    startTeamStat = getStat(comb)
    
    linkTeam = []
    for people in peoples:
        if people not in comb:
            linkTeam.append(people)

    linkTeamStat = getStat(linkTeam)

    return [startTeamStat, linkTeamStat]

def getStat(peoples):
    result = 0
    for item1 in peoples:
        for item2 in peoples:
            if item1==item2: continue
            result += stats[item1][item2]
    
    return result

N = int(sys.stdin.readline())
halfN = N//2
stats = []
peoples = [i for i in range(N)]
team_combinations = []
balanceStat = 10000

for _ in range(N):
    stats.append(list(map(int, sys.stdin.readline().split())))

for team in list(combinations(peoples, halfN)):
    team_combinations.append(team)

for comb in team_combinations:
    [startTeamStat, linkTeamStat] = getTeamStats(comb)
    if balanceStat > abs(startTeamStat - linkTeamStat):
        balanceStat = abs(startTeamStat - linkTeamStat)

sys.stdout.write(str(balanceStat))