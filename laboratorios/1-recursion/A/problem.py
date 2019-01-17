import json

def reverse2(text,t):
    if len (text) == 0:
        return t
    else:
        t+=text[-1]
        text = text[:-1]
        return reverse2(text,t)
    
# TODO Complete!!
def reverse(text):
    t = reverse2(text,'')
    return t


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            text = test["text"]
            actual = reverse(text)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
