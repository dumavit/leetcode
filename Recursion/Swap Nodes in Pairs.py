# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        if head and head.next:
            rest = self.swapPairs(head.next.next)
            head.next.next = head
            head = head.next
            head.next.next = rest
        return head
