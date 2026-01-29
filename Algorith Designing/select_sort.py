def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
    
# step 1 : Start from first element.
# step 2 : Assume it is smallest.
# step 3 : Compare with the next element.
# step 4 : Find smallest value.
# step 5 : Note its position.
# step 6 : Swap with first unstorted element.
# step 7 : Move to next index.
# step 8 : Repeat for remaining elements.
# step 9 : Contiue till last element.
# step 10 : Array becomes sorted.  