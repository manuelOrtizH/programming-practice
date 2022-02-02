#Manuel Ortiz at 2022
#Problem solving. Extracted from: https://www.hackerrank.com/challenges/the-birthday-bar/problem
import random
from functools import reduce
def birthday(choc_bar,day_sum,month):
    choc_div = map(lambda x: sum(x) ,zip(*map(lambda x: choc_bar[x:],range(month))))
    filtered_choc = list(filter(lambda x: x == day_sum, choc_div))
    return len(filtered_choc)
    

if __name__ == '__main__':
    n = 100
    choc_bar = [1]
    day_sum = random.randrange(1,32) #day sum
    month = random.randrange(1,13) #month length
    splited = birthday(choc_bar, day_sum, month)
    print(splited)