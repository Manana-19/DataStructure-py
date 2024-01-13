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
        # Creating the new node
        NewNode = NodeConstruct(value)
        # Checking if the root node does not exists
        if (self.root == None):
            self.root = NewNode
        else:
            # Traversing process then placing the new node there
            Node = traverse(self.root, value)
            if value > Node['value']:
                Node['right'] = NewNode
            elif value < Node['value']:
                Node['left'] = NewNode
        
    def lookup(self, value):
        # Traversing the node then checking if the node exists or not
        Node=traverse(self.root, value)
        
        # If the node exists, we return the node itself.
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
                break
        
    # Doing the main process of deletion

        # Deciding where our main node is....
        if (parentNode['left'] == childNode):
            toSelect = 'left'
        else:
            toSelect = 'right'

        
        # If the child node has no children
        if (childNode['right'] is None) and (childNode['left'] is None):
            parentNode[toSelect] = None
        

        # If the child node has a child, we replace it with its successor
        else:
        
            if (childNode['right'] is None) and (childNode['left'] is not None):
                # Replacing the child node with its left node
                parentNode[toSelect] = childNode['left']
            
            elif (childNode['right'] is not None) and (childNode['left'] is None):
                # Replacing the child node with its right node
                parentNode[toSelect] = childNode['right']

            else:
        
                # Creating Temp pair of child nodes
        
                tempParentNode = childNode
                tempChildNode = childNode['right']
                
                while True:

                    # If the given child node's child has no left node
        
                    if tempChildNode['left'] is None:
                        
                        parentNode[toSelect] = {
                            'value':tempChildNode['value'],
                            'right':tempChildNode['right'],
                            'left':tempParentNode['left']
                        }

                        break

                    # If the given child node's child has no right child
                    elif tempChildNode['right'] is None:

                        parentNode[toSelect] = {
                            'value':tempChildNode['value'],
                            'right':tempParentNode['right'],
                            'left':tempChildNode['left']
                        }
                    
                        break