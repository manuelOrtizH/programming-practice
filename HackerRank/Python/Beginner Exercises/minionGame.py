#Manuel Ortiz Hernández at 2020
#Python Problems. Extracted from:  https://www.hackerrank.com/challenges/the-minion-game/problem
import re

def isVowel(s):
	match = re.match('([^aeiou]*)', s, flags=re.I)
	if match:
		index = len(match.group(1))
		if index < len(s):
			return index		
	return -1

def minionGame(string):
	contenders = {"Stuart": 0, "Kevin": 0}
	l = len(string)
	for i in range(l):
		if isVowel(string[i]) == 0:
			contenders['Kevin'] += l-i
		else:
			contenders['Stuart'] += l-i

	if contenders['Kevin'] > contenders['Stuart']:
		print("Kevin", contenders['Kevin'])
	elif contenders['Stuart'] > contenders['Kevin']:
		print("Stuart", contenders['Stuart'])
	else:
		print("Draw")


if __name__ == '__main__':
	s = input()
	minionGame(s)




