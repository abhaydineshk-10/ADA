arr = [34, 56, 78, 56, 67, 45, 56]
n = len(arr)

for i in range(n -1):
    for j in range(n - i - 1):
        if arr[j] > arr[j +1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            
print("Sorted array:", arr)

#step1:start
#step2:read no of elements n
#step3:read array elements
#step4:i=0 to n-2 repeat steps 5-7
#step5:repeat step 6-7 for j=0 to n-1-2
#step6:if array [j] > array [j+1], swap them
#step7:end inner loop
#step8:end outer loop
#step9:display the sorted array
#step10:stop