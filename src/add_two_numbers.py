__author__ = 'Nan'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        # if l1 is None or l2 is None:
        #     raise Exception
        result = ListNode(0)
        temp = result
        stored = 0
        while not (l1 is None and l2 is None):
            temp.val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + stored
            if temp.val > 9:
                temp.val %= 10
                stored = 1
            else:
                stored = 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if not (l1 is None and l2 is None):
                temp.next = ListNode(0)
                temp = temp.next
        if stored == 1:
            temp.next = ListNode(1)

        return result

a = ListNode(0)
b = ListNode(1)
s = Solution()
print s.addTwoNumbers(a, b).val