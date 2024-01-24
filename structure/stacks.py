# Creating this Node function to create a node so that I don't have to type the dictionary again and again
def Node(value, Next=None): # Time Complexity: O(1)
    return {'value': value, 'next': Next}

# Creating the Stacks Data Structure using LinkedList
class Stacks:
    
    # Initializing the Data Structure with a value as it's input
    def __init__(self, value):
        
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def __len__(self):
        return self.length
    
    # Pushing the element to the head of the data structure so that we can easily pop it out with the time complexity of O(1)
    
    def push(self, value): # Time Complexity: O(1)
    
        Head = self.head
        self.head = Node(value, Head)
        self.length += 1
    
        return True
    
    # Poping the element out from the data structure by replacing the head by it's next node

    def pop(self): # Time Complexity: O(1)
        
        if self.length == 0:
            return None
        
        value = self.head['value']
        self.head = self.head['next']
        self.length -= 1
        
        return value
    
    # Creating a function which allows us to see what is on the top of the stack (which is on the tail here and it's the next value to be popped)
    def peek(self): # Time Complexity: O(1)
        return self.tail['value']
    
    # Creating a function to loop through the data structure so that we can create a list and see what data is in our data structure
    def show(self): # Time Complexity: O(n)
        CurrentNode = self.head
        toShow = []
        i=0
        while i < self.length:
            toShow.append(CurrentNode['value'])
            CurrentNode=CurrentNode['next']
            i+=1

        
        # Reversing the list just so that we can have it in the right order of insertion
        return toShow[::-1]