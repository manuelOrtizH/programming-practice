#Manuel Ortiz at 2022
#Extracted from: https://www.hackerrank.com/challenges/bigger-is-greater/problem

def biggerIsGreater(w):
    suffix = [w[-1]]
    preffix = list(map(lambda a: a, w[:-1]))
    pivot = ''
    j = 0
    for el in w[-2::-1]:
        if suffix[j] > el:
            pivot = el
            preffix.pop()
            suffix = suffix[::-1]
            break
        suffix.append(el)
        preffix.pop()
        j+=1
    if len(suffix)==len(w):
        return 'no answer'
    j = len(suffix) - 1
    while j>=0:
        if suffix[j] > pivot:
            suffix[j], pivot = pivot, suffix[j]
            suffix = sorted(suffix)
            break
        j-=1
    return ''.join(preffix + [pivot] + suffix)

if __name__ == '__main__':
    word = 'dcba'
    result = biggerIsGreater(word)
    print(result)


    