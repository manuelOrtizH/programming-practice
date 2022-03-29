# Manuel Ortiz at 2022
# Extracted fromhttps://www.hackerrank.com/challenges/the-hurdle-race/problem

def hurdleRace(k,height):
    max_diff = max(height) - k
    return max_diff if max_diff > 0 else 0

if __name__ == '__main__':
    k = 7
    heights = [2, 5, 4, 5, 2]
    print(hurdleRace(k, heights))
