#!/bin/python
'''
NOTES:
even xy yx
odd xyx or xzyzx or xzjyjzx

chr(ord('c') + 1)
'd'
ord('c') - ord('d')
-1

'''

strings = ['abc', 'abcba', 'abcd', 'cba']

def isPalindrome(word):
	if word == word[::-1]:
		return True
	else:
		return False

def countPalindromeMaker(word):
	counter = -1
	result = 0
	
	for letter in word:
		if ord(letter) - ord(word[counter]) < 0:
			result += ord(letter) - ord(word[counter])

		counter = counter - 1
	
	return abs(result)

for word in strings:
	if isPalindrome(word) == True:
		print 0
	else:
		result = countPalindromeMaker(word)
		print result

	


