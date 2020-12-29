import sys

def isPalindrome(word, start, end):
    index = 0
    while end - index > start + index:
        if word[end-index] == word[start+index]:
            index = index + 1
            continue
        return False
    return True


word = sys.stdin.readline().rstrip()
ans = len(word)
start, end = 0, len(word) - 1

while True:
    if isPalindrome(word, start, end): break
    ans = ans + 1
    start = start + 1

print(ans)
