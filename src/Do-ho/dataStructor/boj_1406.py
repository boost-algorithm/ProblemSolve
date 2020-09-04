initString = input()
M = int(input())
cursor = len(initString)

def process(command):
    global initString
    if len(command)==1:
        singleCommand(command[0])
    else:
        commandP(command[1])

def singleCommand(command):
    if command == 'L' :
        commandL()
    elif command == 'D':
        commandD()
    elif command == 'B':
        commandB()

def commandP(ch):
    global initString, cursor, M
    if cursor == len(initString):
        initString = initString + ch
    else:
        initString = initString[:cursor] + ch + initString[cursor:]
    M += 1
    cursor += 1

def commandL():
    global cursor
    if cursor==0:
        return
    cursor -= 1

def commandD():
    global cursor
    if cursor==0:
        return
    cursor += 1

def commandB():
    global cursor, initString
    if cursor==0:
        return
    elif cursor==len(initString):
        initString = initString[:cursor-1]
        cursor -= 1
    else:
        initString = initString[:cursor-1] + initString[cursor:]
        cursor -= 1

for i in range(M):
    inputString = input()
    command = inputString.split(' ')
    process(command)

print(initString)

