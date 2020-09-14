def shiftLinkedList(head, k):
    # Write your code here.
    newHead = None
    prev = None
    current = head
    length = 0
    while current is not None:
        current = current.next
        length += 1
    
    current = head
    if k >= 0:
        movements = length - (k % length)
    else:
        movements = (length - k) % length
    
    while movements != 0:
        prev = current
        current = current.next
        movements -=1
    if prev is not None and prev.next is not None:
        newHead = current
        prev.next = None
        current = newHead
        while current.next is not None:
            current = current.next
        current.next = head

    return newHead if newHead is not None else head
    

# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
