def intersectionCardinality(indices, sets):
    if len(indices) == 0:
        return 0
    
    common = sets[indices[0]]
    for idx in range(1, len(indices)):
        common = common.intersection(sets[indices[idx]])

    return len(common)

def inclusionExclusion(sets):
    n = len(sets) 
    result = 0
    b = 0
    while b < (1 << n):
        indices = []
        k = 0
        while k<n:
            if b & (1 << k):
                indices.append(k)
            k += 1
        
        cardinality = intersectionCardinality(indices, sets)
        if len(indices) % 2 == 1:
            result += cardinality
        else:
            result -= cardinality
        b += 1
    
    return result

print(inclusionExclusion([{1, 2, 3}, {2, 3, 4}, {1, 3, 5}, {2, 3}]))