# Manuel Ortiz at 2021
# Extracted from: https://www.hackerrank.com/challenges/sock-merchant/problem
PAIR = 2
def sockMerchant(n,socks):
    basket = dict.fromkeys({*socks}, 0)
    for sock in socks:
        basket[sock] += 1
    a = [x//2 for x in basket.values()]
    return sum(a)

if __name__ == '__main__':
    socks = [1,2,1,2,1,3,2]
    print(sockMerchant(len(socks), socks))