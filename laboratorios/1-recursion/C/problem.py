import json

def has_more_vowels2(s,acu):
    vocales = ['a','e','i','o','u']
    if len(s)< 1:
        return acu
    else:
        if s[0] in vocales:
            acu+=1
        s=s[1:]
        return has_more_vowels2(s,acu)
        


# TODO Complete!
def has_more_vowels(s):
    s = s.lower()
    vocales = has_more_vowels2(s,0)
    consonantes = len(s) - vocales
    if consonantes < vocales:
        return True
    else:
        return False


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            s = test["s"]
            actual = has_more_vowels(s)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
