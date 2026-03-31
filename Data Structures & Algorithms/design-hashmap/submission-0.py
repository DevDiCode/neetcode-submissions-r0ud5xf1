class MyHashMap:
    def __init__(self):
        self.M = 15000  # Number of buckets
        self.buckets = [[] for _ in range(self.M)]

    def _get_index(self, key):
        return key % self.M

    def put(self, key: int, value: int) -> None:
        index = self._get_index(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                return
        self.buckets[index].append((key, value))

    def get(self, key: int) -> int:
        index = self._get_index(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = self._get_index(key)
        self.buckets[index] = [(k, v) for (k, v) in self.buckets[index] if k != key]



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)