from functools import reduce

def catAndMouse(x,y,z):
    dif_a, dif_b = abs(x-z), abs(y-z)
    if dif_a == dif_b:
        return 'Mouse C'
    else:
        return 'Cat A' if dif_a < dif_b else 'Cat B'


if __name__ == '__main__':
    q = 2
    q1 = [1,2,3]
    q2 = [1,3,2]
    catAndMouse(q1[0], q1[1], q1[2])

    