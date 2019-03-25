from sys import stdin

def jolly_jumpers(lista,k):
    l = []
    for i in range(len(lista)-1):
        if lista[i+1]-lista[i]>=1 and lista[i+1]-lista[i]<=k and lista[i+1]-lista[i] not in l :
            l.append(lista[i+1]-lista[i])
        elif lista[i]-lista[i+1]>=1 and lista[i]-lista[i+1]<=k  and lista[i]-lista[i+1] not in l:
            l.append(lista[i]-lista[i+1])
        else:
            return False
    return True
        

def main():
    lista = [int(x) for x in stdin.readline().strip().split()]
    print(jolly_jumpers(lista,len(lista)-1))
main()
