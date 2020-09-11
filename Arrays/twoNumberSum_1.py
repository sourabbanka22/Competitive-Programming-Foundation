def twoNumberSum(array, targetSum):
    Cache = {}
    for val in array:
        check = targetSum - val
        if check in Cache:
            return [check, val]
        else:
            Cache[val] = True
    return []
