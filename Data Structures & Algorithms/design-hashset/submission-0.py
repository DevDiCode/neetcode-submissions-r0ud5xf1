class MyHashSet:
    def __init__(self):
        self.M = 15000  # Number of buckets
        self.buckets = [[] for _ in range(self.M)]

    def _get_index(self, key):
        return key % self.M

    def add(self, key: int) -> None:
        index = self._get_index(key)
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        index = self._get_index(key)
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self._get_index(key)
        return key in self.buckets[index]

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)