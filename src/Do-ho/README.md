# :fire: Week1

## :question: 백준 1158번 문제 (요세푸스 순열)
- 처음 풀었던 방식
    ```python
        a, b = map(int, input().split())

        linked_list = []
        queue = []
        count = 1
        idx = 0

        for i in range(a):
            linked_list.append(str(i+1))

        while(len(linked_list)!=0):
            if(count==b):
                queue.append(linked_list[idx])
                linked_list.remove(linked_list[idx])
                count = 1
            else:
                count += 1
                idx = (idx + 1)%len(linked_list)

        print('<'+', '.join(queue)+'>')
    ```
    
    - 시간초과....
    - 따라서 카운트를 하나씩 올리는 것이 아닌 바로 올려서 검사해도 된다고 생각했음
    
- 두 번째 풀었던 방식

    ```python
    N, K = map(int, input().split())
    
    numArr = []
    queue = []
    idx = 0
    
    for i in range(N):
        numArr.append(str(i+1))
    
    while(len(numArr)!=0):
        idx = (idx + (K-1)) % len(numArr)
        popData = numArr.pop(idx)
        queue.append(popData)
    
    print('<'+', '.join(queue)+'>')
    ```



## :question: 백준 1406번 문제 (에디터)

- 커맨드에 따라서 함수를 나눠 구현해야 할 것 같다.
- 복잡도에 대한 부분을 개선하면 런타임 에러가 발생하지 않지 않을까...
- 아니면 hidden case가 있을까...?