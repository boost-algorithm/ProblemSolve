import sys

def decodeNum():
    word = sys.stdin.readline().rstrip()
    length = len(word)
    if word[0] == '0': return 0
    sol = [1] * (length + 1)
    for i in range(1, length):
        prev = int(word[i-1]+word[i])
        now = int(word[i])
        if prev == 10 or prev == 20:
            sol[i+1] = sol[i-1]
        elif 11 <= prev and prev <= 26:
            sol[i+1] = (sol[i] + sol[i-1]) % 1000000
        elif 1 <= now and now <= 9:
            sol[i+1] = sol[i]
        else: return 0
    return sol[length]

print(int(decodeNum()))
