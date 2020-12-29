# 회문

### 시간초과...

```
import sys

def isPalindrome(S):
    return S == S[::-1]

def isPseudoPalindrome(S):
    for i in range(len(S)):
        if(isPalindrome(S[:i] + S[i+1:])): return True
    return False

def palindrome(S):
    if(isPalindrome(S)): return '0'
    elif(isPseudoPalindrome(S)): return '1'
    return '2'

T = int(sys.stdin.readline())

for _ in range(T):
    S = sys.stdin.readline().strip()
    sys.stdout.write(palindrome(S) + '\n')
```

### 시간초과 2..

```
import sys

def isPalindrome(S):
    mid = int(len(S) / 2)
    for i in range(mid):
        if (S[i] != S[len(S)-1-i]): return False
    return True

def isPseudoPalindrome(S):
    for i in range(len(S)):
        if(isPalindrome(S[:i] + S[i+1:])): return True
    return False

def palindrome(S):
    if(isPalindrome(S)): return '0'
    elif(isPseudoPalindrome(S)): return '1'
    return '2'

T = int(sys.stdin.readline())

for _ in range(T):
    S = sys.stdin.readline().strip()

    sys.stdout.write(palindrome(S) + '\n')
```

### 성공

```
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
```

