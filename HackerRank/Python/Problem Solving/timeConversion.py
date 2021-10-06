# Manuel Ortiz Hernández at 2020
# Problem solving. Extracted from: https://www.hackerrank.com/challenges/time-conversion/problem
import os
import sys

def time_conversion(s):
    hour = 0
    to_return = ""
    hour = int(s[0:2])
    if s.find("PM") != -1:    
        if hour != 12:
            hour += 12
        to_return = str(hour) + s[2:8]
    else:
        if hour == 12:
            to_return = "00" + s[0:8]
        else:
            to_return = s[0:8]
    return to_return

if __name__ == '__main__':
    s = input()
    result = time_conversion(s)
    print(result)


