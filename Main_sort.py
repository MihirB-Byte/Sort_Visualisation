#from Bubble_Sort, insertion_sort, Merge_sort,quick_sort,selection_sort 
import Bubble_Sort, insertion_sort, Merge_sort, quick_sort, selection_sort

sort_selector = 0
class Main_Sort:

    def __init__(self, sort_option, list_inp):
        self.sort_selector = sort_option
        self.user_inputs = list_inp
        
    def sort_selection (self):

        print("inside the sort selection func")

        if self.sort_selector == "1":
            print("inside sort selector if stmt")
            Sorted_list = Bubble_Sort.bubbleSort(self.user_inputs)
            print("Sorted list with BBl Sort:" + str(Sorted_list))
        elif self.sort_selector == "2":
            print("inside ins sort cond if stmt")
            Sorted_list = insertion_sort.insertionSort(self.user_inputs)
            print("Sorted list with Inser Sort:" + str(Sorted_list))
        elif self.sort_selector == "3":
            print("inside Merge sort cond if stmt")
            Sorted_list = Merge_sort.mergeSort(self.user_inputs)
            print("Sorted list with Merge Sort:" + str(Sorted_list))
        elif self.sort_selector == "4":
            print("inside quick sort cond if stmt")
            Sorted_list = quick_sort.quicksort(self.user_inputs)
            print("Sorted list with quick Sort:" + str(Sorted_list))
        elif self.sort_selector == "5":
            print("inside Selection sort cond if stmt")
            Sorted_list = selection_sort.selectionSort(self.user_inputs)
            print("Sorted list with selection Sort:" + str(Sorted_list))
        
        return Sorted_list
    


def main():

    print("Select the type of input you want to use: \n")
    input_type = input("1: auto \n" +"2: Manual \n" )
    if (input_type == 1):
        user_inputs = [int(x) for x in input("Enter multiple values seperated with comma : ").split(",")] #getting multiple values from the user seperated by space
        print("Choose a number to select the type of sort you want to use: \n")
        sort_selector = input("1: Bubble Sort \n" +"2: Insertion Sort \n" + "3: Merge Sort \n" + "4: Quick Sort \n" + "5: Selection Sort \n " )

    else:
        print("generate numbers automatically")
    
    Main_Sort(sort_selector, user_inputs)


    
if __name__ == "__main__": main()

