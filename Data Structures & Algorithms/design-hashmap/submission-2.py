class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class MyHashMap:

    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map = [None, None]
        

    def put(self, key: int, value: int) -> None:
        
        if self.size >= self.capacity // 2:
            self.rehash()
        first_tombstone = -1
        curr = self.hash(key)
        while self.map[curr] is not None:
            if self.map[curr].key == key:
                self.map[curr].val = value
                return
                
            if self.map[curr].key == -1 and first_tombstone == -1:
                first_tombstone = curr
            curr = (curr + 1) % self.capacity
        
        if first_tombstone != -1:
            # Before using a tombstone, we must continue searching to ensure
            # the key doesn't exist later in the probe sequence
            search_curr = curr
            while self.map[search_curr] is not None:
                if self.map[search_curr].key == key:
                    self.map[search_curr].val = value
                    return
                search_curr = (search_curr + 1) % self.capacity
            insertion_idx = first_tombstone
        else:
            insertion_idx = curr
            
        self.map[insertion_idx] = Pair(key, value)
        self.size += 1
        

    def get(self, key: int) -> int:
        curr = self.hash(key)

        while self.map[curr] is not None:
            if self.map[curr].key == key:
                return self.map[curr].val
            
            curr = (curr + 1) % self.capacity

        return -1
        

    def remove(self, key: int) -> None:
    
        curr = self.hash(key)

        while self.map[curr] is not None:
            if self.map[curr].key == key:
                self.map[curr] = Pair(-1,-1)
                self.size -=1
                return
            
            curr = (curr + 1) % self.capacity
            
    def rehash(self):

        oldMap = self.map
        self.capacity *= 2
        self.map = [None] * self.capacity
        self.size = 0
        for pair in oldMap:
            if pair and pair.key != -1:
                self.put(pair.key,pair.val)
    
    def hash(self,key):

        return key % self.capacity