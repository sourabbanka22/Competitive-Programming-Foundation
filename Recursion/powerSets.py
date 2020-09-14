def powerset(array):
    # Write your code here.
    result = [[]]
    for element in array:
        result += powersetUtil(result, element)
    
    return result

def powersetUtil(result, element):
    tempArray = []
    for subarray in result:
        tempArray.append(subarray + [element])
    return tempArray

print(powerset([1,2,3]))
