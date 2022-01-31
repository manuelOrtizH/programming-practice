#Manuel Ortiz Hernández at 2020
#Python Problems. Extracted from: https://www.hackerrank.com/challenges/find-a-string/problem
def verifyUppercase(string):
	for char in string:
		if (char >= 'a' and char <= 'z'):
			return True

def countSubstring(string, sub_string):

	if len(string) <=1:
		return "The length is from 2"

	if verifyUppercase(string) or verifyUppercase(sub_string):
		return "Needs to be in uppercase the whole word"

	counter = 0
	sub_length = len(sub_string)
	i = 0
	while i<=len(string):

		if string.find(sub_string,i,i+sub_length) >= 0:
			counter+=1
		i+=1

	return counter

if __name__ == '__main__':
	string = input().strip()
	sub_string = input().strip()
	count = countSubstring(string, sub_string)
	print(count)



