##C
from sys import stdin

def fibonacci(n):
    if n  <= 1:
        return n,0
    else:
        a,b = fibonacci(n-1)
    return a+b,a

def main():
    n = int(stdin.readline().strip())
    m = int(stdin.readline().strip())
    k = fibonacci(n)% m
    print(k)
main()
