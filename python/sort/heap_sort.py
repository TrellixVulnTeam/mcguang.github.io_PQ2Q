
def parent(i):
	"""
	Floor(i/2) 
	"""
	return i/2

def left(i):
	return 2*i

def right(i):
	return 2*i+1

def max_heapify(A, i):
	l = left(i)
	r = right(i)
	heap_size = len(A)
	if l <= heap_size and A[l] > A[i]:
		largest = l
	else:
		largest = i
	if r <= heap_size and A[r] > A[largest]:
		largest = r
	if largest != i:
		A[i], A[largest] = A[largest], A[i]
		max_heapify(A, largest)



def max_heapify_loop(A, i):
	heap_size = len(A)
	while True:
		l = left(i)
		r = right(i)
		if l<= heap_size and A[l] > A[i]:
			largest = l
		else:
			largest = i
		if r <= heap_size and A[r] > A[largest]:
			largest = r
		if largest != i:
			A[i], A[largest] = A[largest], A[i]
			i = largest
		else:
			break

def build_max_heap(A):
	heap_size = len(A)
	for i in range(heap_size/2,0,-1):
		max_heapify(A,i)


