def selectionSort(arr:list[int]) -> [list[int]]:

    # Creating a nested loop below
    for i in range(len(arr)):
        x=i
        # Creating the lowest val variable
        low=arr[i]

        # Creating the second loop below
        for j in range(i, len(arr)):
            
            # Checking if the lowest is actually the lowest in the remaining list
            if arr[j] < low:
                low = arr[j]
                x=j
        
        arr[x], arr[i] = arr[i], arr[x]

    return arr