import sys

def sol():
    n = int(sys.stdin.readline())
    score = []
    for _ in range(n):
        score.append(int(sys.stdin.readline()))

    if n <= 2: return sum(score)

    scoreSum = [score[0], score[0]+score[1], max(score[0],score[1])+score[2]]
    for i in range(3, n):
        scoreSum.append(score[i]+max(score[i-1]+scoreSum[i-3], scoreSum[i-2]))
    return scoreSum.pop()

print(sol())