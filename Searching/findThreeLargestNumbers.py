def findThreeLargestNumbers(array):
    # Write your code here.
    big = float("-inf")
    bigger = float("-inf")
    biggest = float("-inf")

    for val in array:
        if val > biggest:
            big = bigger
            bigger = biggest
            biggest = val
        elif val > bigger:
            big = bigger
            bigger = val
        elif val > big:
            big = val
        
    return [big, bigger, biggest]

print(findThreeLargestNumbers([3, 4, 67, 1, 45, 9, 10]))
print(findThreeLargestNumbers([-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]))