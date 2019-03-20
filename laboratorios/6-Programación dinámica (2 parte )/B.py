from sys import stdin

def ways(n):
    
    w = [0,1,2]
    while len(w) <= n:
        R = w[-1]+ w[-2]* (len(w)-1)
        w.append(R)
        
    return w[n]

def main():
    n = int(stdin.readline().strip())
    print(ways(n))
main()
