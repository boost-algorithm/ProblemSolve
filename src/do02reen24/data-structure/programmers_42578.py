def solution(clothes):
    answer = 1
    clothesMap = dict()
    for c in clothes:
        if clothesMap.get(c[1]) == None:
            clothesMap[c[1]] = []
        clothesMap[c[1]].append(c[0])

    for value in clothesMap.values():
        answer *= (len(value) + 1)

    answer -= 1
    return answer