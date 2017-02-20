import heapq

myDict = {1:'a', 3:'d', 8:'g', 5:'m', 9:'t', 4:'s', 2:'u'}
topNum = 3
nlargestList = heapq.nlargest(topNum, myDict.keys())
nsmallestList = heapq.nsmallest(topNum, myDict.keys())

for key in nlargestList:
	print key,myDict[key]

for key in nsmallestList:
	print key,myDict[key]
