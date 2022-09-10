class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    slowPointer = head
    fastPointer = head
    for i in range(k):
        fastPointer = fastPointer.next

    if fastPointer is None:
        head.value = head.next.value
        head.next = head.next.next
        return 

    while fastPointer.next is not None:
        fastPointer = fastPointer.next
        slowPointer = slowPointer.next
    slowPointer.next = slowPointer.next.next
