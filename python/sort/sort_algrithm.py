# By Albert in 2017-2-20

import pdb

"""
Implimentions of different sort algrithm
reference visualgo.net
"""
def swap(data, left, right):
	"""
	swap two element in a array(data)
	"""
	tmp = data[left]
	data[left] = data[right]
	data[right] = tmp
	

def bubbleSort(data = []):
	"""
	Bubble Sort
	exchange the nearest two element by compare it
	"""
	length = len(data)
	swapCounter = 0
	left = 0
	swapped = True
	loop = 0
	while swapped:
		swapped = False
		for i in range(length - 1 - loop):
			if data[i] > data[i + 1]:
				swap(data, i, i + 1)
				swapped = True
				swapCounter += 1
		loop += 1
	return data

def bubble_sort(lists):
	count = len(lists)
	for i in range(0, count):
		for j in range(i + 1, count):
			if lists[i] > lists[j]:
				lists[i],lists[j] = lists[j],lists[i]
	return lists

def selectSort(data = []):
	"""
	chose the minimun element, and exchange with the left unsorted element 
	"""
	length = len(data)
	for i in range(length - 1):
		minIndex = i
		for j in range(i,length):
			if data[j] < data[minIndex]:
				minIndex = j
		swap(data, i, minIndex)
	return data

def select_sort(lists):
	count = len(lists)
	for i in range(0, count):
		min = i
		for j in range(i + 1, count):
			if lists[min] > lists[j]:
				min = j
		lists[min], lists[i] = lists[i], lists[min]
	return lists

def insertSort(data = []):
	"""
	insert an element in the previous sorted sub-array
	"""
	length = len(data)
	for i in range(1, length):
		tmp_element = data[i]
		data[i] = -100
		tmp_index = i
		for j in range(i-1,-1,-1):
			if data[j] > tmp_element and j > 0:
				data[tmp_index] = data[j]
				tmp_index -= 1
			elif data[j] > tmp_element and j == 0:
				data[tmp_index] = data[j]
				data[j] = tmp_element
			else: 
				data[tmp_index] = tmp_element
				break

	return data
def insert_sort(lists):
	count = len(lists)
	for i in range(1, count):
		key = lists[i]
		j = i - 1
		while j >= 0:
			if lists[j] > key:
				lists[j+1] = lists[j]
				lists[j] = key
			j -= 1
	return lists 



if __name__ == '__main__':
	data = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
	#print("Bubble sort result is %s" % bubbleSort(data))
	#print("Select sort result is %s" % selectSort(data))
	print("Insert sort result is %s" % insertSort(data))
