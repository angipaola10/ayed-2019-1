#B-iterative
from sys import stdin

def binary_search(n,lista,k):
    for i in range(len(lista)):
        if len(lista) < 2:
            if lista[0] == n:
                return k
            else:
                return -1
        else:
            middle = len(lista)//2
            if lista[middle] == n:
                return k+middle
            else:
                izq = lista[:middle]
                if n > izq[-1]:
                    lista = lista[middle+1:]
                    k+=middle+1
                else:
                    lista = lista[:middle]
        

def main():
    n = int(stdin.readline().strip())
    lista = [int(x) for x in stdin.readline().strip().split(',')]
    print(binary_search(n,lista,0))
main()
