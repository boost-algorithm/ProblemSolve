import sys

def isValidInput(inputs):
    stack = []
    try:
        for char in inputs:
            if char == '(' or char == '[':
                stack.append(char)
                continue
            pre = stack.pop()
            if pre == '(' and char == ')':continue
            if pre == '[' and char == ']':continue
            return False
    except: return False
    if stack: return False
    return True
if __name__ == "__main__":
    inputs = str(sys.stdin.readline().strip())
    result = 0
    stack = []
    if not isValidInput(inputs):
        print(0)
        sys.exit(0)
    for char in inputs:
        if char == '(' or char == '[':
            stack.append(char)
            continue
        preValue = stack.pop()
        if char == ']':
            if preValue == '[':
                stack.append(3)
                continue
        elif char == ')':
            if preValue == '(':
                stack.append(2)
                continue
        while True:
            lastValue = stack.pop()
            if lastValue == '(':
                stack.append(preValue * 2)
                break
            elif lastValue == '[':
                stack.append(preValue * 3)
                break
            else:
                preValue += lastValue
    print(sum(stack))