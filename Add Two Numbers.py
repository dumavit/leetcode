# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        remainder = 0
        val1 = l1.val
        val2 = l2.val
        result = ListNode(val1+val2)
        while True:
            val1 = l1.next.val
            val2 = l2.next.val
            s = val1 + val2 + remainder
            result.next = ListNode(s % 10)
            remainder = s / 10
        return result
