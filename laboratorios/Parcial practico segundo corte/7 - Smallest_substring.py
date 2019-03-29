from sys import stdin

def substring(cad):
    l = []
    i=0
    while len(cad) > 0 and i<len(cad):
        if cad[i] in cad[:i]:
            k = cad[:i].index(cad[i])
            l.append(len(cad[:i]))
            cad = cad[k+1:]
            i=0
            
        else:
            i+=1
    l.append(len(cad))
    return max(l)
        
def main():
    cad = stdin.readline().strip()
    print(substring(cad))
main()
