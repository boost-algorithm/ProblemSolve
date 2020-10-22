import sys

T = int(sys.stdin.readline())

for _ in range(T):
    employees = []
    N = int(sys.stdin.readline())
    for _ in range(N):
        employees.append(list(map(int, sys.stdin.readline().split())))
    employees.sort()

    testEmployee = employees[0]
    count = 1
    for employee in employees:
        if testEmployee[1] > employee[1]:
            count += 1
            testEmployee = employee
    print(count)