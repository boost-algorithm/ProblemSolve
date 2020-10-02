# 스타트 택시

- 맵에다가 해당 사람을 표현

- 1은 벽, 2와 -2를 동시에 표현해 시작점과 도착점을 표기

  - 이렇게 할 경우 겹칠 위험이 있을듯
  - 따라서 맵에 넣고 비교하는 것도 좋을듯

- 길 찾기 알고리즘으로 bfs를 채택

  - 모든 맵을 찾지 않고 중간에 break 가능할까?

    ```python
    def bfs(graph, start):
        visited = []
        queue = [start]
    
        while queue:
            n = queue.pop(0)
            if n not in visited:
                visited.append(n)
                if n in graph:
                    queue += sorted(graph[n] - set(visited))
        return visited
    ```

    - 재귀 구조가 아니라서 가능할 것 같음!
    - 어디로 움직일 지에 대한 설계가 필요

  - 

