class LinkedList:

    # Initializing the linked list with a head value
    def __init__(self, value):
        
        self.head = {
            'value': value,
            'next': None
        }
        self.tail = self.head
        self.length = 1
    
    # Defining the length function for this data structure
    def __len__(self):
        return len(self.length)
    
    # Creating the append function by taking the new value form the user and creating a node with next value as None Type (null in other languages)
    def append(self, value):
        
        newNode = {
            'value': value,
            'next': None
        }
        
        self.tail['next'] = newNode
        
        self.tail = newNode
        self.length += 1
        
        return self.length
    
    # Creating the prepend function by taking the new value form the user and creating a node with head as this node's next value
    def prepend(self, value):
        
        newNode = {
            'value': value,
            'next': self.head
        }
        
        self.head = newNode
        self.length += 1
        
        return self.length
    
    # Creating a show function to view all the data in this data structure in the form of a list
    def show(self):
        toShow = []
        nextValue = self.head

        # We create the reference value as self.head first and then everytime it loops, the next object will become the nextValue variable
        # The loop goes through the length of the linked list so we don't need to worry about Out Of Range or While Loop's infinite runtime error 
        
        for i in range(self.length):
        
            toShow.append(nextValue['value'])
        
            if i != (self.length-1):
                nextValue = nextValue['next']
        
        return toShow