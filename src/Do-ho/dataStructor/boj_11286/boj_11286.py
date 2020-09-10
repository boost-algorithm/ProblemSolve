import math
import sys

heap = []

def swap(parentIdx, childIdx):
    global heap
    tmp = heap[parentIdx]
    heap[parentIdx] = heap[childIdx]
    heap[childIdx] = tmp

def reheapdown():
    global heap
    parentIdx = 0
    
    leftChildIdx = 1
    rightChildIdx = 2
    while True:
        if parentIdx == 0 and leftChildIdx < len(heap) and rightChildIdx < len(heap):
            if abs(heap[leftChildIdx]) <= abs(heap[rightChildIdx]):
                if leftChildIdx < len(heap) and abs(heap[leftChildIdx]) <= abs(heap[parentIdx]):
                    if abs(heap[leftChildIdx]) == abs(heap[parentIdx]) and heap[leftChildIdx] >= heap[parentIdx]: return
                    swap(parentIdx, leftChildIdx)
                    parentIdx = leftChildIdx
                elif rightChildIdx < len(heap) and abs(heap[rightChildIdx]) <= abs(heap[parentIdx]):
                    if abs(heap[rightChildIdx]) == abs(heap[parentIdx]) and heap[rightChildIdx] >= heap[parentIdx]: return
                    swap(parentIdx, rightChildIdx)
                    parentIdx = rightChildIdx
                else:
                    break
            else:
                if rightChildIdx < len(heap) and abs(heap[rightChildIdx]) <= abs(heap[parentIdx]):
                    if abs(heap[rightChildIdx]) == abs(heap[parentIdx]) and heap[rightChildIdx] >= heap[parentIdx]: return
                    swap(parentIdx, rightChildIdx)
                    parentIdx = rightChildIdx
            
                elif leftChildIdx < len(heap) and abs(heap[leftChildIdx]) <= abs(heap[parentIdx]):
                    if abs(heap[leftChildIdx]) == abs(heap[parentIdx]) and heap[leftChildIdx] >= heap[parentIdx]: return
                    swap(parentIdx, leftChildIdx)
                    parentIdx = leftChildIdx
                else:
                    break
        else:
            if leftChildIdx < len(heap) and abs(heap[leftChildIdx]) <= abs(heap[parentIdx]):
                if abs(heap[leftChildIdx]) == abs(heap[parentIdx]) and heap[leftChildIdx] >= heap[parentIdx]: return
                swap(parentIdx, leftChildIdx)
                parentIdx = leftChildIdx
            elif rightChildIdx < len(heap) and abs(heap[rightChildIdx]) <= abs(heap[parentIdx]):
                if abs(heap[rightChildIdx]) == abs(heap[parentIdx]) and heap[rightChildIdx] >= heap[parentIdx]: return
                swap(parentIdx, rightChildIdx)
                parentIdx = rightChildIdx
            else:
                break
        leftChildIdx = parentIdx * 2 + 1
        rightChildIdx = parentIdx * 2 + 2
    

def reheapup(childIdx):
    global heap
    if childIdx == 0: return
    parentIdx = math.floor((childIdx + 1) / 2) - 1
    while abs(heap[parentIdx]) >= abs(heap[childIdx]):
        if childIdx == 0: return
        if abs(heap[childIdx]) == abs(heap[parentIdx]) and heap[childIdx] >= heap[parentIdx]: return
        swap(parentIdx, childIdx)
        childIdx = parentIdx
        parentIdx = math.floor(childIdx/2)

def insert(input):
    global heap
    heap.append(input)
    reheapup(len(heap)-1)

def popMin():
    global heap
    if(len(heap)==0):
        print(0)
        return
    if(len(heap)==1):
        print(heap.pop())
        return
    output = heap[0]
    heap[0] = heap.pop()
    reheapdown()
    print(output)

N = int(sys.stdin.readline())

for i in range(N):
    inputNumber = int(sys.stdin.readline())
    if(inputNumber == 0): popMin()
    else: insert(inputNumber)