#Manuel Ortiz at 2022
#Extracted from: https://www.hackerrank.com/challenges/electronics-shop/problem

from functools import reduce
def getMoneySpent(keyboards, drives, b):
	sorted_a = list(filter(lambda e: e<b,sorted(drives,reverse=True)))
	sorted_b = list(filter(lambda e: e<b, sorted(keyboards, reverse=True)))
	prices = -1
	for f in sorted_a:
		for s in sorted_b:
			price = (f+s) if (f+s) <= b else -1
			if price > prices:
				prices = price
	return prices

if __name__ == '__main__':
	b = 100
	keyboards = [1,2,3,4,5]
	drives = [55,45,35,25,15,5,0]
	result = getMoneySpent(keyboards, drives, b)
	print(result)
