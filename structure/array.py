class Array:

    def __init__(self):
        self.length = 0
        self.data = {}
    
    def __len__(self):
        return self.length

    def get(self, index): # Time Complexity: O(1)
        
        if (self.data[index]):
        
            return self.data[index]
        
        else:
            return None
    
    def Append(self,item): # Time Complexity: O(1) for static, O(n) for dynamic while alloting more memory
        
        if (item):
        
            self.data[self.length] = item
            self.length += 1
            return self.length-1
        
        else:
            return None
    
    def Pop(self): # Time Complexity: O(1)
        
        if self.length>1:

            # Fetching the last item on the Array, then decrements the length of the array and then deletes the data and return the data that we have stored in toReturn Variable
            toReturn = self.data[self.length-1]
            self.length -= 1
            del self.data[self.length-1]
            return toReturn
        
        else:
            return None
    
    def Remove(self, item): # Time Complexity: O(1)
        
        if item not in self.data:
            return None
        
        else:
            # Defining a variable to use in order to find the element's index in the Array
            indexToShift=0
            
            # Looping through the Array to fetch the index of the element
            for index,data in self.data.items():
                if data==item:
                    indexToShift=index
                    break
            
            # Looping through the range of the index that we have to shift till the end of the Array
            for i in range(indexToShift, self.length-1):
                
                # Shifting all the elements by their successor
                self.data[i] = self.data[i+1]
            
            # Deleting the last element since it's going to be the duplicate of the second last element and then decrementing the length of the Array 
            del self.data[self.length-1]
            self.length-=1
            
            return self.length

    