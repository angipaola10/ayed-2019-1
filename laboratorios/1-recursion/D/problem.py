import json


# TODO Complete!
def compute_ways(n):
    if n == 3:
        return 4
    elif n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return compute_ways(n-1) + compute_ways(n-2) + compute_ways(n-3)


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            n = test["n"]
            actual = compute_ways(n)
            expected = test['result']
            assert actual == expected, f'Test {i} | n: {n} | expected: {expected}, actual: {actual}'
        print('OK!')
