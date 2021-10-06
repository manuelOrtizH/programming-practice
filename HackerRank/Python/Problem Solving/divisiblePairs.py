# Manuel Ortiz Hernández at 2021
# Problem solving. Extracted from: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
def divisibleSumPairs(k, arr, pairs):
    if len(arr) == 1:
        return pairs
    i = arr[0]
    for num in arr[1:]:    
        sum_pairs = num + i
        if (sum_pairs % k) == 0: 
            pairs += 1
    return divisibleSumPairs(k, arr[1:], pairs)

def readData():
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    ar = list(map(int, input().rstrip().split()))
    input_data = [n, k, ar]
    return input_data

def main():
    # input_data = readData()
    input_data = [6,3, [1,3,2,6,1,2]]
    result = divisibleSumPairs(input_data[1], input_data[2], 0)
    print("The result is: ", result)
    
if __name__ == '__main__':
    main()
    