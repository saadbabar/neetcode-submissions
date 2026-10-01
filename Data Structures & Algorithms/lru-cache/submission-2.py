
from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dq = deque()

    def get(self, key: int) -> int:
        if key in self.dq:
            self.dq.remove(key)
            self.dq.append(key)
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if len(self.dq) == self.capacity and key not in self.cache:
            val = self.dq.popleft()
            del self.cache[val]

        self.cache[key] = value
        if key in self.dq:
            self.dq.remove(key)
        self.dq.append(key)

        return None
