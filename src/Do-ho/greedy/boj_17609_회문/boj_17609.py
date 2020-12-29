import sys

def isPalindrome(S):
    mid = int(len(S) / 2)
    for i in range(mid):
        if (S[i] != S[len(S)-1-i]): return False
    return True

def isPseudoPalindrome(S):
    mid = int(len(S) / 2)
    for i in range(mid):
        if (S[i] != S[len(S)-1-i]):
            FrontStr = S[:i] + S[i+1:]
            BackStr = S[:len(S)-1-i] + S[len(S)-i:]
            if(isPalindrome(FrontStr) or isPalindrome(BackStr)): return True
            return False
    return True

def palindrome(S):
    if(isPalindrome(S)): return '0'
    elif(isPseudoPalindrome(S)): return '1'
    return '2'

if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        S = sys.stdin.readline().strip()
        sys.stdout.write(palindrome(S) + '\n')