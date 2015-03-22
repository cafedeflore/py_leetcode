# coding=utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        temp_a = headA
        temp_b = headB
        len_a = 0
        len_b = 0
        while temp_a is not None:
            len_a += 1
            temp_a = temp_a.next

        while temp_b is not None:
            len_b += 1
            temp_b = temp_b.next

        temp_a = headA
        temp_b = headB
        if len_a > len_b:
            for i in range(len_a - len_b):
                temp_a = temp_a.next
        else:
            for i in range(len_b - len_a):
                temp_b = temp_b.next

        while not(temp_a is None and temp_b is None):
            if temp_a.val == temp_b.val:
                return temp_a
            temp_a = temp_a.next
            temp_b = temp_b.next


        return None