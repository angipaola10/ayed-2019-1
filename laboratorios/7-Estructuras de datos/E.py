from sys import stdin

def main():
    cad = stdin.readline().strip()
    lista = [int(x) for x in cad.split('→')]
    if lista[-1] in lista[:-1]:
        print(str(True)+"\n"+cad[:-1-len(str(lista[-1]))])
    else:
        print(False)

main()
