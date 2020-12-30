import sys

def isAlpha(n):
    return int(n)>=1 and int(n)<=26

def isDivision(n):
    return int(n)>10 and int(n)<=26 and int(n)!=20

def validation(n):
    if(n[0]=='0'): return False
    prev = n[0]
    for i in range(1, len(n)):
        if(n[i]=='0' and (prev != '1' and prev != '2')): return False
        prev = n[i]
    return True
            
def decode(N):
    L = len(N) + 1
    D = [0 for _ in range(L)]
    if(not validation(N)): return 0
    D[0] = 1
    
    if(isDivision(N[:2])): D[1] = 2
    else: D[1] = 1
    
    if(L > 2): prev = N[1]

    for i in range(2, len(N)):
        target = N[i]
        word = prev + target
        if(word=='10' or word=='20'): D[i] = D[i-2]
        elif(not isAlpha(word)): D[i] = D[i-1]
        elif(prev == '0'): D[i] = D[i-2]
        elif(target == '0'): D[i] = D[i-2]
        else: D[i] = D[i-1] + D[i-2]
        prev = N[i]
    print(D)
    return D[L-2] % 1000000

N = sys.stdin.readline().strip()
print(decode(N))