import sys

if __name__ == '__main__':
    brackets = sys.stdin.readline().rstrip()
    stack = []
    result = 0
    for i in range(0, len(brackets)):
        if brackets[i] == '(' and brackets[i+1] == ')':
            if stack:
                stack[-1] += 1
        elif brackets[i] == '(':
            stack.append(0)
        elif not brackets[i-1] == '(':
            laser = stack.pop()
            result += laser + 1
            if stack:
                stack[-1] += laser
    print(result)