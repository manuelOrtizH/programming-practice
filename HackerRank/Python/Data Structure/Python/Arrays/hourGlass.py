#Manuel Ortiz Hernández at 2020
#Data Structure Problem Solving. Extracted from: https://www.hackerrank.com/challenges/2d-array/problem
def getMax(total_sums):
	maximum = 0
	for i in range(1,len(total_sums)-1):
		if total_sums[maximum] < total_sums[i]:
			maximum = i
	return total_sums[maximum]

def hourGlassSum(arr):
	total_sums = []
	for i in range(len(arr)-2):
		for j in range(map(len(arr))):
			sum_hour_glass = 0
			sum_hour_glass += arr[i][j]+arr[i][j+1]+arr[i][j+2]
			sum_hour_glass += arr[i+1][j+1]
			sum_hour_glass += arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
			total_sums.append(sum_hour_glass)
		
	maximum = getMax(total_sums)
	return maximum		

if __name__ == '__main__':

	arr = [[1, 1, 1, 0, 0, 0],[0, 1, 0, 0, 0, 0],[1, 1, 1, 0, 0, 0],[0, 0, 2, 4, 4, 0],[0, 0, 0, 2, 0, 0],[0, 0, 1, 2, 4, 0]]
	level_zero 	= [1, 1, 1, 0, 0, 0]
	level_one 	= [0, 1, 0, 0, 0, 0]
	level_two 	= [1, 1, 1, 0, 0, 0]
	level_three = [0, 0, 2, 4, 4, 0]
	level_four 	= [0, 0, 0, 2, 0, 0]
	level_five 	= [0, 0, 1, 2, 4, 0]

	maximum = hourGlassSum(arr)
	print(maximum)
	


