from sys import stdin

def is_valid(keys,i,j):
    if i>=0 and i<4 and j>=0 and j<3:
        if keys[i][j] != '*' and keys[i][j]!='#':
            return keys[i][j]
        else:
            return 10
    else:
        return 10

def calcular(n,m,row,col,keys):
    aa = 0
    for x in range(n-1):
        ml=[]
        for i in range(len(keys)):
            for j in range(len(keys[i])):
                if keys [i][j] != '*' and keys[i][j] != '#':
                    temp = m[keys[i][j]][-1]
                    for k in range(len(row)):
                        num = is_valid(keys,i+row[k],j+col[k])
                        if num < 10:
                            temp+=m[num][-1]
                    ml.append([temp])              
        m = []
        m.append(ml[-1])
        m = m+ml[:-1]
        
    acu = 0
    for p in m:
        acu+=p[0]

    return acu                       

keys = [[1,2,3],
        [4,5,6],
        [7,8,9],
        ['*',0,'#']]

row = [0,-1,0,1]
col = [-1,0,1,0]
n = int(stdin.readline().strip())
if n == 1:
    print(10)
else:
    m = [[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]
    print(calcular(n,m,row,col,keys))
