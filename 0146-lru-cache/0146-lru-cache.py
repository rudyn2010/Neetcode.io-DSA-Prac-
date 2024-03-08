class LRUCache:

    def __init__(self, capacity: int):
        self.lru = {}
        self.stk = deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
            If key is present in the cache, 
                Take the value, Remove the node from the queue and add it to the front of the queue
            Else,
                Return -1
        """
        
        if key in self.lru:
            value = self.lru[key]
            self.stk.remove(key)
            self.stk.append(key)
            return value
        
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """
            Put Key in cache:
                1. If Key is already present in Cache, remove the key from the queue and add it to the front (to preserve order)
                2. If Key is not in the Cache, 
                    Remove the oldest one in the cache, and Add the new key to the queue and the cache
        """

        if key not in self.lru:
            if len(self.stk) == self.capacity :
                old = self.stk.popleft()
                del self.lru[old]
        
        else:
            self.stk.remove(key)
            
        self.stk.append(key)
        self.lru[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)