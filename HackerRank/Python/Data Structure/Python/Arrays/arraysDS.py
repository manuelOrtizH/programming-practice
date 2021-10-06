#Manuel Ortiz Hernández at 2020
#Data Structure Problem Solving. Extracted from: https://www.hackerrank.com/challenges/arrays-ds/problem

import math
import os 
import random
import re
import sys

def reverseArray(arr, arr_count):
	i = arr_count-1
	a = []
	while(i>=0):
		a.append(arr[i])
		i-=1

	print(a)


if __name__ == '__main__':

	arr_count = int(input())
	arr = list(map(int, input().rstrip().split()))
	reverseArray(arr, arr_count)
	
