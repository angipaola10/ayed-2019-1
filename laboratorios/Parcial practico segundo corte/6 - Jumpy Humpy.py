from sys import stdin

def jumpy(n,l):
    for i in range(len(l)-1):
        if l[i+1] - l[i] < 0:
            break
    l = l[:i+1]
    r = []
    for i in range(len(l)-2,-1,-1):
        if i == len(l)-2:
            r.append(l[-2]^l[-1])
        else:
            r.append(l[i]^r[-1])
    return max(r)
    
def main():
    n = int(stdin.readline().strip())
    l = [int(x) for x in stdin.readline().strip().split()]
    print(jumpy(n,l))
main()
