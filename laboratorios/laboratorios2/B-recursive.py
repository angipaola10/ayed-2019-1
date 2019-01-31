#B-recursive
from sys import stdin

def binary_search(n,lista,k):
    if len(lista) < 2:
        if lista[0] == n:
            return k
        else:
            return -1
    else:
        middle = len(lista)//2
        if lista[middle] == n:
            return middle
        else:
            izq = lista[:middle]
            der = lista[middle+1:]
            if n > izq[-1]:
                return binary_search(n,der,k+1+middle)
            else:
                return binary_search(n,izq,k)

def main():
    n = int(stdin.readline().strip())
    lista = [int(x) for x in stdin.readline().strip().split(',')]
    print(binary_search(n,lista,0))
main()
