from sys import stdin

def coins(n,lista):
    m = []
    lista.sort()
    for x in lista:
        l = []
        for y in range(min(lista),n+1):
            l.append(0)
        m.append(l)
        
    for i in range(len(lista)):
        j = 0
        for k in range(min(lista),n+1):
            if k-lista[i] == 0 and lista[i]>1:
                m[i][j] += 1
            if lista[i] == 1:
                m[i][j]+=1
            if i>0:
                m[i][j] += m[i-1][j]
            if k-lista[i] >= min(lista) and lista[i]>1:
                j2 = k-lista[i]-min(lista)
                m[i][j]+= m[i][j2]
            j+=1
    return(m[-1][-1])
                        
    
def main():
    n = int(stdin.readline().strip())
    lista = [int(x) for x in stdin.readline().strip().split(',')]
    print(coins(n,lista))
main()
