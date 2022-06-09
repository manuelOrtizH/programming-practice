#Manuel Ortiz at 2022
#Extracted from: https://www.hackerrank.com/challenges/day-of-the-programmer/problem

def dayOfProgrammer(year):
    julian = lambda y: y % 4 == 0
    gregorian = lambda y: y % 400 == 0 or (y % 4 ==0 and y % 100 != 0)
    calendar_type = julian if 1700 <= year < 1917 else gregorian
    programmer_day = 256 if year != 1918 else 269
    days = 244 if calendar_type(year) else 243
    return f'{programmer_day - days}.09.{year}'
    
if __name__ == '__main__':
    year = 1700
    result = dayOfProgrammer(year)
    print(result)