#Manuel Ortiz at 2022
#Extracted from https://www.hackerrank.com/challenges/angry-professor/problem

def angryProfessor(k,a):
    on_time = len([s for s in a if s<=0])
    return 'NO' if on_time >= k else 'YES'

if __name__ == '__main__':
    k = 2
    a = [0, -1, 2, 1]
    print(angryProfessor(k, a))