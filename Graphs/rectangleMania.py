def rectangleMania(coords):
    # Write your code here.
    coordMapper = {}
    for coord in coords:
        coord = stringifyCoordinates(coord)
        coordMapper[coord] = True
    
    rectangleCount = 0
    
    for coord1 in coords:
        for coord2 in coords:
            if isUpperRight(coord1, coord2):
                upperLeft = stringifyCoordinates([coord1[0], coord2[1]])
                bottomRight = stringifyCoordinates([coord2[0], coord1[1]])
                if upperLeft in coordMapper and bottomRight in coordMapper:
                    rectangleCount += 1
    
    return rectangleCount

def isUpperRight(coord1, coord2):
    return coord2[0]>coord1[0] and coord2[1]>coord1[1]

def stringifyCoordinates(coord):
    stringified = str(coord[0]) + "-" + str(coord[1])
    return stringified