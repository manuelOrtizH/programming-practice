#Manuel Ortiz at 2022
#Extracted from: https://www.hackerrank.com/challenges/counting-valleys/problem
level = {'U': 1, 'D': -1}


def countingValleys(steps, path):
    count = 0
    valley = 0
    is_under = False
    for each in path:
        count += level[each]
        if count < 0:
            is_under = True
        if count >= 0 and is_under:
            is_under = False
            valley+=1
        


if __name__ == '__main__':
    steps = 8
    path = 'UDDDUDUU'
    countingValleys(steps, path)