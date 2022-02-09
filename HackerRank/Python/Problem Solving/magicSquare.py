MATRIX = {0: [(1,2), (3,6), (4,8)], 1: [(0,2), (4,7)], 2: [(0,1), (4,6), (5,8)],  3: [(0,6), (4,5)], 4: [(0,8), (2,6), (3,5), (1,7)],
           5: [(3,4), (2,8)], 6: [(0,3), (7,8), (4,2)], 7: [(1,4), (6,8)], 8:[(6,7), (2,5), (0,4)]}


def formingMagicSquare(s):
    levels, cost, row, limit = {0:[],1:[],2:[]},0,0,2
    for i in range(len(s)):
        for x,y in MATRIX[i]:
            sums = s[x] + s[y] + s[i]
            #if levels[row]:
                #if levels[row][-1] != sums or sums == 15:
                    #levels[row] = []
                    #break
            levels[row].append(sums)
        if row == limit:
            print(levels)
            levels[0],levels[1],levels[2] = [],[],[]         
            row = 0
            
        else:
            row+=1

    return cost

if __name__ == '__main__':
    s = [4,8,2,4,5,7,6,1,6]
    result = formingMagicSquare(s) 



        