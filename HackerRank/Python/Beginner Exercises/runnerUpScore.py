#Manuel Ortiz Hernández at 2020
#Python problems. Extracted from: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

def runnerUp(arr):
	maximum_runner = 0
	secondMax = 0
	if not arr:
		return "empty"
	for i in range(1, len(arr)):
		if arr[maximum_runner]<arr[i]:
			secondMax = maximum_runner
			maximum_runner = i
		else:
			if arr[i]<arr[maximum_runner] and arr[i]>arr[secondMax]:
				secondMax = i
		if arr[secondMax]==arr[maximum_runner]:
			secondMax+=1
	return arr[secondMax]

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    result = runnerUp(arr)

