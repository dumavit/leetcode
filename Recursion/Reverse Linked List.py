# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val}->'


class Solution:
    def reverseList(self, node):
        if node and node.next:
            rest = self.reverseList(node.next)
            node.next.next = node
            node.next = None
            node = rest
        return node


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(6)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
res = Solution().reverseList(ListNode())
while res:
    print(res, end=' ')
    res = res.next

