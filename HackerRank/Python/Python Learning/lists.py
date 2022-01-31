#Manuel Ortiz Hernández at 2020
#Python Problems. Extracted from: https://www.hackerrank.com/challenges/python-lists/problem
def readData():
	N = int(input())
	list_to_modify = []
	for _ in range(N):
		commands = {}
		function, *line = input().split()
		numbers = list(map(str, line))
		commands[function] = numbers
		detCmds(commands, list_to_modify)
		
	return commands

def detCmds(commands, list_to_modify):
	for function, numbers in commands.items():
		if function == "print":
			print(list_to_modify)
		else:
			function += "(" + ",".join(numbers) + ")"
			eval("list_to_modify."+function)
		


def main():
	readData()

if __name__ == '__main__':
	main()