# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, node):
        odd = oddHead = ListNode()
        even = evenHead = ListNode()
        while node:
            odd.next = node
            odd = node
            even.next = node.next
            even = node.next
            node = node.next.next if node.next else None
        odd.next = evenHead.next
        return oddHead.next
