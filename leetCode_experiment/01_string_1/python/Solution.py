import collections

class Solution_1:
	def strStr(self, source, target):
		if source is None or target is None:
			return -1

		for i in range(len(source) - len(target) + 1):
			for j in range(len(target)):
				if source[i+j] != target[j]:
					break

			else: # no break
				return i
		return -1


class Solution_2:
	"""
	@param s: The first string
	@param t: The second string 
	@return true or false
	"""
	
	def anagram(self, s, t):
		return collections.Counter(s) == collections.Counter(t)


class Solution_3:
	"""
	@param s: The first string
	@param t: The second string 
	@return true or false
	"""
	
	def anagram(self, s, t):
		return sorted(s) == sorted(t)

class Solution_4:
	"""	
	"""
	
	def compare_strings(self, A, B):
		#return a dict with defalut value set to 0
		letters = collections.defaultdict(int)
		for a in A:
			letters[a] += 1

		for b in B:
			if b not in letters:
				return False
			if letters[b] <= 0:
				return False
			else:
				letters[b] -= 1
		return True

class Solution_5:
	"""
	@param strs: A list of strings
	@return: A list of strings 
	"""
	def anagrams(self, strs):
		if len(strs) < 2:
				return strs
		result = []
		visited = [False] * len(strs)
		for index1,s1 in enumerate(strs):
			hasAnagrams = False
			for index2,s2 in enumerate(strs):
				if index2 > index1 and not visited[index2] and self.isAnagrams(s1,s2):
					result.append(s2)
					visited[index2] = True
					hasAnagrams = True
			if not visited[index1] and hasAnagrams:
				result.append(s1)
		return result

	def isAnagrams(self, str1, str2):
		if sorted(str1) == sorted(str2):
			return True
		return False


class Solution_6:
	"""
	@param strs: A list of strings
	@return: A list of strings
	"""
	def anagrams(self, strs):
		strDict = {}
		result = []
		for string in strs:
			if "".join(sorted(string)) not in strDict.keys():
				strDict["".join(sorted(string))] = 1
			else:
				strDict["".join(sorted(string))] += 1
		for string in strs:
			if strDict["".join(sorted(string))] > 1:
				result.append(string)
		return result

class Solution_7:
	"""
	@param A: A string
	@param offset: Rotate string with offset.
	@return: Rotated string
	"""
	def rotateString(self, A, offset):
		if A is None or len(A) == 0:
			return A

		offset %= len(A)
		before = A[:len(A) - offset]
		after = A[len(A) - offset:]
		#[::-1] means reverse in Python
		A = before[::-1] + after[::-1]
		A = A[::-1]

		return A



			
if __name__ == "__main__":
	S_1 = Solution_1()
	result_1 = S_1.strStr('source','urc')
	print(result_1)

	S_2 = Solution_2()
	result_2 = S_2.anagram('abcde','deacb')
	print(result_2)

	S_3 = Solution_3()
	result_3 = S_3.anagram('abcde','decab')
	print(result_3)

	S_4 = Solution_4()
	result_4 = S_4.compare_strings('ABCD','AABC')
	print(result_4)
	
	S_5 = Solution_5()
	result_5 = S_5.anagrams(["aaa","abc","acb","cba","aaa","cda"])
	print(result_5)	
	
	S_6 = Solution_5()
	result_6 = S_6.anagrams(["aaa","abc","acb","cba","aaa","cda"])
	print(result_6)	
	
	S_7 = Solution_7()
	result_7 = S_7.rotateString('abcdefg',3)
	print(result_7)
