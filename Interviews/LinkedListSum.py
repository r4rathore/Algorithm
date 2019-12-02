#You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

#Example:
#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data=None):
        self.root = Node(data)

    def addItem_Head(self, item):
        new_node = Node(item)
        new_node.next = self.root
        self.root = new_node

    def len(self):
        count = 0
        temp = self.root
        while temp.next is not None:
            count += 1
            temp = temp.next
        return count


class Solution:
    def addLinkedList(self, l1: LinkedList, l2: LinkedList):
        num1 = Solution.getListNumber(l1)
        num2 = Solution.getListNumber(l2)
        return num1 + num2

    def getListNumber(list: LinkedList):
        # listSize:int = list.len()
        temp = list.root
        number: int = 0
        place = 0
        while temp is not None and temp.data is not None:
            number += pow(10, place) * temp.data
            temp = temp.next
            place += 1

        return number


l1 = LinkedList(2)
l1.addItem_Head(3)
l1.addItem_Head(5)

l2 = LinkedList(5)
l2.addItem_Head(3)
l2.addItem_Head(2)

sum = Solution().addLinkedList(l1, l2)
print(sum)
