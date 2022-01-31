#Manuel Ortiz Hernández at 2020
#Python Problems. Extracted from: https://www.hackerrank.com/challenges/python-string-formatting/problem
def printFormatted(number):
	length = len("{0:b}".format(number))
	for i in range(1, number+1):
		print("{0:{l}d} {0:{l}o} {0:{l}X} {0:{l}b}".format(i, l=length))

if __name__ == '__main__':
	n = int(input())
	printFormatted(n)