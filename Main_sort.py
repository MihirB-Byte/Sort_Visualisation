#from Bubble_Sort, insertion_sort, Merge_sort,quick_sort,selection_sort 
import Bubble_Sort, insertion_sort, Merge_sort, quick_sort, selection_sort



Sorted_list=[]
x=[]
user_inputs=[]
sort_selector=0

if __name__ == "__main__":

    print("Choose a number to select the type of sort you want to use: \n")
    sort_selector = input("1: Bubble Sort \n" +"2: Insertion Sort \n" + "3: Merge Sort \n" + "4: Quick Sort \n" + "5: Selection Sort \n " )


    user_inputs = [int(x) for x in input("Enter multiple values seperated with comma : ").split(" ")] #getting multiple values from the user seperated by space
    
    if sort_selector == "1":
        print("inside sort selector if stmt")
        Sorted_list = Bubble_Sort.bubbleSort(user_inputs)
        print("Sorted list with BBl Sort:" + str(Sorted_list))
    elif sort_selector == "2":
        print("inside ins sort cond if stmt")
        Sorted_list = insertion_sort.insertionSort(user_inputs)
        print("Sorted list with Inser Sort:" + str(Sorted_list))
    elif sort_selector == "3":
        print("inside Merge sort cond if stmt")
        Sorted_list = Merge_sort.mergeSort(user_inputs)
        print("Sorted list with Merge Sort:" + str(Sorted_list))
    elif sort_selector == "4":
        print("inside quick sort cond if stmt")
        Sorted_list = quick_sort.quicksort(user_inputs)
        print("Sorted list with quick Sort:" + str(Sorted_list))
    elif sort_selector == "5":
        print("inside Selection sort cond if stmt")
        Sorted_list = selection_sort.selectionSort(user_inputs)
        print("Sorted list with selection Sort:" + str(Sorted_list))

    
    
