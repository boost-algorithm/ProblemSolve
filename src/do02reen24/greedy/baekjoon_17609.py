import sys

def getPalindrome(word, length):
    index = 0
    while length - index > index:
        if word[index] == word[length - index]:
            index = index + 1
            continue
        return index
    return -1

def isPalindrome(word, length):
    index = getPalindrome(word, length)
    if index == -1: return 0
    
    deleteLeft = word[:index] + word[index+1:]
    if getPalindrome(deleteLeft, len(deleteLeft) - 1) == -1: return 1
    
    deleteRight = word[:length - index] + word[length - index+1:]
    if getPalindrome(deleteRight, len(deleteRight) - 1) == -1: return 1
    
    return 2

n = int(sys.stdin.readline())
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    print(isPalindrome(word, len(word) - 1))
