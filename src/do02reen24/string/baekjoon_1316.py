import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    count = 0
    for _ in range(n):
        word = sys.stdin.readline().rstrip()
        check = {}
        before = word[0]
        for w in word:
            if check.get(w) == None:
                check[w] = True
                before = w
            elif before == w:
                continue
            else:
                count -= 1
                break
        count += 1
    print(count)