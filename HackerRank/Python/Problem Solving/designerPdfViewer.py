#Manuel Ortiz at 2022
#Extracted from: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

import string

def designerPdfViewer(h,word):
    if not word:
        return 0
    my_dict = {s: w for s,w in zip(string.ascii_lowercase, h)}
    max_letter = word[0]
    if word[1:]:
        for letter in word[1:]:
            act_val, max_val = my_dict[letter], my_dict[max_letter]
            max_letter = letter if act_val > max_val else max_letter

    return len(word) * my_dict[max_letter]
        

if __name__ == '__main__':
    h = '1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5'
    word = 'b'
    h = map(lambda v: int(v), h.split(' '))
    print(designerPdfViewer(h, word))