def binarySearch(arr:list[int], item:int) -> bool:
    
    length = len(arr)

    if (length == 0) or (length == 1 and arr[0] != item):
        return False

    mid=(length//2)
    
    if arr[mid] == item: 
        return True
    elif arr[mid] > item:
        return binarySearch(arr[:mid], item)
    elif arr[mid] < item:
        return binarySearch(arr[mid:], item)