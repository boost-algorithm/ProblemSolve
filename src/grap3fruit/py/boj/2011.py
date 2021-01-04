import sys
input = sys.stdin.readline().strip()
dp = [0]*5001

def calc(input, dp):
    if int(input[0]) == 0:  # 맨 앞이 0이면 return 0
        return 0

    dp[0] = 1

    if len(input) == 1:  # 맨 앞이 0이 아니고, 길이가 1이면 return 1
        return 1

    if int(input[1]) == 0:  # input[1]이 0인데 input[0]이 1,2면
        if int(input[0]) > 0 and int(input[0]) < 3:
            dp[1] = 1
        else:
            return 0

    if int(input[1]) != 0:  # input[1]이 0이 아니고,
        if (int(input[1]) < 7 and int(input[0]) == 2) or int(input[0]) == 1:  # 10 ~ 26 사이면
            dp[1] = 2
        else:
            dp[1] = 1

    if len(input) == 2:  # 입력이 두개면 return
        return dp[1]

    n = 2
    while n < len(input):  # dp[2] 부터 여기서 구함.
        if int(input[n]) > 0:  # input[n]이 0보다 클 경우는 input[n-1]에 그대로 붙여줄 수 있음.
            dp[n] = dp[n-1]

        # n,n-1이 10 ~ 26 사이면, dp[n-2]에 10~26을 붙일 수 있음.
        if (int(input[n]) < 7 and int(input[n-1]) == 2) or int(input[n-1]) == 1:
            dp[n] = (dp[n-2] + dp[n])

        n += 1

    return(dp[len(input)-1] % 1000000)


print(calc(input, dp))
