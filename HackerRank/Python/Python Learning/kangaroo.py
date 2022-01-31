import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):
	diff = ((x2 + v2) - (x1 + v1))
	pattern = v1-v2

	if pattern < 0 or pattern == 0:
		return "NO"
	else:
		if diff%pattern == 0:
			return "YES"
		else:
			return "NO"


if __name__ == '__main__':
    
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)