# Bubble sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def BubbleSort(arr: list[int]) -> list[int]:

    # Creating nested list to check the items individually and swap if the condition is met

    for i in range(len(arr)):

        for j in range(len(arr)):
        
            if arr[i] < arr[j]:

                arr[i], arr[j] = arr[j], arr[i]

    # Returning the sorted Array

    return arr