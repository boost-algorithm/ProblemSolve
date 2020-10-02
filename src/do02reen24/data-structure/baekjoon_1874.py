import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline())
    stack = []
    count = 1
    result = []
    for _ in range(t):
        n = int(sys.stdin.readline())
        check = False
        while count <= t:
            if stack and stack[-1] == n:
                stack.pop()
                result.append('-')
                check = True
                break
            stack.append(count)
            result.append('+')
            count += 1
        if not check and stack:
            while stack:
                result.append('-')
                if n == stack.pop():
                    check = True
                    break
        if not check:
            print('NO')
            sys.exit(0)
    for r in result:
        print(r)