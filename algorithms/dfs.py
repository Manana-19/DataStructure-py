def DFSPreOrder(tree, arr):
    
    arr.append(tree['value'])

    if tree['left'] is not None:
        DFSPreOrder(tree['left'], arr)
    
    if tree['right'] is not None:
        DFSPreOrder(tree['right'], arr)
    
    return arr

def DFSInOrder(tree, arr):
    if tree['left'] is not None:
        DFSInOrder(tree['left'], arr)
    
    arr.append(tree['value'])

    if tree['right'] is not None:
        DFSInOrder(tree['right'], arr)

    return arr

def DFSPostOrder(tree, arr):
    if tree['left'] is not None:
        DFSPostOrder(tree['left'], arr)
    
    if tree['right'] is not None:
        DFSPostOrder(tree['right'], arr)

    arr.append(tree['value'])

    return arr