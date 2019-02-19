from sys import stdin

def ordenar(lista, k):
    if len(lista) == 1:
        return k
    else:
        j = min(lista)
        if lista[0]!= j:
            band, band2 = lista[0], lista.index(j)
            lista[0], lista[band2] = j, band
            print(lista)
            return ordenar(lista[1:],k+1)
        else:
            return ordenar(lista[1:],k)
            

def main():
    lista = [int(x) for x in stdin.readline().strip().split()]
    print(ordenar(lista,0))
main()
