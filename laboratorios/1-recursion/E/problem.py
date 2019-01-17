import json

def cadena (n,k,n2):
    n= str(n)
    if k>0:
        n2+=n
        return cadena(n,k-1,n2)
    else:
        return n2

def superdigit2(cad,acu):
    cad = str(cad)
    if len(cad) > 1:
        for i in range(len(cad)):
            acu+=int(cad[i])
        return superdigit2(acu,0)
    else:
        return int(cad)
    
# TODO Complete!
def super_digit(n, k):
    cad = cadena(n,k,'')
    a=superdigit2(cad,0)
    return a

if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            n = test["n"]
            k = test["k"]
            actual = super_digit(n, k)
            expected = test['result']
            assert actual == expected, f'Test {i} | n: {n} | k: {k} | expected: {expected}, actual: {actual}'
        print('OK!')
