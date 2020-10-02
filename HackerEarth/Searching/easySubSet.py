'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
# aLen = int(input())
# aList = set(map(int, input().split()))
# cLen = int(input())
# cList = set(map(int, input().split()))

aLen = 2
aList = [1, 2]
cLen = 3
cList = [3, 4, 5]

bList = []
startIdx = min(cList)-min(aList)
endIdx = max(cList)-max(aList)+1
for index in range(startIdx, endIdx):
    found = True
    for val in aList:
        if index+val not in cList:
            found = False
            break
    if found:
        # bList.append(index)
        print(index, end=" ")

# print(*bList)




