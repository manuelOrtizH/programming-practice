#Manuel Ortiz Hernández at 2020
#Problem solving. Extracted from: https://www.hackerrank.com/challenges/merge-the-tools/problem

def mergeTheTools(string,k):
	sub_div = len(string)//k
	counter = 0
	
	i = 0
	for i in range(0, len(string), sub_div):
		sub_string = string[i:i+sub_div]
		to_print = ""
		for each in sub_string:
			if to_print.find(each) == -1:
				to_print += each
		print(to_print)


			
if __name__ == '__main__':
	string,k = input(), int(input())
	mergeTheTools(string, k)