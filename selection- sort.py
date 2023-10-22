def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
if __name__ == "__main__":
    unsorted_list = [64, 25, 12, 22, 11]
    
    print("Unsorted list:", unsorted_list)
    
    selection_sort(unsorted_list)
    
    print("Sorted list:", unsorted_list)
