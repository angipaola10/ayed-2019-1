import json

def parimpar(lista,cont,pares,impares):
    if cont < len(lista):
        if lista[cont] % 2 == 0:
            pares.append(lista[cont])
        else:
            impares.append(lista[cont])
        return parimpar(lista,cont+1,pares,impares)
    else:
        return pares+impares

# TODO Complete!
def arrange(numbers):
    number = parimpar(numbers,0,[],[])
    return number


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            numbers = test["numbers"]
            actual = arrange(numbers)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
