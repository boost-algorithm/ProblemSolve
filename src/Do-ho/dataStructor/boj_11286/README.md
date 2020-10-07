

## 우선 순위 큐

1. PriorityQueue를 이용한 방법

   ```python
   import sys
   from queue import PriorityQueue
   
   que = PriorityQueue()
   
   N = int(sys.stdin.readline())
   
   for i in range(N):
       x = int(sys.stdin.readline())
       if(x!=0): que.put((abs(x), x))
       else:
           if que.empty(): print(0)
           else: print(que.get()[1])
   ```

2. heapq를 이용한 방법

   ```python
   import sys
   import heapq
   
   N = int(input())
   heap = []
   
   for i in range(N):
       x = int(sys.stdin.readline())
       if(x!=0): heapq.heappush(heap, (abs(x), x))
       else:
           if len(heap)==0: print(0)
           else: print(heapq.heappop(heap)[1])
   ```



## 알게된 점

- input()과 sys.stdin.readline의 속도 차이 [참조](https://www.acmicpc.net/blog/view/56)

  - N(=10,000,000), 자연수(10,000 이하)가 적힌 파일을 입력받는데 걸리는 시간을 측정

  - input()은 12.4443초

  - int(sys.stdin.readline())은 4.4394초

  - 제일 빠른건 map(int,os.read(0, 100000000).decode('utf-8').split('\n'))

  - 하지만 0.03초 차이밖에 나지 않음

    

## 참조

[참조](https://www.youtube.com/watch?v=jfwjyJvbbBI)