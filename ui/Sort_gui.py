#!/usr/bin/python3


from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Sort_Gui:

    def __init__(self, master):
        master.title('Sort Visualisation')
        

        self.style = ttk.Style()

        self.panedwindow = ttk.Panedwindow(master, orient=VERTICAL)
        self.panedwindow.pack(fill=BOTH, expand=True)

        self.top_frame = ttk.Frame(self.panedwindow, width=100, height=300, relief=SUNKEN)
        self.bottom_frame = ttk.Frame(self.panedwindow, width=400, height=400, relief=SUNKEN)
        self.panedwindow.add(self.top_frame, weight=1)
        self.panedwindow.add(self.bottom_frame, weight=4)

        self.input_frame = ttk.Frame(self.top_frame)
        self.input_frame.place(relx = 0.5, rely = 0.5, anchor = 'center', relwidth = 0.95, relheight = 0.95)
        self.input_frame.config(width=500, height=300, relief='sunken', borderwidth= 5)

        
       





    def submit(self):
        
        self.clear()
        messagebox.showinfo(title='Submiting results', message='Results submitted !')

    def export(self):
        self.clear()
        messagebox.showinfo(title='Reports Exporting !', message='Reports Exported!')

    def clear(self):
        self.exam_center_input.delete(0, 'end')


def main():
    root = Tk()
    sort_gui = Sort_Gui(root)
    root.mainloop()


if __name__ == "__main__": main()
