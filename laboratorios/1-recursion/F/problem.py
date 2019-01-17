import json

def moveTower(N,from_disc, to_disc, using):
    if N >= 1:
        moveTower(N-1,from_disc,using,to_disc)
        moveDisk(from_disc,to_disc)
        moveTower(N-1,using,to_disc,from_disc)

def moveDisk(from_disc,to_disc):
    return "moving disk from",from_disc,"to",to_disc


# TODO Complete!
def hanoi(n):
    return moveTower(n,'A','B','C')


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            n = test["n"]
            hanoi(n)
        print('OK!')
