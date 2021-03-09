# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA.next and headB.next:
            return headA.val == headB.val and self.getIntersectionNode(headA.next, headB.next)
        if headA.next and not headB.next:
            return self.getIntersectionNode(headA.next, headB)
        if not headA.next and headB.next:
            return self.getIntersectionNode(headA, headB.next)
        return headA.val == headB.val


print(Solution().getIntersectionNode())