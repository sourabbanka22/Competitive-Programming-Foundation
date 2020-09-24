def balancedBrackets(string):
    # Write your code here.
    stack = []
    for barcket in string:
        if barcket == "(" or barcket == "[" or barcket == "{":
            stack.append(barcket)
        elif barcket == ")" or barcket == "]" or barcket == "}":
            if len(stack) == 0:
                return False
            elif stack[-1] == "(" and barcket == ")" or stack[-1] == "[" and barcket == "]" or stack[-1] == "{" and barcket == "}":
                stack.pop()
            else:
                return False
    
    return len(stack)==0

print(balancedBrackets("(((((({{{{{[[[[[([)])]]]]]}}}}}))))))"))
print(ord("z"), ord("A"))