# O(N) time | O(1) space
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    tortise = head.next
    hare = head.next.next
    while hare != tortise:
        tortise = tortise.next
        hare = hare.next.next
    tortise = head
    while tortise != hare:
        tortise = tortise.next
        hare = hare.next
    return hare
    
