#Manuel Ortiz Hernández at 2020
#Data Structure Problem Solving. Extracted from: https://www.hackerrank.com/challenges/dynamic-array/problem

import math
import os 
import random
import re
import sys

def createSequences(n):
	sequences = []
	for _ in range(n): 
		sequences.append([])	
	return sequences

def dynamicArray(n,queries):
	sequences = createSequences(n)
	last_answer = 0
	last_answer_array = []
	i = 0
	while i<len(queries):
		query_to_do = queries[i][0]
		x = queries[i][1]
		y = queries[i][-1]
		if query_to_do == 1:
			seq_list = ((x^last_answer)%n)
			sequences[seq_list].append(y)
		else:
			seq_list = ((x^last_answer)%n)
			index = y%len(sequences[seq_list])
			last_answer = sequences[seq_list][index]
			last_answer_array.append(last_answer)
		i+=1

	return last_answer_array


if __name__ == '__main__':

	first_multiple_input = input().rstrip().split()
	n = int(first_multiple_input[0])
	q = int(first_multiple_input[1])
	queries = []

	for _ in range(q):
		queries.append(list(map(int,input().rstrip().split())))


	result = dynamicArray(n, queries)

	for each in result:
		print(each)
 	
 	
