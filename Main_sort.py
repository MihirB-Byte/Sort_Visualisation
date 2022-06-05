from Bubble_Sort import *
from quick_sort import *
# insertion_sort, Merge_sort,quick_sort,selection_sort
# import insertion_sort, Merge_sort, quick_sort, selection_sort


class Main_Sort:

    def __init__(self, option_s, list_inp):
        self.sort_option = option_s
        self.user_inputs = list_inp
        self.sorted_list = []
        print("inside the sort selection func")

        if self.sort_option == "1":
            print("inside sort selector if stmt")
            self.sorted_list = BubbleSort(self.user_inputs)

        elif self.sort_option == "2":
            print("inside ins sort cond if stmt")
            sorted_list = insertion_sort.insertionSort(self.user_inputs)
            print("Sorted list with Insert Sort:" + str(sorted_list))
        elif self.sort_option == "3":
            print("inside Merge sort cond if stmt")
            sorted_list = Merge_sort.mergeSort(self.user_inputs)
            print("Sorted list with Merge Sort:" + str(sorted_list))
        elif self.sort_option == "4":
            print("inside quick sort cond if stmt")
            self.sorted_list = QuickSort(self.user_inputs)
            # print("Sorted list with quick Sort:" + str(sorted_list))
        elif self.sort_option == "5":
            print("inside Selection sort cond if stmt")
            sorted_list = selection_sort.selectionSort(self.user_inputs)
            print("Sorted list with selection Sort:" + str(sorted_list))

    def return_sorted_list(self):
        return self.sorted_list





def main():
    print("Select the type of input you want to use: \n")
    input_type = input("1: auto \n" +"2: Manual \n" )
    print(input_type)
    if (input_type == '1'):
        print("generate numbers automatically")
    else:
        user_inputs = [int(x) for x in input("Enter multiple values seperated with comma : ").split(",")] #getting multiple values from the user seperated by space
        print("Choose a number to select the type of sort you want to use: \n")
        sort_selector = input("1: Bubble Sort \n" +"2: Insertion Sort \n" + "3: Merge Sort \n" + "4: Quick Sort \n" + "5: Selection Sort \n " )
        Main_Sort(sort_selector, user_inputs)


    
if __name__ == "__main__": main()

