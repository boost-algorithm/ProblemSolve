import itertools

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"], ["bluen_turban", "headgear"], ["blue_sung1", "eyewear"], ["blue1g1", "shoes"], ["blue_1", "shoes"]]

answer = 0
bucket = {}

for cloth in clothes:
	cloth_type = cloth[1]
	if not cloth_type in bucket :
		bucket[cloth_type] = 1
	
	elif cloth_type in bucket :
		bucket[cloth_type] += 1

arr = list(bucket.values())

result = 0
for i in range(1, len(arr)+1):
	nCr = itertools.combinations(arr, i)
	calc_arr = list(nCr)
	print(calc_arr)
	for j in range(0, len(calc_arr)):
		multi = 1
		for el in calc_arr[j] :
			multi *= el
		
		result += multi

print(result)
