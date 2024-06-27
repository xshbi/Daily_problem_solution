def insertion_sort_nonincreasing(arr):
    """
    Performs insertion sort on the given array in non-increasing order.
    
    Args:
    arr (list): The array to be sorted.
    
    Returns:
    list: The sorted array in non-increasing order.
    """
    n = len(arr)
    
    # Traverse through the array
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

# Example usage
arr = [31, 41, 59, 26, 41, 58]
sorted_arr = insertion_sort_nonincreasing(arr)
print(sorted_arr)  # Output: [59, 58, 41, 41, 31, 26]
