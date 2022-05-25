def selectionSort(alist):

   for i in range(len(alist)):

      # Find the minimum element in remaining
       minPosition = i

       for j in range(i+1, len(alist)):
           if alist[minPosition] > alist[j]:
               minPosition = j
                
       # Swap the found minimum element with minPosition       
       temp = alist[i]
       alist[i] = alist[minPosition]
       alist[minPosition] = temp

   return alist

"""
user_inputs = [int(x) for x in input("Enter multiple values seperated with comma : ").split(" ")] #getting multiple values from the user seperated by space
print("the list is : " + str(user_inputs))


Sorted_list=selectionSort(user_inputs)
print("Sorted list : " + str(Sorted_list)) """