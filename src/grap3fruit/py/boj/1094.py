import sys 

target = int(sys.stdin.readline())

datas = [64]

def calc(datas):
	if sum(datas) > target:
		current_min = min(datas)
		datas.remove(current_min)
		datas.append(current_min/2)

		if sum(datas) == target:
			return len(datas)

		if sum(datas) > target:
			return calc(datas)

		if sum(datas) < target:
			datas.append(current_min/2)
			return calc(datas)

	if sum(datas) == target:
		return len(datas)

print(calc(datas))