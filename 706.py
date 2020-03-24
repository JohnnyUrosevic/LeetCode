class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.table = [[] for _ in range(self.size)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        i = hash(key) % self.size
        
        bucket = self.table[i]
        for j in range(len(bucket)):
            if key == bucket[j][0]:
                bucket[j][1] = value
                return
                
        self.table[i].append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        i = hash(key) % self.size
        bucket = self.table[i]

        if bucket:
            for item in bucket:
                if key == item[0]:
                    return item[1]
            
            return -1
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        i = hash(key) % self.size
        
        bucket = self.table[i]
        for j in range(len(bucket)):
            if key == bucket[j][0]:
                del(self.table[i][j])
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)