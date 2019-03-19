from sys import stdin

def spikes(road,speed,position):
    if speed == 0 :
        return True
    if position >= len(road):
        return False
    if road[position] == ' False' or road[position] == 'False' :
        return False
    if spikes(road,speed,position+speed) == True:
         return True
    if spikes(road,speed-1,position+speed-1) == True:
         return True
    if spikes(road,speed+1,position+speed+1) == True:
        return True
    return False


def main():
    road = [str(x) for x in stdin.readline().strip().split(',')]
    speed = int(stdin.readline().strip())
    position = int(stdin.readline().strip())
    if road[position] == ' False' or road[position]=='False':
        print('False')
    else:
        print(spikes(road,speed,position))
main()
