import heapq
import pdb

pdb.set_trace()
myList = [5, 2, 6, 12, 7, 3, 4, 9]
topNum = 3
nlargestList = heapq.nlargest(topNum, myList)
nsmallestList = heapq.nsmallest(topNum, myList)
print nlargestList
print nsmallestList 
