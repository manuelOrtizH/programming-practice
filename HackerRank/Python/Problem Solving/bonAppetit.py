def bonAppetit(bill,k,b):
    sum_bill = (sum(bill) - bill[k])//2
    return 'Bon Appetit' if sum_bill == b else b - sum_bill

if __name__ == '__main__':
    k, b = 1, 12
    #k bill[k] item Anna did not consume
    #b Amount of Money Brian charged Anna
    bill = [3,10,2,9]
    print(bonAppetit(bill, k, b))