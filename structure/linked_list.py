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
    def append(self, value): # TIme Complexity: O(1)
        
        newNode = {
            'value': value,
            'next': None
        }
        
        self.tail['next'] = newNode
        
        self.tail = newNode
        self.length += 1
        
        return self.length
    
    # Creating the prepend function by taking the new value form the user and creating a node with head as this node's next value
    def prepend(self, value): # Time Complexity : O(1)
        
        newNode = {
            'value': value,
            'next': self.head
        }
        
        self.head = newNode
        self.length += 1
        
        return self.length
    
    # Creating a show function to view all the data in this data structure in the form of a list
    def show(self): # Time Complexity: O(n)
        toShow = []
        nextValue = self.head

        # We create the reference value as self.head first and then everytime it loops, the next object will become the nextValue variable
        # The loop goes through the length of the linked list so we don't need to worry about Out Of Range or While Loop's infinite runtime error 
        
        for i in range(self.length): # O(n)
        
            toShow.append(nextValue['value'])
        
            if i != (self.length-1):
                nextValue = nextValue['next']
        
        return toShow
    
    # Creating an insert funciton to insert the value at a specific index in this linked list

    def insert(self, value, index): # Time Complexity: O (n)
        
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
        for i in range(index-1): # O(n)
            Node = Node['next']
        
        # After this, We replace the old value with the new one, then creating a new node containing the old value and it's next value
        
        leader = Node
        leader['next'] = {
            'value': value,
            'next': leader['next']
        }
        
        self.length += 1

        return True
    
    # Creating a function to remove a value from the linked list
    def removeValue(self, value): # Time Complexity: O(n)
        
        # Getting the list form of the data stucture and check if the value in the data structure exists or not, then grabbing the index

        theList = self.show() # O(n)

        index=-1
        
        if value not in theList:
            return False
        
        else:
            index=theList.index(value)

        # As we get the index from the list function "index", we can now use our self.RemoveIndex Function

        return self.RemoveIndex(index) # O (n)
    
    # Removing the item from the linked list structure with the help of the index as it's parameter
    def RemoveIndex(self, index):
        
        # Invalidating the function on the following condition:
        # - If the index is less than 0
        #  -If the index is greater than or equal to the length of the linked list (the index start from 0 so it should also be not equal to the linked list's length)
        if (index < 0) or (index >= self.length):
            return False
        
        # If the Index is 0, We're just going to replace the head by it's next node and return with Time Complexity of O(1)
        if index == 0:
            self.head = self.head['next']

        # For General Case (except the first case), we're going to traverse the linkedlist with the help of for loop as we did in insert function
        # Then we're going to replace that node with it's next node.
        else:

            Node = self.head

            for i in range(index-1): # O(n)
                Node = Node['next']
        
            Node['next'] = Node['next']['next']
            

        self.length -= 1

        return True
    
    # Reversing the entire linkedlist structure by re-building it.
    def Reverse(self): # Time Complexity: O(n)

        # Grabbing the list form of the linkedlist which will increase the space complexity by O(n)
        Arr = self.show() # O(n)

        # Re creating the linked list data structure with the help of negative indexing in the list
        self.head = {
            'value':Arr[-1],
            'next':None
        }
        self.tail = self.head

        # Looping through the items in the list with negative indexing so that we get the reverse order and use the append function
        for item in Arr[-2::-1]: # O(n)
            self.append(item)
            self.length -= 1
        
        return True