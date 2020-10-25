def getArea(m, openIntervals):
    INT_MIN = -2**32

    area = 0
    previous = INT_MIN
    for l, r in openIntervals:
        previous = max(previous, l)
        area += max(0, (r - previous) * m)
        previous = max(r, previous)
    return area

def unionOfRectangles(rectangles):
    MOD = 10**9 + 7
    INT_MIN = -2**32
    
    events = []
    for x1, y1, x2, y2 in rectangles:
        events.append([x1, 0, y1, y2])
        events.append([x2, 1, y1, y2])
    events.sort()
        
    area = 0
    previous = INT_MIN
    openIntervals = []
    for event in events:
        current, close, y1, y2 = event
        area += getArea(current - previous, openIntervals)
        if close:
            openIntervals.remove((y1,y2))
        else:
            openIntervals.append((y1,y2))
            openIntervals.sort()
        previous = current
    return area % MOD

print(unionOfRectangles([[2, 1, 4, 2], [2, 3, 4, 5], [1, 4, 3, 6]]))