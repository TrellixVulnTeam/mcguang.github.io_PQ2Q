
def zero_sum_array(array):
	n = len(array)
	result = []
	for i in range(n):
		for j in range(i,n):
			if sum(array[i:j+1]) == 0:
				result.append([i, j])
	return result

if __name__ == "__main__":
	print zero_sum_array([-3, 1, 2, -3, 4])


