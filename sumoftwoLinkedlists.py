# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    dummyNode = LinkedList(0)
    currentNode = dummyNode
    firstHead = linkedListOne
    secondHead = linkedListTwo
    carry = 0
    while firstHead is not None or secondHead is not None or carry != 0:
        firstHeadValue = firstHead.value if firstHead is not None else 0
        secondHeadValue = secondHead.value if secondHead is not None else 0
        
        temp_sum = firstHeadValue + secondHeadValue + carry
        unitsPlace = temp_sum % 10
        newNode = LinkedList(unitsPlace)
        currentNode.next = newNode
        currentNode = newNode

        carry = temp_sum // 10
        firstHead = firstHead.next if firstHead is not None else None
        secondHead = secondHead.next if secondHead is not None else None
    return dummyNode.next
        
