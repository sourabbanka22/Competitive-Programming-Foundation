def reverseLinkedList(head):
    left = None
    mid = head
    right = head.next

    while right is not None:
        mid.next = left
        left = mid
        mid = right
        right = right.next
	mid.next = left
	
    return mid
