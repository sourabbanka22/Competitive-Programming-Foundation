def equationOfLine(P, Q):
    a = Q[1]-P[1]
    b = P[0]-Q[0]
    c = -(a*P[0]+b*P[1])
    
    equation = ""
    if b<0:
        equation = str(a)+"x - "+str(b)+"y "+str(c)+" = 0"
    else:
        equation = str(a)+"x + "+str(b)+"y "+str(c)+" = 0"
    
    return equation


P = [3, 2]
Q = [2, 6]
print(equationOfLine(P, Q))