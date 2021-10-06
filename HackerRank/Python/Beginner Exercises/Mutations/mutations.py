#Manuel Ortiz Hernández at 2020
#Python problems. Extracted from: https://www.hackerrank.com/challenges/python-mutations/problem

def mutateString(string, index, new_character):
	new_string = ""
	if index < 0:
		return new_string + string
	if index > len(s):
		return string + new_string
	new_string = string[:index] + new_character +string[index+1:]
	return new_string


def main():
	s  = input()
	i, c = input().split()
	s_new = mutateString(s, int(i), c)
	print(s_new)

if __name__ == '__main__':
	main()