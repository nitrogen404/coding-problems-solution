# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    if head.next is None:
        return head
    first = None
    second = head
    while second is not None:
        third = second.next
        second.next = first
        first = second
        second = third
    return first
