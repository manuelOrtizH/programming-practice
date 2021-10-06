#Manuel Ortiz Hernández at 2020
#Python Problems. Extracted from: https://www.hackerrank.com/challenges/swap-case/problem
def swapCase(s):
	final_word = ""
	for word in s:
		if word.islower():
			final_word+=word.upper()	
		else:
			final_word+=word.lower()

	return final_word


if __name__ == '__main__':
	s = input()
	result = swapCase(s)
	print(result)