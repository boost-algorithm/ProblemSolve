def combineString(string, word, count):
    if not count == 1:
        string += str(count)
    string += word
    return string

def compression(string, length):
    compString = ''
    temp = string[:length]
    count = 0
    index = list(range(0, len(string), length))
    for i in index:
        now = string[i:i+length]
        if now == temp:
            count+=1
        else:
            compString = combineString(compString, temp, count)
            count = 1
            temp = now
        if i == index[-1]:
            compString = combineString(compString, temp, count)
    return len(compString)

def solution(s):
    answer = len(s)
    for length in range(1, int(len(s) / 2) + 1):
        result = compression(s, length)
        if answer > result:
            answer = result
    return answer

sList = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd"
]

for s in sList:
    print(solution(s))