#Manuel Ortiz at 2022
#Extracted from https://www.hackerrank.com/challenges/permutation-equation/problem

def permutationEquation(p):
    my_dict = {v:i+1 for i,v in enumerate(p)}
    result = []
    for i in range(1,len(p)+1):
        j = my_dict[my_dict[i]]    
        result.append(j)
    return result

if __name__ == '__main__':
    p = [2,3,1]
    # 1 = p3 = p(p2) = p(1) = 2
    # 2 = p1 = p(p3) = p(3) = 3
    #result = []
    result = permutationEquation(p) 
    print(*result)