
def mergeSort(arr:list[int]) -> list[int]:

    if len(arr) == 1:
        return arr

    # Dividing the array with recursion
    
    mid=len(arr)//2

    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])    
    
    # Got the divided array
    return Sorted(left, right)
    

# The code to sort while returning a combined array
def Sorted(left, right):

    # Returning if either part is None or empty
    if left is None: return right
    if right is None: return left

    arrayToReturn = []

    leftIndex = 0
    rightIndex = 0

    # Creating while loop till the index of either of the elements goes out of range
    while leftIndex < len(left) and rightIndex < len(right):

        if left[leftIndex] < right[rightIndex]:
            arrayToReturn.append(left[leftIndex])
            leftIndex+=1
        else:
            arrayToReturn.append(right[rightIndex])
            rightIndex+=1

    # Adding up the remaining elements
    arrayToReturn += left[leftIndex:]
    arrayToReturn += right[rightIndex:]
    
    return arrayToReturn
