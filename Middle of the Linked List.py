# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head.next
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
        return slow
