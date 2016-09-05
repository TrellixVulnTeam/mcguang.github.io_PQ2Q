class Solution:
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



if __name__ == "__main__":
	S = Solution()
	result = S.strStr('source','urc')
	print(result)
