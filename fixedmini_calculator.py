import tkinter 
import tkinter.messagebox

class MiniCalculatorGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Mini Calculator")
        
        # Frame
        self.top_frame = tkinter.Frame(self.main_window)

        self.middle_frame = tkinter.Frame(self.main_window)

        self.bottom_frame = tkinter.Frame(self.main_window)

        # Labels
        self.label1 = tkinter.Label(self.top_frame, \
            text="Enter two numbers: ")
    
        # Number Entries
        self.number_entry1 = tkinter.Entry(self.top_frame, \
            width=10)

        self.number_entry2 = tkinter.Entry(self.top_frame, \
            width=10)

        self.value = tkinter.StringVar()

        # Middle Frame

        self.label2 = tkinter.Label(self.middle_frame, \
            text="Result: ")
        
        self.result_label = tkinter.Label(self.middle_frame, \
            textvariable= self.value)

        # Bottom Frame
        self.add_button = tkinter.Button(self.bottom_frame, \
            text='+', \
                command=self.addi)

        self.subtract_button = tkinter.Button(self.bottom_frame,\
            text='-', \
                command=self.subt)

        self.multiply_button = tkinter.Button(self.bottom_frame, \
            text='*', \
                command=self.multpli)

        self.divide_button = tkinter.Button(self.bottom_frame, \
            text='/', \
                command=self.divi)

        self.quit_button = tkinter.Button(self.bottom_frame, \
            text='Quit', \
            command= self.main_window.destroy)

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        self.label1.pack(side='left')
        self.label2.pack(side='left')
        self.result_label.pack(side='left')

        self.number_entry1.pack(side='left')
        self.number_entry2.pack(side='left')

        self.add_button.pack(side='left')
        self.subtract_button.pack(side='left')
        self.multiply_button.pack(side='left')
        self.divide_button.pack(side='left')
        self.quit_button.pack(side='right')

    def addi(self):
        entry1 = float(self.number_entry1.get())
        entry2 = float(self.number_entry2.get())
        result = float(entry1 + entry2)
        self.value.set(result)
    
    def subt(self):
        entry1 = float(self.number_entry1.get())
        entry2 = float(self.number_entry2.get())
        result = float(entry1 - entry2)
        self.value.set(result)

    def multpli(self):
        entry1 = float(self.number_entry1.get())
        entry2 = float(self.number_entry2.get())
        result = float(entry1 * entry2)
        self.value.set(result)

    def divi(self):
        entry1 = float(self.number_entry1.get())
        entry2 = float(self.number_entry2.get())
        if entry2 == 0:
            result = "Division by zero error!!!"
            self.value.set(result)
        else:
            result = float(entry1 / entry2)
            self.value.set(result)

minicalcgui = MiniCalculatorGUI()
tkinter.mainloop()