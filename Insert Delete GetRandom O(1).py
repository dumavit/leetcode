from random import random
from math import floor


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.elements = []
        self.hashMap = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.hashMap:
            return False
        self.elements.append(val)
        self.hashMap[val] = len(self.elements)-1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        valIndex = self.hashMap.pop(val, None)
        if valIndex is None:
            return False
        if valIndex == len(self.elements) - 1:
            self.elements.pop()
        else:
            last_element = self.elements.pop()
            self.elements[valIndex] = last_element
            self.hashMap[last_element] = valIndex
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.elements[floor(random()*len(self.elements))]


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
