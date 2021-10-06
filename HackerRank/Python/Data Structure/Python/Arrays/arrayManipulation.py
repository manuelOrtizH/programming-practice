#Manuel Ortiz Hernández at 2020
#Data Structure Problem Solving. Extracted from: https://www.hackerrank.com/challenges/crush/problem
import time

def arrayManipulation(n, queries):
    zero_array = [0 for x in range(n)]
    i = 0  
    initial_index = queries[0][0] 
    maximum = 0
    
    maximum = arrayManipulationRec(i, initial_index, zero_array, queries)

    print(zero_array)
    return maximum

def arrayManipulationRec(i, initial_index, zero_array, queries):
    final_index = queries[i][1]
    to_add = queries[i][2]

    if i == len(queries):
        return max(zero_array)
    
    if initial_index > final_index:
        i+=1
        if i < len(queries):
            initial_index = queries[i][0]
        else:
            return max(zero_array)
    else:
        zero_array[initial_index-1] += to_add
        initial_index+=1
        
    arrayManipulationRec(i, initial_index, zero_array, queries)
    return max(zero_array)


if __name__ == '__main__':
    
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    start_time = time.time()

    result = arrayManipulation(n, queries)

    end_time = time.time()

    print(result)
    print("--- %s seconds ---" % (end_time - start_time))














