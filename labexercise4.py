import tkinter
import tkinter.messagebox

class HappybirthdayGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, \
                                   text= "Do you want to text happy birthday to Chinwe?")
        self.radio_var = tkinter.IntVar()
        #self.radio_var.set(1)
        self.opt1 = tkinter.Radiobutton(self.top_frame, \
            text='Yes', variable=self.radio_var, \
                                        value=1)
        self.opt2 = tkinter.Radiobutton(self.top_frame, \
                                        text='No', variable=self.radio_var, \
                                        value=2, command=self.main_window.destroy)
        self.opt1.pack()
        self.opt2.pack()

        self.msg_entry = tkinter.Entry(self.top_frame, \
                                    width=10)
        
        self.label1.pack(side='left')
        self.msg_entry.pack(side='left')
        
        self.send_button = tkinter.Button(self.bottom_frame, \
                                          text= "Send with love", \
                                          command=self.txt_something)
        self.quit_button = tkinter.Button(self.bottom_frame, \
                                          text= "Don't send", \
                                          command= self.main_window.destroy)
        self.send_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        
    
    def txt_something(self):
        tkinter.messagebox.showinfo('1 new message from Chinwe', "Thank you for the sweet message")

happy_birthdaymsg = HappybirthdayGUI()
tkinter.mainloop()