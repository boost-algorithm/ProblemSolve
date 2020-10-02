import sys

if __name__ == '__main__':
    ans = 0
    n = int(sys.stdin.readline())
    t = int(sys.stdin.readline())
    network = {}
    for _ in range(t):
        n1, n2 = map(int, sys.stdin.readline().split())
        if network.get(n1) == None:
            network[n1] = []
        network[n1].append(n2)
        if network.get(n2) == None:
            network[n2] = []
        network[n2].append(n1)
    visit = [False] * (n + 1)
    queue = []
    queue.append(1)
    visit[1] = True
    while queue:
        index = queue.pop()
        check = network[index]
        while check:
            com = check.pop()
            if visit[com] == False:
                queue.append(com)
                visit[com] = True
                ans += 1
    print(ans)