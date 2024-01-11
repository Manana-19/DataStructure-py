def NodeConstruct(value):
    return {'value':value, 'right': None, 'left': None}

def traverse(Node, value):

    if (value > Node['value']):
        if (Node['right'] is not None):
            return traverse(Node['right'], value)
        else: 
            return Node
    
    elif (value < Node['value']):
        if (Node['left'] is not None):
            return traverse(Node['left'], value)
        else:
            return Node
    
    elif (value == Node['value']):
        return Node
        

class BST:
    
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        NewNode = NodeConstruct(value)
        if (self.root == None):
            self.root = NewNode
        else:
            Node = traverse(self.root, value)
            if value > Node['value']:
                Node['right'] = NewNode
            elif value < Node['value']:
                Node['left'] = NewNode
        
    def lookup(self, value):
        Node=traverse(self.root, value)
        if Node is not None:
            return Node
        else:
            return None
    
    def remove(self, value):

        # Checking if the value exists in the BST
        if (self.lookup(value) is None): 
            return None

        parentNode = None
        childNode = self.root

        # Using the loop to traverse
        while True:
        
            if value > childNode['value']:
                parentNode , childNode = childNode, childNode['right']
        
            elif value < childNode['value']:
                parentNode , childNode = childNode, childNode['left']
        
            elif value == childNode['value']:
        
                print(parentNode,'parent')
                print(childNode,'child')
        
                break
        
        # Doing the main process of deletion
        if parentNode['left'] == childNode:
            parentNode['left'] = None
        
        elif parentNode['right'] == childNode:
            parentNode['right'] = None

        


