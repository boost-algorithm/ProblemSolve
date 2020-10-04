def is_same_arr(a,b):
	if len(a) != len(b):
		return False

	for i in range(len(a)):
		if a[i] != b[i]:
			return False
	return True

def compare(s, compare_length):
	cursor = 0
	compress = 0
	compress_time = 0
	result_arr = []
	
	while cursor < len(s):
		ref_arr = s[cursor:cursor+compare_length]
		compare_arr = s[cursor+compare_length:cursor+compare_length+compare_length]

		if len(compare_arr) == 0 :
			result_arr.append([compress_time+1, len(s)-cursor])
			break

		if is_same_arr(ref_arr, compare_arr):
			compress = compare_length
			compress_time += 1

		if not is_same_arr(ref_arr, compare_arr) :
			if compress_time == 0 :
				result_arr.append([compress_time+1, compare_length])
			else :
				result_arr.append([compress_time+1, compress])

			compress = 0
			compress_time = 0

		cursor += compare_length

	return result_arr

s = "xababcdcdababcdcd"
s = "abcabcabcabcdededededede"
# s = "abcabcdede"
# s = "aabbaccc"
# s = "a"
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#s = "aaaaa"
max_value = [0,0]
compare_lengths = int((len(s) - 0)/2)
min_result = 1001
if compare_lengths == 0:
  min_result = 1 
for compare_length in range(compare_lengths+1):
	if compare_length == 0 :
		continue

	result = 0
	result_arr = compare(s,compare_length)
	print("result_arr: ",result_arr)
	for e in result_arr:
		if e[0] == 1 :
			result += e[1]

		elif e[0] != 1 :
			result += e[1]+len(str(e[0]))

	print("result: ", result)
	if result < min_result:
		min_result = result

print(min_result)

start_idx = 0
result = 0
