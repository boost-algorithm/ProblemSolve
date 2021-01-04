import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
data = [[0]*(M+2)]
for _ in range(N):
    input_arr = '0' + str(sys.stdin.readline().strip().split()[0]) + '0'
    splited_arr = [int(i) for i in input_arr]
    data.append(splited_arr)

data.append([0]*(M+2))
print(N, M, data)


def bfs(init, N, M, data):
    global count
    global visited
    global queue

    queue.append(init)
    while queue:
        q_size = len(queue)

        for _ in range(q_size):
            el = queue.popleft()
            Y = el[0]
            X = el[1]
            if el not in visited and data[Y][X] == 1:
                visited.append(el)
                print(el)

                if X == M and Y == N:
                    print("도착")
                    print(visited)
                    print(count)
                    break

                right = [Y, X+1]
                down = [Y+1, X]
                left = [Y, X-1]
                up = [Y-1, X]

                for pos in [right, down, left, up]:
                    if data[pos[0]][pos[1]] != 0:
                        queue.append(pos)
        count += 1


count = 1
visited = []
queue = deque([])


def calc(N, M, data):
    global count
    global visited
    init = [1, 1]
    bfs(init, N, M, data)


calc(N, M, data)
