# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    start = head
    prev = None
    while head:
        if head.val == val:
            if prev:
                prev.next = head.next
            else:
                start = head.next
        else:
            prev = head

        head = head.next
    return start