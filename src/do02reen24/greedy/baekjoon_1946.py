import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        applicant = []        
        for i in range(n):
            rankA, rankB = map(int, sys.stdin.readline().split(' '))
            applicant.append([rankA, rankB])
        applicant.sort(key = lambda rank: rank[0])

        minB = applicant[0][1]
        ans = 0
        for rankA, rankB in applicant:
            if rankB <= minB:
                minB = rankB
                ans += 1
        print(ans)