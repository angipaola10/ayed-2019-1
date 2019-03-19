from sys import stdin

def ways(n):
    if n%2 != 0 or n==0:
        return 0
    w = [3,11]
    while len(w)< n//2:
        R = (4*w[-1])-(w[-2])
        w.append(R)
    return w[n//2-1]
        

def main():
    n = int(stdin.readline().strip())
    print(ways(n))
main()
