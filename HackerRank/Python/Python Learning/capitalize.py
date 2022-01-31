#Manuel Ortiz Hernández at 2020
#Python Problems. Extracted from: https://www.hackerrank.com/challenges/capitalize/problem
def solve(s):
	previous = ""
	final_s = ""
	for i in range(len(s)):
		capitalized = s[i]
		if i <= 0:
			capitalized = my_capitalize(s[i]) 
		else:
			previous = s[i-1]

		if previous == " ":
			capitalized = my_capitalize(s[i])
		
		final_s += capitalized

	return final_s
		
def myCapitalize(letter):
	if letter.islower():
		letter = letter.upper()

	return letter

def main():
	s = input()
	result = solve(s)
	print(result)

if __name__ == '__main__':
	main()
