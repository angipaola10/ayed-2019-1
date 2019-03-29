from sys import stdin

def main():
    n = int(stdin.readline().strip())
    lista = [int(x) for x in stdin.readline().strip().split()]
    q,r = stdin.readline().split()
    q,r = int(q),int(r)
    ordenada = sorted(lista)
    stri = []
    for i in range(q):
        ind,dul,r = stdin.readline().split()
        ind,dul,r = int(ind),int(dul),int(r)
        x = lista[ind-1]
        lista[ind-1]=dul
        ordenada[ordenada.index(x)]=dul
        ordenada.sort()
        stri.append(ordenada[r-1])
    print(*stri)
main()
