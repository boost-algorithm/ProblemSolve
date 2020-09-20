import sys

N = int(sys.stdin.readline())

def checkString(string):
    check_arr = {}
    prev_char = string[0]

    for ch in string:
        try:
            if not check_arr[ch]: return False
        except:
            check_arr[ch] = True
        check_arr[prev_char] = False
        check_arr[ch] = True
        prev_char = ch
        
    return True

result = 0

for i in range(N):
    string = sys.stdin.readline().replace('\n', '')
    if checkString(string): result += 1

print(result)