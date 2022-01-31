#Manuel Ortiz Hernández at 2020
#Python Problems. Extracted from: https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def splitAndJoin(line):
	line = line.split(" ")
	#new_line = line.split(" ") Split all the line
	new_line = "-".join(line)
	return new_line

def main():
	line = input()
	result = splitAndJoin(line)
	print(result)


if __name__ == '__main__':
	main()