
class BubbleSort:
    def __init__(self, list_inp):
        self.user_inputs = list_inp
        for passnum in range(len(self.user_inputs)-1, 0, -1):
            for i in range(passnum):
                if self.user_inputs[i]>self.user_inputs[i+1]:
                    temp = self.user_inputs[i]
                    self.user_inputs[i] = self.user_inputs[i+1]
                    self.user_inputs[i+1] = temp
        print("Sorted list with BBl Sort:" + str(self.user_inputs))



def main():
    BubbleSort(list_inp)

if __name__ == "__main__": main()