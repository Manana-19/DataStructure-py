# Creating this Node function to create a node so that I don't have to type the dictionary again and again
def Node(value, Next=None): # Time Complexity: O(1)
    return {'value': value, 'next': Next}

# Creating the Queue Data structure with the help of Linkedlist data structure
class Queue:
    
    # Initializing the Data Structure with a value as it's input
    def __init__(self, value):
        
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def __len__(self):
        return self.length
    
    # Pushing the element to the tail then replacing the tail to the new node we just created.
    def push(self, value): # Time Complexity: O(1)
        
        self.tail['next'] = Node(value)
        self.tail = self.tail['next']
        self.length += 1
        
        return True
    
    # Poping the element from the head because that's the most easiest way to remove an item from the linkedlist data structure
    def pop(self): # Time Complexity: O(1)

        if self.length == 0:
            return None
        
        value = self.head['value']
        self.head = self.head['next']
        self.length -= 1
        
        return value
    
    # Creating a peek function to see and return the last element from the queue (which is the next element to be popped)
    def peek(self): # Time Complexity: O(1)
        return self.tail['value']
    
    # Creating a function to loop through the data structure so that we can create a list and see what data is in our data structure
    def show(self): # Time Complexity: O(n)
        
        CurrentNode = self.head
        toShow = []

        for i in range(self.length):
            toShow.append(CurrentNode['value'])
            CurrentNode=CurrentNode['next']
        
        return toShow