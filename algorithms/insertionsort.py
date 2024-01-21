def InsertionSort(arr:list[int]) -> list[int]:

    for i in range(1, len(arr)):

        if arr[i] < arr[i-1]:

            if arr[i] < arr[0]:
                
                arr.insert(0, arr.pop(i))

            else:

                for j in range(i):

                    if arr[i] < arr[j]:

                        # I have to insert it in the middle of the list

                        arr.insert(j, arr.pop(i))
    
    return arr


