#Manuel Ortiz at 2022
#Extracted from https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

def reversed(n):
    return int(str(n)[::-1])


def beautifulDays(i,j,k):
    days_to_eval = range(i,j+1)
    beautiful = 0
    for day in days_to_eval:
        calc = (day - reversed(day)) / k
        if calc.is_integer():
            beautiful+=1
    return beautiful

if __name__ == '__main__':
    i,j,k = 20,23,6
    print(beautifulDays(i, j, k))
