

def remove_element(array, remove_num):
	n = len(array)
	result = []
	for i in range(n):
		if array[i] != remove_num:
			result.append(array[i])
	return len(result),result

if __name__ == "__main__":
	print remove_element([0,4,4,0,0,2,4,4], 2)

