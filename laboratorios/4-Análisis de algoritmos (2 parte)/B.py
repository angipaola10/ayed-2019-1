# B
from sys import stdin

def friendqueries():
    n = int(stdin.readline().strip())
    dic = {}
    for i in range (n):
        a , b = stdin.readline().split()
        a , b = int(a) , int(b) 
        if a in dic :
            k = dic.get(a)
            dic[a] = k+1
        else:
            dic[a] = 1
        if b in dic:
            k = dic.get(b)
            dic[b] = k+1
        else:
            dic[b] = 1
        print(int(dic.get(a))+int(dic.get(b)))
friendqueries()
