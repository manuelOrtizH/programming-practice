#Manuel Ortiz at 2022
#Extracted from: https://www.hackerrank.com/challenges/service-lane/problem

def serviceLane(n, cases, width):
    result = map(lambda case: min(width[case[0]:case[-1]+1]), cases)
    return list(result)

if __name__ == '__main__':
    n = 8 
    t = 5
    width = [1, 2, 2, 2, 1]
    cases = [[2, 3], [1, 4], [2, 4], [2, 4], [2, 3]]
    result = serviceLane(n,cases, width)
    print(result)