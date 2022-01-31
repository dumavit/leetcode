class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map_volume = 10000
        self.arr = [[] for _ in range(self.hash_map_volume)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        arr_index = self.hashcode(key)
        elements = self.arr[arr_index]
        for index in range(len(elements)):
            item_key = elements[index][0]
            if item_key == key:
                elements[index][1] = value
                return None
        self.arr[arr_index].append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        arr_index = self.hashcode(key)
        for item_key, item_value in self.arr[arr_index]:
            if item_key == key:
                return item_value
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        arr_index = self.hashcode(key)
        self.arr[arr_index] = [
            item for item in self.arr[arr_index] if item[0] != key]

    def hashcode(self, key):
        return key % self.hash_map_volume


# Your MyHashMap object will be instantiated and called as such:
hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
hashMap.get(1)
hashMap.get(3)
hashMap.put(2, 1)
hashMap.get(2)
hashMap.remove(2)
hashMap.get(2)
