import sys

board = []
blue = 0
white = 0

def checkBoard(startRow, endRow, startCol, endCol):
    check = board[startRow][startCol]
    for r in range(startRow, endRow):
        for c in range(startCol, endCol):
            if not check == board[r][c] : return False
    global blue
    global white
    if check == 1: blue = blue + 1
    elif check == 0: white = white + 1
    return True

def compress(n, startRow, startCol):
    n = int(n / 2)
    ans = []
    if checkBoard(startRow, startRow + n, startCol, startCol + n):
        ans.append(board[startRow][startCol])
    else:
        ans.append(compress(n, startRow, startCol))
    if checkBoard(startRow, startRow + n, startCol + n, startCol + n + n):
        ans.append(board[startRow][startCol + n])
    else:
        ans.append(compress(n, startRow, startCol + n))
    if checkBoard(startRow + n, startRow + n + n, startCol, startCol + n):
        ans.append(board[startRow + n][startCol])
    else:
        ans.append(compress(n, startRow + n, startCol))
    if checkBoard(startRow + n, startRow + n + n, startCol + n, startCol + n + n):
        ans.append(board[startRow + n][startCol + n])
    else:
        ans.append(compress(n, startRow + n, startCol + n))

def findSolution(N):
    if checkBoard(0, N, 0, N): return
    compress(N, 0, 0)

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    for _ in range(N):
        inputs = list(map(int, sys.stdin.readline().split(' ')))
        board.append(inputs)
    findSolution(N)
    print(white)
    print(blue)