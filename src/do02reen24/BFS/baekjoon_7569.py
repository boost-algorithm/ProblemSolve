import sys

dh = [-1, 1, 0, 0, 0, 0]
dr = [0, 0, -1, 1, 0, 0]
dc = [0, 0, 0, 0, -1, 1]

def getDays():
    n, m, k = map(int, sys.stdin.readline().split())
    ans = 0
    boxes = []
    remain = 0
    tomatoes = []
    for height in range(0, k):
        box = []
        for row in range(0, m):
            t = list(map(int, sys.stdin.readline().split()))
            box.append(t)
            for col in range(0, len(t)):
                if t[col] == 0:
                    remain += 1
                elif t[col] == 1:
                    tomatoes.append((height, row, col))
        boxes.append(box)
    if remain == 0:
        return 0
    if not tomatoes:
        return -1
    newTomatoes = []
    while tomatoes:
        h, r, c = tomatoes.pop()
        for i in range(0, 6):
            mh = h + dh[i]
            mr = r + dr[i]
            mc = c + dc[i]
            if mh >=0 and mh < k and mr >=0 and mr < m and mc >=0 and mc < n:
                if boxes[mh][mr][mc] == 0:
                    boxes[mh][mr][mc] = 1
                    remain -= 1
                    newTomatoes.append((mh, mr, mc))
        if not tomatoes and newTomatoes:
            tomatoes = newTomatoes
            newTomatoes = []
            ans += 1
    if remain > 0:
        return -1
    return ans
if __name__ == '__main__':
    print(getDays())