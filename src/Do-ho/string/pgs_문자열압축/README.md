# 문자열 압축

1. 아이디어

```python
for 1글자부터 전체 길이의 반까지 돌림:
	prev_str = 첫 글자 선언
	count = 1
	lastcount = 0
	
	for 글자 길이 단위로 움직임:
		target_str = 타겟 글자 선언
		
		if 앞 뒤 글자가 같다면:
			count += 1
			if 마지막 검사라면:
				lastcount = len(str(count)) + 글자 길이
		elif count가 1이라면:
			lastcount = 글자 길이
		else:
			# count가 2이상인데 마지막이 아닌 경우 이므로
			lastcount = len(str(count)) + 글자 길이
			
```



- 1차 시도 실패...

```
def solution(s):
    answer = 1000
    length = int(len(s) / 2) + 1
    
    for i in range(1, length):
        prev_str = s[0:i]
        count = 1
        lastcount = 0
        prev_j = 0
        for j in range(i, len(s)-i+1 ,i):
            target_str = s[j:(j+i)]
            print(j)
            print(target_str)
            if prev_str == target_str:
                count+= 1
                if count!=1 and j+i+i>=len(s)-i:
                    lastcount += len(str(count)) + i
                    
            elif count==1: lastcount += i
            else:
                lastcount += len(str(count)) + i
                count = 1
            prev_str = target_str
            prev_j = j
        # print(lastcount)
        # print(prev_j)
        if(prev_j != len(s)-i):
            print('ggggggg')
            lastcount += len(s)-prev_j
        # print(prev_j, lastcount)
        if lastcount < answer: answer = lastcount

    return answer
```

