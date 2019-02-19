from sys import stdin

def primo(num):
    if num==2 or num==1:
        return "Si"
    else:
        cont = 0
        for i in range(2, int(num**(1/2))+1):
            if num%i==0:
                return "No"
        return "Si"
        
    

def main():
    p = int(stdin.readline().strip())
    n = [int(x) for x in stdin.readline().strip().split()]
    rta = ''
    for i in range(len(n)):
        if i==len(n)-1:
            rta += primo(n[i])
        else:
            rta += primo(n[i])+' '
    print(rta)

main()
