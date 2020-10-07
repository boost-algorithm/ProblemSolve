def solution(clothes):
    answer = 1
    hash = {}
    for item in clothes:
        try: hash[item[1]] += 1
        except: hash[item[1]] = 1 + 1
    
    for val in list(hash.values()): answer *= val
    
    return answer - 1