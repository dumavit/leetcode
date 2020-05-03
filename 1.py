class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.uniq = dict()
        self.seen = set()
        self.head = LinkNode(None)
        self.tail = LinkNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        for num in nums:
            self.add(num)

    def _ins(self, value) -> None:
        """insert at tail"""
        node = LinkNode(value)
        node.next = self.tail
        node.prev = self.tail.prev
        node.next.prev = node
        node.prev.next = node
        self.uniq[value] = node
        self.seen.add(value)

    def _del(self, value: int) -> None:
        """delete given value"""
        node = self.uniq[value]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.uniq.pop(value)

    def showFirstUnique(self) -> int:
        return self.head.next.val if len(self.uniq) > 0 else -1

    def add(self, value: int) -> None:
        if value in self.uniq:
            return self._del(value)
        if value in self.seen:
            return
        self._ins(value)
