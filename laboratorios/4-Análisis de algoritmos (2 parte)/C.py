from sys import stdin

def main():
    prices = [int(x) for x in stdin.readline().strip().split()]
    money = int(stdin.readline().strip())
    prices.sort()
    acu = 0
    i = 0
    print(prices)
    while acu <= money and len(prices)>0:
        acu += prices[0]
        prices = prices[1:]
        i+=1
    print(i-1)
main()
