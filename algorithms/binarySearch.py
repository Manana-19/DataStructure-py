def binarySearch(arr:list[int], item:int) -> bool:
    
    # Getting the length of the array since we have to access it multiple times so we're not gonna call the len() function again and again...
    length = len(arr)

    
    # Checking if the length of the array is 0 so that we can end the recursion.
    if (length == 0) or (length == 1 and arr[0] != item):
        return False

    # Dividing the Array
    mid=(length//2)
    

    # Returning True if the Mid item is actually the item we wanna look for...
    if arr[mid] == item: 
        return True
    
    # If the Item is bigger than the mid item then we divide the array into the right side of the mid item
    elif arr[mid] > item:
        return binarySearch(arr[:mid], item)
    
    # If the Item is smaller than the mid item then we divide the array into the left side of the mid item
    elif arr[mid] < item:
        return binarySearch(arr[mid:], item)