#class bblsort(object):

print(" in bbl sort ")

def bubbleSort(user_inputs):
    for passnum in range(len(user_inputs)-1,0,-1):
        for i in range(passnum):
            if user_inputs[i]>user_inputs[i+1]:
                temp = user_inputs[i]
                user_inputs[i] = user_inputs[i+1]
                user_inputs[i+1] = temp
    #print("user inputs :" + str(user_inputs))
    return user_inputs


"""
user_inputs = [int(x) for x in input("Enter multiple values seperated with comma : ").split(" ")] #getting multiple values from the user seperated by space
print("the list is : " + str(user_inputs))

Sorted_list= bubbleSort(user_inputs)
print("Sorted List : " + str(Sorted_list))

"""