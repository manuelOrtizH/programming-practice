#Manuel Ortiz at 2022
#Extracted from https://www.hackerrank.com/challenges/find-digits/problem

def findDigits(n):
    c = 0
    for d in str(n):
        if n % int(d) == 0:
            c+=1
    return c

if __name__ == '__main__':
    n = [33]
    for num in n:
        result = findDigits(num)
        print(result)