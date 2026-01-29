from array import array
a = array('i', [4, 2, 7, 1])
key = 7

found = False
for index in range(len(a)):
    if a[index] == key:
        print("Key found at index:", index)
        found = True
        break

if not found:
    print("Key not found")
    
    
# step 1: start 
# step 2: read n
# step 3: read the array elements
# step 4: read     
# step 5: set i = 0 
# step 6: repeat while i < n
#         if arr[i] == key
#         print "element found in the position i + 1"
#         stop
#         else
#         increase i by 1
# step 7: if i =n, print "element not found"
#step 8: stop 
