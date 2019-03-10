from sys import stdin

def rutas(matriz):
    matriz[0][0] = 1 
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 'x':
                if i-1>=0 and matriz[i-1][j] != 'x':
                   matriz[i][j] += matriz[i-1][j]
                if j-1>=0 and matriz [i][j-1] != 'x':
                       matriz[i][j] += matriz[i][j-1]
    return matriz[-1][-1]
        
    
def main():
    string = stdin.readline().strip()
    matriz=[]
    for i in range(len(string)):
        if string[i] =='[':
            lista=[]
            while string[i]!=']':
                if string[i] == '1':
                    lista.append('x')
                elif string[i] == '0':
                    lista.append(0)
                i+=1
            matriz.append(lista)
        else:
            i+=1
    print(rutas(matriz[1:]))
main()
