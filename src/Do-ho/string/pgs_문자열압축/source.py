def solution(s):
    answer = 1000
    length = int(len(s) / 2) + 1
    
    for i in range(1, length):
        arr = []
        for j in range(0, len(s)-i+1 ,i):
            arr.append(s[j:(j+i)])
        
        # 아이템 중복 검사
        prev_item = arr[0]
        count = 0
        addcount = 0
        for idx, item in enumerate(arr):
            if prev_item == item:
                print(prev_item, item)
                count += 1
                if(idx==len(arr)-1):
                    addcount += len(str(count)) + i
            elif count==1:
                addcount += i
                print(prev_item, item)
            else:
                print(prev_item, item)
                addcount += len(str(count)) + i
                count = 1
            prev_item = item
        
        print(i, addcount)
        # 스트링 끝까지 검사 안했을 때
        if(len(arr)*i!=len(s)):
            addcount += len(s) - (len(arr)*i)
        print(i, addcount)
        
        if addcount < answer: answer = addcount
    return answer