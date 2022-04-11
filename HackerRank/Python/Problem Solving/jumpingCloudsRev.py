#Manuel Ortiz at 2022
#Extracted from https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

def jumpingOnClouds(c,k):
    e = 100
    for cloud in range(0,len(c),k):
        e -= k
        if c[cloud] == 1:
            e-=2
    
    return e



if __name__ == '__main__':
    n = 10
    k = 3
    c = [1, 1, 1, 0, 1, 1, 0, 0, 0, 0]
    #[0, 0, 1, 0, 0, 1, 1, 0]
    #       i        i   

    #[1, 1, 1, 0, 1, 1, 0, 0, 0, 0]

    #Resut = 92
    result = jumpingOnClouds(c, k)
    print(result)




