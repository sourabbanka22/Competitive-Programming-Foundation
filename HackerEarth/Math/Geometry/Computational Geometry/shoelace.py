def polygonArea(coords):
    area = 0.0

    length = len(coords)
    second = length-1
    for first in range(length):
        area += (coords[second][0]+coords[first][0]) * (coords[second][1]-coords[first][1])
        second = first
    
    return abs(area/2.0)

coords1 = [[0, 1], [2, 3], [4, 7]]
coords2 = [[-2, -2], [0, 4], [3, -1], [1, -1]]
print(polygonArea(coords2))