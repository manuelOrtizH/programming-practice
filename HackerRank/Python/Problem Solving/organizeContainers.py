#Manuel Ortiz at 2022
#Extracted from: https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

def organizingContainers(containers, n):
    balls_set, containers_set = set(), set()
    for i in range(len(containers)):
        sum_container,sum_ball = 0,0
        for j in range(len(containers[i])):
            sum_ball+=containers[j][i]
            sum_container+=containers[i][j]
        containers_set.add(sum_container)
        balls_set.add(sum_ball)
    swaps = len(balls_set)
    return 'Possible' if len({*balls_set, *containers_set}) == swaps else 'Impossible'

if __name__ == '__main__':
    q = 2 # number of queries
    n = 3 # number of containers (rows) and types (columns)
    containers = [[2,2,3],[1,2,3],[1,1,2]]
    result = organizingContainers(containers, len(containers))
    print(result)