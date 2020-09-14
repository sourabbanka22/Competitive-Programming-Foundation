def rearrangeLinkedList(head, k):
    # Write your code here.
    smaller = None
    bigger = None
    kth = None
    kthLeft = None
    biggestLeft = None
    smallestLeft = None
    containsK = False
    current = head
    
    while current is not None:
        if current.value == k:
            containsK = True
            if kthLeft is None:
                kthLeft = current
            else:
                kth.next = current
            kth = current
            current = current.next
            continue
        elif current.value < k:
            if smaller is None:
                smaller = current
                smallestLeft = current
            else:
                smaller.next = current
                smaller = smaller.next
        else:
            if bigger is None:
                bigger = current
                biggestLeft = current
            else:
                bigger.next = current
                bigger = bigger.next
        current = current.next
    
    if kth is not None:
        kth.next = biggestLeft
        if smaller is not None:
            smaller.next = kthLeft
            head = smallestLeft
        else:
            head = kthLeft
    else:
        if smaller is not None:
            smaller.next = biggestLeft
            head = smallestLeft
        else:
            head = biggestLeft
    if bigger is not None:
        bigger.next = None
    
    return head


# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
