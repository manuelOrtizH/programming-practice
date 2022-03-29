#Manuel Ortiz at 2022
#Extracted from https://www.hackerrank.com/challenges/utopian-tree/problem

def utopianTree():
    cache = {0: 1}
    def season(n):        
        if n not in cache:
            if n % 2 == 0:
                cache[n] = season(n-1)+1
            else:
                cache[n] = season(n-1)*2
        return cache[n]
    return season

if __name__ == '__main__':
    cycles = [0,1,4]
    fn = utopianTree()
    for n in cycles:
        print(fn(n))