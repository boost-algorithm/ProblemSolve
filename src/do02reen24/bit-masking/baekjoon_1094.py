import sys

if __name__ == '__main__':
    x = int(sys.stdin.readline())
    stick = [64]
    stick_sum = 64
    while not x == stick_sum:
        half_stick = int(stick.pop() / 2)
        stick.append(half_stick)
        stick_sum = sum(stick)
        if stick_sum < x:
            stick.append(half_stick)
    print(len(stick))
