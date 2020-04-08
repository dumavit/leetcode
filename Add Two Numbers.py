# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = ListNode()
        curr = result
        remainder = 0
        l1_val = l1.val or 0
        l2_val = l2.val or 0
        while l1_val or l2_val or remainder:
            s = l1_val + l2_val + remainder
            curr.val = s % 10
            remainder = s / 10
            curr.next = ListNode()
            curr = curr.next
            l1_val =
        return result


print(Solution().addTwoNumbers(a, b))
