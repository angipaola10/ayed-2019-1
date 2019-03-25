from sys import stdin

def left_rotation(lista,n):
    k = len(lista)
    while n>k:
        n-=k
    l1 = lista[n:]
    l2 = lista[:n]
    return l1+l2

def main():
    lista = [int(x) for x in stdin.readline().strip().split()]
    n = int(stdin.readline().strip())
    print(left_rotation(lista,n))
main()
