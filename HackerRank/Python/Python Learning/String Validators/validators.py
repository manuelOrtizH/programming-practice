#Manuel Ortiz Hernández at 2020
#Python Problems. Extracted from: https://www.hackerrank.com/challenges/string-validators/problem
def evaluateStrings(string, dict_functions):
	num = ""
	for i in range(1,6):
		limit = 0
		for i in len(string):
			num = str(i)
			if eval("char."+dict_functions[num]+"()"):
				print(True)
				break
			limit+=1

			if limit == len(string):
				print(False)
				break
	
def read_data():
	string = input()	
	return string
	
def main():
	string = read_data()
	dict_functions = {'1': "isalnum", 
					  '2': "isalpha", 
					  '3': "isdigit", 
					  '4': "islower", 
					  '5': "isupper" }

	evaluateStrings(string, dict_functions)

if __name__ == '__main__':
	main()




