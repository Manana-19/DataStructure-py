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
    
    # Creating an insert funciton to insert the value at a specific index in this linked list

    def insert(self, value, index):
        
        # Creating a if-else if- statement to save work in the following cases
        # - If the index is out of range
        # - If the index is 0 So we can just use the function prepend
        # - If the Index is the same length of the data structure so that we can just use the function append

        if (index > self.length):
            return False
        elif (index == 0):
            self.prepend(value)
        elif (index == self.length):
            self.append(value)
        
        # Now going through the "for loop" with the range(index-1) so that we don't have to work that hard
        
        Node = self.head
        for i in range(index-1):
            Node = Node['next']
        
        # After this, We replace the old value with the new one, then creating a new node containing the old value and it's next value
        
        leader = Node
        leader['next'] = {
            'value': value,
            'next': leader['next']
        }
        
        self.length += 1

        return True
    
    def removeValue(self, value):
        
        theList = self.show()

        index=-1
        
        if value not in theList:
            return False
        
        else:
            index=theList.index(value)

        return self.RemoveIndex(index)
    
    def RemoveIndex(self, index):
        
        if (index < 0) or (index >= self.length):
            return False
        
        if index == 0:
            self.head = self.head['next']

        else:

            Node = self.head

            for i in range(index-1):
                Node = Node['next']
        
            Node['next'] = Node['next']['next']
            

        self.length -= 1

        return True