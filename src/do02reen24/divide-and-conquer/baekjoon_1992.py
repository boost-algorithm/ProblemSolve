import sys

board = []

def checkBoard(startRow, endRow, startCol, endCol):
    check = board[startRow][startCol]
    for r in range(startRow, endRow):
        for c in range(startCol, endCol):
            if not check == board[r][c]: return False
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
    return '(' + ''.join(ans) + ')'

def findSolution(N):
    if checkBoard(0, N, 0, N):
        return board[0][0]
    ans = compress(N, 0, 0)
    return ans

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    for i in range(N):
        inputs = list(sys.stdin.readline().rstrip())
        board.append(inputs)
    print(findSolution(N))