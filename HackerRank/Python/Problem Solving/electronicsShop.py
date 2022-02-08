#Manuel Ortiz at 2022
#Extracted from: https://www.hackerrank.com/challenges/electronics-shop/problem

from functools import reduce
def getMoneySpent(keyboards, drives, b):
	sorted_a, sorted_b = list(filter(lambda e: e<b,sorted(drives,reverse=True))), list(filter(lambda e: e<b, sorted(keyboards, reverse=True)))
	if len(keyboards) > len(drives):
		sorted_a,sorted_b = sorted_b, sorted_a
	prices = []
	for f in sorted_a:
		for s in sorted_b:
			price = f+s
			if price <= b:
				prices.append(price)
	print(prices)
	return -1 if not prices else max(prices)

if __name__ == '__main__':
	b = 100
	keyboards = [1,2,3,4,5]
	drives = [55,45,35,25,15,5,0]
	result = getMoneySpent(keyboards, drives, b)
	print(result)
