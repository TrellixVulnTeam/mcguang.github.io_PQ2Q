class Solution_1:
	"""
	@param strs: a string with several wards.
	@return: reverse string
	"""
	def reverseWords(self, strs):
		splitList = strs.split()
		reverseList = splitList[::-1]
		list2str = " ".join(reverseList)
		return list2str


class Solution_2:
	"""
	@param s: a string
	@return: boolean. whether the string is a valid palindrome
	"""
	def isPalindrome(self, s):
		if not s:
			return True

		l, r = 0, len(s) -1

		while l < r:
			# find left alphanumeric character
			if not s[l].isalnum():
				l += 1
				continue

			# find right alphanumeric character
			if not s[r].isalnum():
				r -= 1
				continue
			# case insensitive compare
			if s[l].lower() == s[r].lower():
				l += 1
				r -= 1
			else:
				return False

		return True


if __name__ == "__main__":
	 S_1 = Solution_1()
	 print(S_1.reverseWords('the sky is blue'))
	 
	 S_2 = Solution_2()
	 print(S_2.isPalindrome('A man a plan a canal: panama'))
