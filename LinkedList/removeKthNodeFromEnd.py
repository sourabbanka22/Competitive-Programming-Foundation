# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
	behind = head
	front = head
	counter = 1
	while counter <= k:
		front = front.next
		counter += 1
	if front == None:
		head.value = head.next.value
		head.next = head.next.next
		return
	while front.next is not None:
		front = front.next
		behind = behind.next
	behind.next = behind.next.next