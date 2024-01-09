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
    
#   def remove(value):
        # Ik the logic but too lazy to implement