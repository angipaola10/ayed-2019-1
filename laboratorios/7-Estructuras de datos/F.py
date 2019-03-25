from sys import stdin
from collections import deque

def main():
    n = int(stdin.readline().strip())
    gval_line = [0 for i in range(n)]
    gval = [gval_line[:] for i in range(n)]
    grid = []
    queue = deque([])

    for i in range(n):
        grid.append(input().strip())

    coords = [int(i) for i in input().strip().split(' ')]
    initial = (coords[0], coords[1])
    final = (coords[2], coords[3])

    queue.append(initial)

    while len(queue)!=0:
        curr = queue.popleft()
        y, x = curr
        if curr==final:
            print(str(gval[y][x]))
            break
        cval = gval[y][x]+1

        for i in range(y+1, n):
            if grid[i][x] == 'X':
                break
            elif gval[i][x] == 0:
                gval[i][x] = cval
                queue.append((i, x))
                
        for i in range(y-1, -1, -1):
            if grid[i][x] == 'X':
                break
            elif gval[i][x] == 0:
                gval[i][x] = cval
                queue.append((i, x))
    
        for i in range(x+1, n):
            if grid[y][i] == 'X':
                break
            elif gval[y][i] == 0:
                gval[y][i] = cval
                queue.append((y, i))
                
        for i in range(x-1, -1, -1):
            if grid[y][i] == 'X':
                break
            elif gval[y][i] == 0:
                gval[y][i] = cval
                queue.append((y, i))
main()
        
