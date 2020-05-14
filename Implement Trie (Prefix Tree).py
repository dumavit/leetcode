class Node:
    def __init__(self):
        self.terminal = False
        self.children = {}

    def __str__(self):
        return str(list(self.children.keys())) + ' terminal: ' + str(self.terminal)


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        currNode = self.root
        for char in word:
            if char in currNode.children:
                currNode = currNode.children[char]
            else:
                nextNode = Node()
                currNode.children[char] = nextNode
                currNode = nextNode
        currNode.terminal = True

    def search(self, word):
        currNode = self.root
        for char in word:
            if char in currNode.children:
                currNode = currNode.children[char]
            else:
                return False
        return currNode.terminal

    def startsWith(self, prefix):
        currNode = self.root
        for char in prefix:
            if char in currNode.children:
                currNode = currNode.children[char]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
word = 'apple'
obj = Trie()
obj.insert(word)
print(1, obj.search('apple'))
print(2, obj.startsWith('app'))
