from sys import stdin

string = stdin.readline().strip()
stack = []
for i in range(len(string)):
    stack.append(string[i])
reverse = ""
while stack!=[]:
    reverse+=stack.pop()
print(reverse)
    
