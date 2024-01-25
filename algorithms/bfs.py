# Creating the recursion function in order to return the boolean

def Recurstion(q:list, arr:list):
    
    # If the length of the queue is empty then we return the array filled with items by the recursion
    if len(q) == 0 or q is None: return arr

    # Otherwise, we pop the node from the queue
    tree = q.pop(0)

    # If the node has a child then we append it to the queue
    if tree['left'] is not None:
        q.append(tree['left'])

    if tree['right'] is not None:
        q.append(tree['right'])

    # Appending the value in the node into the final array that we're going to return
    arr.append(tree['value'])
    
    # Calling the recursive function
    return Recurstion(q, arr)

# Final function here....
def BFS(tree) -> list:
    return (Recurstion([tree.root], []))