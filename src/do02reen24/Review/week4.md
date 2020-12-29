# :fire: week4

## :ballot_box_with_check: 백준 19238

#### 틀렸습니다.

```python
import sys

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

class Passenger(object):
    def __init__(self, row, col, destRow, destCol):
        self.row = row
        self.col = col
        self.destRow = destRow
        self.destCol = destCol

def pickUpPassenger(board, row, col, n):
    newBoard = [[0]*n for _ in range(n)]
    queue = []
    count = 0
    queue.append([row, col])
    newBoard[row][col] = -1
    while queue:
        count += 1
        newQueue = []
        while queue:
            r, c = queue.pop()
            for i in range(0, 4):
                mr = r + dr[i]
                mc = c + dc[i]
                if mr >= 0 and mr < n and mc >=0 and mc < n:
                    if board[mr][mc] > 0:
                        return board[mr][mc] - 1, count
                    if not board[mr][mc] == -1 and newBoard[mr][mc] == 0:
                        newBoard[mr][mc] = count
                        newQueue.append([mr, mc])
        queue = newQueue
    return -1, -1

def goDestination(board, row, col, destRow, destCol, n):
    newBoard = [[0]*n for _ in range(n)]
    queue = []
    count = 0
    queue.append([row, col])
    newBoard[row][col] = -1
    while queue:
        count += 1
        newQueue = []
        while queue:
            r, c = queue.pop()
            for i in range(0, 4):
                mr = r + dr[i]
                mc = c + dc[i]
                if mr == destRow and mc == destCol:
                    return count
                if mr >= 0 and mr < n and mc >=0 and mc < n:
                    if board[mr][mc] == 0:
                        newBoard[mr][mc] = count
                        newQueue.append([mr, mc])
        queue = newQueue

def moveLocation(n):
    return int(n) - 1

def TaxiService():
    n, m, fuel = map(int, sys.stdin.readline().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, sys.stdin.readline().replace('1', '-1').split())))

    taxiRow, taxiCol = map(moveLocation, sys.stdin.readline().split())
    passengers = []
    for i in range(1, m+1):
        row, col, destRow, destCol = map(moveLocation, sys.stdin.readline().split())
        board[row][col] = i
        passengers.append(Passenger(row, col, destRow, destCol))
    while m > 0:
        if board[taxiRow][taxiCol] > 0:
            board[taxiRow][taxiCol] = 0
        else:
            index, count = pickUpPassenger(board, taxiRow, taxiCol, n)
            fuel -= count
            if fuel < 0 or count == -1:
                return -1
            taxiRow = passengers[index].row
            taxiCol = passengers[index].col
            board[taxiRow][taxiCol] = 0
            fee = goDestination(board, taxiRow, taxiCol, passengers[index].destRow, passengers[index].destCol, n)
            fuel -= fee
            if fuel < 0:
                return -1
            taxiRow = passengers[index].destRow
            taxiCol = passengers[index].destCol
            fuel += fee*2
        m -= 1
    return fuel

if __name__ == '__main__':
    print(TaxiService())
```
