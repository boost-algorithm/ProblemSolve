import sys
import heapq

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    absHeap = []
    for i in range(n):
        command = int(sys.stdin.readline())
        if command == 0:
            try:
                print(heapq.heappop(absHeap)[1])
            except:
                print(0)
        else:
            heapq.heappush(absHeap, (abs(command), command))