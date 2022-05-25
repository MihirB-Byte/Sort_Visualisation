
print("inside Insert sort")
"""
def insertionSort(nlist):
   for index in range(1,len(nlist)):

     currentvalue = nlist[index]
     position = index

     while position>0 and nlist[position-1]>currentvalue:
         nlist[position]=nlist[position-1]
         position = position-1

     nlist[position]=currentvalue
  return nlist
"""
     
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
    return arr

"""
user_inputs = [int(x) for x in input("Enter multiple values seperated with comma : ").split(" ")] #getting multiple values from the user seperated by space
print("the list is : " + str(user_inputs))

Sorted_list=insertionSort(user_inputs)
print("Sorted list : " + str(Sorted_list))

"""