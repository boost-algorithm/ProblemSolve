import sys

if __name__ == '__main__':
    stackLeft = list(sys.stdin.readline().rstrip())
    stackRight = list()
    
    n = int(sys.stdin.readline().rstrip())
    for i in range(0, n):
        command = list(sys.stdin.readline().split())
        if command[0] == 'L' and stackLeft:
            stackRight.append(stackLeft.pop())
        elif command[0] == 'D' and stackRight:
            stackLeft.append(stackRight.pop())
        elif command[0] == 'B' and stackLeft:
            stackLeft.pop()
        elif command[0] == 'P':
            stackLeft.append(command[1])

    print(''.join(stackLeft) + ''.join(list(reversed(stackRight))))