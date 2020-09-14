def productSum(array):
    # Write your code here.
    return productSumUtil(array, 1)

def productSumUtil(array, depth):
    total = 0
    
    for element in array:
        total += element if type(element) == int else productSumUtil(element, depth+1)

    return depth*total

print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))