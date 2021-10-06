#Manuel Ortiz Hernández at 2020
#Python Problems. Extracted from: https://www.hackerrank.com/challenges/nested-list/problem
def readData():	
	group = []

	for _ in range(int(input())):
		name = input("Name: ")
		score = float(input("Score: "))
		group.append([name,score])
	return group

def getSecondMinimum(group):
	minimum = 0
	second_minimum = 0
	final_list = []
	j = 0		
	for i in range(len(group)):
		if group[minimum][1] > group[i][1]:
			second_minimum = minimum
			minimum = i
		else:
			if group[i][1] > group[minimum][1] and group[i][1] < group[second_minimum][1]:
				second_minimum = i
		if group[second_minimum][1] == group[minimum][1]:
			second_minimum+=1
	
	while j< len(group):
		if group[second_minimum][1] == group[j][1]:
			final_list.append(group[j])
		j+=1

	return final_list

def print_students(group):
	group.sort()
	for i in group:
		print(i[0])

def main():
	group = readData()
	printStudents(getSecondMinimum(group))

main()
