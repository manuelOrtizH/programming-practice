#Manuel Ortiz at 2022
#Extracted from: https://www.hackerrank.com/challenges/camelcase/problem


def camelcase(s):
    return len(list(filter(lambda c: c.isupper(),s))) + 1

if __name__ == '__main__':
    s = 'saveChangesInTheEditor'
    result = camelcase(s)
    print(result)
    