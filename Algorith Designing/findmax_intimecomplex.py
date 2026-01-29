arr = [10, 5, 25, 40, 55]
max_element = arr[0]
for i in range(1, len(arr)):
    if arr[i] > max_element:
        max_element = arr[i]
print("Maximum element is:", max_element)

#step1:Start 
#step2:Read the array
#step3:Assume first element with the max
#step4:compare each element is greator, update max
#step5:Print the maxinum value 
#step6:stop