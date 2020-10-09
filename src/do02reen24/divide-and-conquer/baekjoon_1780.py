import sys

board = []

minus = 0
zero = 0
plus = 0

def checkBoard(startRow, endRow, startCol, endCol):
    check = board[startRow][startCol]
    for r in range(startRow, endRow):
        for c in range(startCol, endCol):
            if not check == board[r][c]: return False
    global minus
    global zero
    global plus
    if check == -1: minus += 1
    elif check == 0: zero += 1
    elif check == 1: plus += 1
    return True

def makeRange(n):
    return[[0,0],[0,n],[0,2*n],[n,0],[n,n],[n,2*n],[2*n,0],[2*n,n],[2*n,2*n]]

def compress(n, startRow, startCol):
    n = int(n / 3)
    ranges = makeRange(n)
    for r, c in ranges:
        if not checkBoard(startRow + r, startRow + r + n, startCol + c, startCol + c + n): compress(n, startRow + r, startCol + c)

def findSolution(n):
    if checkBoard(0, n, 0, n): return
    compress(n, 0, 0)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for _ in range(0, n):
        inputs = list(map(int, sys.stdin.readline().split(' ')))
        board.append(inputs)
    findSolution(n)
    print(minus)
    print(zero)
    print(plus)