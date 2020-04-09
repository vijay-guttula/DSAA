import sys

def car(dist, crange, no_of_gasStations, gasstations) :
    curr = 0
    point = 0
    count = 0
    if dist <= crange :
        return 0
    
    while point < no_of_gasStations :
        while point < no_of_gasStations and ((crange - (gasstations[point]-curr) >= 0) ) :
            point += 1
        
        if point == 0 :
            return -1
        
        if point > 0 :
            count += 1
            curr = gasstations[point-1]

        if point < no_of_gasStations and (gasstations[point] - curr) > crange :
            return -1
    if dist - curr <= crange :
        return count
    else :
        return -1

        

if __name__ == '__main__' :
    dist = int(sys.stdin.readline())
    crange = int(sys.stdin.readline())
    no_of_gasStations = int(sys.stdin.readline())
    x = sys.stdin.readline()
    gasstations = []

    for n in (x.split()) :
        gasstations.append(int(n))

    #gasstations = [None] * no_of_gasStations
    #gasstations = list.append((map(int, x.split())))
    #gasstations = int(gasstations)

    print(car(dist, crange, no_of_gasStations, gasstations))
    