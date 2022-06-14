#Manuel Ortiz at 2022
#Extracted from: https://www.hackerrank.com/challenges/the-time-in-words/problem

hour_dict = {1: 'one', 2: 'two', 
             3: 'three', 4: 'four',
             5: 'five', 6: 'six', 
             7: 'seven', 8: 'eight', 
             9: 'nine', 10: 'ten',
             11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'quarter',
             16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
             20: 'twenty', 21: 'twenty one', 22: 'twenty two', 23: 'twenty three',
             24: 'twenty four', 25: 'twenty five', 26: 'twenty six', 27: 'twenty seven',
             28: 'twenty eight', 29: 'twenty nine', 30: 'half'}


def timeInWords(h, m):
    is_minutes = ' minutes' if m != 15 and m != 30 and (60-m)!=15 else ''
    if m == 0:
        return f"{hour_dict[h]} o' clock"
    elif m<=30:
        return f'{hour_dict[m]}{is_minutes[:-1] if m==1 else is_minutes} past {hour_dict[h]}'
    else:
        return f'{hour_dict[60-m]}{is_minutes[:-1] if m==1 else is_minutes} to {hour_dict[h+1]} '
   
if __name__ == '__main__':
    h = 5
    m = 45
    result = timeInWords(h,m)
    print(result)
