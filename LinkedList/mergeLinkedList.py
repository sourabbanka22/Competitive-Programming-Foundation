# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    # Write your code here.
    pointerOne = headOne
    previous = None
    pointerTwo = headTwo

    while pointerOne is not None and pointerTwo is not None:
        if pointerOne.value < pointerTwo.value:
            if previous is None:
                previous = pointerOne
            else:
                previous.next = pointerOne
                previous = previous.next
            pointerOne = pointerOne.next
        else:
            if previous is None:
                previous = pointerTwo
            else:
                previous.next = pointerTwo
                previous = previous.next
            pointerTwo = pointerTwo.next
    
    if pointerOne is None:
        previous.next = pointerTwo
    elif pointerTwo is None:
        previous.next = pointerOne

    
    return headOne if headOne.value < headTwo.value else headTwo

# 1 -> 2 -> 4 -> 8 -> 11
# 0 -> 3 -> 5 -> 9 -> 13 -> 15

headOne = LinkedList(1)
headOne.next = LinkedList(2)
headOne.next.next = LinkedList(4)
headOne.next.next.next = LinkedList(8)
headOne.next.next.next.next = LinkedList(11)

headTwo = LinkedList(0)
headTwo.next = LinkedList(3)
headTwo.next.next = LinkedList(5)
headTwo.next.next.next = LinkedList(9)
headTwo.next.next.next.next = LinkedList(13)
headTwo.next.next.next.next.next = LinkedList(15)

mergeLinkedLists(headOne, headTwo)