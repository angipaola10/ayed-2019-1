#D
from sys import stdin
import time

def pascal(n):
    print(1)
    k = []
    for j in range(n):
        temp = [1]
        for i in range(len(k)-1):
           temp.append(k[i]+k[i+1])
        temp.append(1)
        print(*temp)
        k = temp
   
def main():
    start = time.time()
    n = int(stdin.readline().strip())
    if n==1:
        print(1)
    else:
        pascal(n)
    end = time.time()
    print(end-start)
main()
