from sys import stdin

def solve(n,x,c):
    li = [0]*2000000
    for i in range(1,n+1):
        li[i] = li[i-1] + c[i-1]
        if i>2:
            li[i] = min(li[i], li[i-2]+ x +c[i-1])
        if i>3:
            li[i] = min(li[i], li[i-3]+ 2*x +c[i-1])
        if i>4:
            li[i] = min(li[i], li[i-4]+ 3*x +c[i-1])
            
    return li[n]

def main():
    n , x = stdin.readline().split()
    n , x  = int(n) , int(x)
    c = [int(x) for x in stdin.readline().strip().split()]
    print(solve(n,x,c))
main()
