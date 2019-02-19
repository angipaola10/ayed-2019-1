#C
from sys import stdin
import time

def fibonacci_mod(n,m,x):
    if m==1:
        return 0
    elif n==1:
        return 0
    elif n==2 or n==3:
        return 1
    else:
        while m > x[-1]:
            x.append(x[-1]+x[-2])

        while True:
            if x[-1]==1 and x[-2]==1 and x[-3]==0:
                if len(x)>3:
                    x= x[:-3]
                break
            else:
                x.append((x[-1]+x[-2])%m)
                
        k = n%len(x)
        return x[k]
            
def main():
    start = time.time()
    n = int(stdin.readline().strip())
    m = int(stdin.readline().strip())
    print(fibonacci_mod(n,m,[0,1,1]))
    end = time.time()
    print((end-start)/1000)
main()
