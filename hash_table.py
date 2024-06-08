class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key): 
        #sum of ascii values for all characters mod table size gives us index
        return sum(ord(char) for char in key) % self.size

    def find_pair(self, bucket, key):
        return next((pair for pair in bucket if pair[0] == key), None)

    def insert(self, key, value):
        index = self.hash_function(key)
        pair = self.find_pair(self.table[index], key)
        if pair:
            pair[1] = value
        else:
            self.table[index].append([key, value])
        #Simple
        # for pair in self.table[index]: #[pair[0,1]]- key, value
        #     if pair[0] == key: 
        #         pair[1] = value
        #         return 
        # self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        pair = self.find_pair(self.table[index], key)
        return pair[1] if pair else None
        #Simple
        # for pair in self.table[index]:
        #     if pair[0] == key:
        #         return pair[1]
        # return None
    
    def delete(self, key):
        index = self.hash_function(key)
        pair = self.find_pair(self.table[index], key)
        if pair:
            self.table[index].remove(pair)
        #Simple
        # for i, pair in enumerate(self.table[index]):
        #     if pair[0] == key:
        #         del self.table[index][i]
        #         return 
        # return None
    
    def __repr__(self): #display
        return str(self.table)
