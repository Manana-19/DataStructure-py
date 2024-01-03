class HashTable:

    # Initializing a HashTable through the given size and creating an empty linked list to avoid collisions
    def __init__(self, size):
        self.data = list([] for _ in range(size))
        self.length = size

    # Creating a hash function that grabs the address of each key and put the pair of key and value in the hash table
    def __hash__(self, key) -> int:
        
        Hash = 0
        
        for i in range(len(key)):
        
            Hash = (Hash + ord(key[i])*i)%self.length
        
        return Hash
    
    # Set Function for the hash table
    def set(self, key, value): # Time Complexity: O(1)
        
        address = self.__hash__(key) # Assuming the time complexity of the function to O(1)
        
        self.data[address].append([key, value]) # O(1)

    # Get Function for the hash table
    def get(self, key): # Time Complexity: O(1) [O(n) in collisions case]
        
        address = self.__hash__(key)
        data = self.data[address]
        
        if (data.__len__() != 0):
        
            for i in range(len(data)): # O(1) if the collision doesn't occur
        
                if (data[i][0] == key):
        
                    return data[i][1]
    
    # Keys function for the hash table where we get the all values in hash table
    def keys(self): # Time Complexity: O(n)
        
        arr = []
        
        for item in self.data: # O(n)
        
            if (item.__len__() != 0):
        
                for x in item:
        
                    arr.append(x[1])
        
        return arr