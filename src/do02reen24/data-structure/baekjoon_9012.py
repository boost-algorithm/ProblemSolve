import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for _ in range(n):
        brackets = sys.stdin.readline().rstrip()
        result = 'YES'
        stack = []
        for bracket in brackets:
            if bracket == '(':
                stack.append('(')
            else:
                try:
                    stack.pop()
                except:
                    result = 'NO'
                    break
        if stack:
            result = 'NO'
        print(result)