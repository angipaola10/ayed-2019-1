#A
from sys import stdin
import time

def partition(lista):
    pivote,menores,mayores = lista[0],[],[]
    for i in range(1,len(lista)):
        if lista[i] < pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
    return menores,[pivote],mayores


def quick_sort(lista):
    if len(lista) < 2:
        return lista
    else:
        menores,medio,mayores = partition(lista)
    return quick_sort(menores)+medio+quick_sort(mayores)

def main ():
    start = time.time()
    lista = [int (x) for x in stdin.readline().strip().split()]
    if len(lista) > 10:
        r = quick_sort(lista)
        r.reverse()
        print(r[:10])
    else:
        print(lista)
    end = time.time()
    print((end - start)/1000)
main()
