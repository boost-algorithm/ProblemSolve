import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    inputs = list(map(int, sys.stdin.readline().split()))
    position = list(range(1, n+1))
    balloons = [[inputs[i], position[i]] for i in range(0, n)]

    result = []
    index = 0
    while True:
        b = balloons.pop(index)
        result.append(b[1])
        length = len(balloons)
        if length == 0:
            break
        if b[0] > 0:
            index = (index + b[0] - 1) % length
        else:
            index = (index + b[0] + length) % length

    print(' '.join(map(str,result)))