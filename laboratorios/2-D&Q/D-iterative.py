#D-iterative
from sys import stdin

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

def majority(lista,k,n):
    for j in lista:
        if len(lista)== 0:
            return False
        elif len(lista) ==1:
            if 1 > n//2:
                return True
            else:
                return False
        else:
            for i in range(len(lista)):
                if lista[i] == lista[0]:
                    k+=1
                else:
                    break
            if k > n//2:
                return True
            else:
                lista = lista[i:]
                k = 0

        
def main():
    n = int(stdin.readline().strip())
    lista = [int(x) for x in stdin.readline().strip().split()]
    lista = quick_sort(lista)
    print(majority(lista,0,n))
main()
