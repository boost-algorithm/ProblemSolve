import sys

def getIntTime(time):
    h = int(time[0:2]) * 60
    m = int(time[3:5])
    return h + m

def changeInt(start, end, time):
    return [getIntTime(start), getIntTime(end) + time]

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for i in range(t):
        time = int(sys.stdin.readline())
        na, nb = map(int, sys.stdin.readline().split(' '))
        a_list, b_list = [], []
        for _ in range(na):
            start , end = map(str, sys.stdin.readline().rstrip().split(' '))
            a_list.append(changeInt(start, end, time))
        for _ in range(nb):
            start , end = map(str, sys.stdin.readline().rstrip().split(' '))
            b_list.append(changeInt(start, end, time))
        a_list.sort()
        b_list.sort()
        
        sol_A, sol_B = 0, 0
        a_train, b_train = [], []
        
        while True:
            train_type = None
            train = None
            if a_list and b_list:
                if a_list[0] < b_list[0]: train_type = 'a'
                else: train_type = 'b'
            elif a_list: train_type = 'a'
            elif b_list: train_type = 'b'
            else: break

            if train_type == 'a':
                start, end = a_list.pop(0)
                if a_train and a_train[0] <= start:
                    a_train.pop(0)
                else: sol_A += 1
                b_train.append(end)
                b_train.sort()
            if train_type == 'b':
                start, end = b_list.pop(0)
                if b_train and b_train[0] <= start:
                    b_train.pop(0)
                else: sol_B += 1
                a_train.append(end)
                a_train.sort()

        print("Case #"+str(i+1)+":",sol_A,sol_B)