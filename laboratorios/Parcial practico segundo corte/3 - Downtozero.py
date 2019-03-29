from sys import stdin

def downtozero(n):
    nums = [0,1,2,3,3]+[None]*(n-4)
    for i in range(2,n+1):
        if (nums[i] is None) or (nums[i]>nums[i-1]+1):
            nums[i] = nums[i-1]
        for j in range(1,i+1):
            if j*n > n:
                break
            if (nums[i*j] is None) or (nums[i]+1 < nums[i*j]):
                nums[i*j] = nums[i]+1
    return nums
        

def main():
    q = int(stdin.readline().strip())
    n= []
    for i in range (q):
        n.append(int(stdin.readline().strip()))
    nmax = max(n)
    p = downtozero(nmax)
    for i in n:
        print(p[i])
main()
