class Node:
    def __init__(self, value):
        self.value = value
        self.prev = self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        return node

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.tail:
            self.tail = node.prev
        if node == self.head:
            self.head = node.next

    def __str__(self):
        result = 'head::    '
        node = self.head
        while node:
            result += str(node.value) + ', '
            node = node.next
        result += '   ::tail'
        return result


class FirstUnique:
    def __init__(self, nums):
        self.linked_list = LinkedList()
        self.numsDict = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self):
        head = self.linked_list.head
        # print(self.linked_list)
        return head.value if head else -1

    def add(self, value):
        if value in self.numsDict:
            self.linked_list.remove(self.numsDict.get(value))
        else:
            node = self.linked_list.add(value)
            self.numsDict[value] = node


# Your FirstUnique object will be instantiated and called as such:
firstUnique = FirstUnique([2, 3, 5])
firstUnique.showFirstUnique()  # return 2
firstUnique.add(5)             # the queue is now [2,3,5,5]
firstUnique.showFirstUnique()  # return 2
firstUnique.add(2)             # the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique()  # return 3
firstUnique.add(3)             # the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique()  # return 3
firstUnique.add(35)             # the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique()  # return -1
firstUnique.add(36)             # the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique()  # return -1
firstUnique.add(35)             # the queue is now [2,3,5,5,2,3]
firstUnique.add(36)             # the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique()  # return -1
for i in range(100, 200):
    firstUnique.add(i)
for i in range(101, 199):
    firstUnique.add(i)
firstUnique.showFirstUnique()  # return -1
