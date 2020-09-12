# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    # Write your code here.
    fast = head.next.next
    slow = head.next
    while fast != slow:
        fast = fast.next.next
        slow = slow.next
    
    while head != slow:
        head = head.next
        slow = slow.next
    
    return head
