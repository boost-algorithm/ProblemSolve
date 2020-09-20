import sys

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    permutation = list(range(1, n + 1))
    answer = []
    index = 0

    while len(permutation):
        index = (index + k - 1) % len(permutation)
        answer.append(permutation.pop(index))
    print("<"+', '.join(map(str, answer))+">")