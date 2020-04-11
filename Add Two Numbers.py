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
        while True:
            s = remainder
            if l1:
                s += l1.val
            if l2:
                s += l2.val
            curr.val = s % 10
            remainder = s / 10
            curr.next = ListNode()
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return result


print(Solution().addTwoNumbers(a, b))
