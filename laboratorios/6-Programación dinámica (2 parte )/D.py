from sys import stdin

def countWays(n, k) :
    r = [0,k,k**2,k**3-k]
    
    while len(r) <= n:
        t = r[-1]*k - r[-3]*(k-1)
        r.append(t%(10**9 +7)) ## %(10**9 +7)evita desbordamiento de enteros para números muy grandes
        
    return r[n]

def main():
    n = int(stdin.readline().strip())
    k = int(stdin.readline().strip())
    print(countWays(n,k))
main()

