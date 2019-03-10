from sys import stdin

def maximo(n,lista):
    dic = {}
    m = []
    lista.sort()
    for x in range (len(lista)):
        m.append([])
    for i in  range(len(lista)):
        x=0
        for j in range(min(lista),n+1):
            if i == 0:
                m[i].append(min(lista))
                dic[min(lista)]=[min(lista)]
            elif j-lista[i] < 0:
                m[i].append(m[i-1][x])
            elif j-lista[i] == 0:
                m[i].append(j)
                dic[j] = [j]
            elif j - lista[i] >= min(lista):
                k = j - lista[i]-min(lista)
                m[i].append(m[i-1][k]+lista[i])
                v = dic.get(j - lista[i])
                dic[j] = v+[lista[i]]
            elif j - lista[i] < min(lista):
                if m[i-1][x] > lista[i]:
                    m[i].append(m[i-1][x])
                    dic[j] = dic[m[i-1][x]]
                else:
                    m[i].append(lista[i])
                    dic[j] = [lista[i]]
            x+=1
    return m[-1][-1] , dic

def eliminar(dic, lista, n):
    v = dic.get(n)
    for i in v:
        del(lista[lista.index(i)])
    return lista
            

def main():
    lista = [int(x) for x in stdin.readline().strip().split(',')]
    a = int(stdin.readline().strip())
    b = int(stdin.readline().strip())
    n = [a,b]
    acu = 0
    if a in lista:
        acu+=a
        del(lista[lista.index(a)])
        if b in lista:
            acu+=b
        else:
            acu+=maximo(b,lista)
    elif b in lista:
        acu+=b
        del(lista[lista.index(b)])
        ka,da = maximo(a,lista)
        acu+=ka
    if acu == 0:
        ka , da = maximo(a,lista)
        kb , db = maximo(b,lista)
        if ka == a and kb == b:
            if a>b :
                #a
                acu+=a
                lista = eliminar(da,lista,a)
                kb , db = maximo(b,lista)
                acu+=kb
            elif a<b:
                #b
                acu+=b
                lista = eliminar(db,lista,b)
                ka , da = maximo(a,lista)
                acu+=ka
            else:
                #cualquiera
                acu+=a
                lista = eliminar(da,lista,a)
                kb , db = maximo(b,lista)
                acu+=kb
        elif ka == a:
            #sirve a
            acu+=a
            lista = eliminar(da,lista,a)
            kb , db = maximo(b,lista)
            acu+=kb
        elif kb == b:
            #sive b
            acu+=b
            lista = eliminar(db,lista,b)
            ka , da = maximo(a,lista)
            acu+=ka
        elif ka!=a and kb!=b:
            if ka-a < kb-b:
                #ka
                acu+=ka
                lista = eliminar(da,lista,a)
                kb , db = maximo(b,lista)
                acu+=kb
            elif ka-a > kb-b:
                #kb
                acu+=kb
                lista = eliminar(db,lista,b)
                ka , da = maximo(a,lista)
                acu+=ka
            else:
                acu+=a
                lista = eliminar(da,lista,a)
                kb , db = maximo(b,lista)
                acu+=kb
    print(acu)
        
main()
