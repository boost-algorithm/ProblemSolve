import sys

def palindrome(S):
    return S == S[::-1]

S = sys.stdin.readline().strip()
S_reverse = S[::-1]

max_palindrome = 0
for i in range(len(S_reverse)):
    checkString = S_reverse[0:i+1]
    if palindrome(checkString): max_palindrome = len(checkString)

print(len(S)*2 - max_palindrome)