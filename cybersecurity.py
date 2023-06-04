import tkinter 
import tkinter.messagebox

class WorldClassSecurity():
    def __init__(self, numguesses, correct_password):
        self.numguesses = numguesses
        self.correct_password = correct_password

#Create derived class(Inheritance)      
class GuessPasswordGUI(WorldClassSecurity):
    def __init__(self):
        super().__init__(4, "I1stw2DLwIw4yrs&immH")

        self.login_window = tkinter.Tk()
        
        self.login_window.title("Diamond Bank User Login")

        self.top_frame = tkinter.Frame(self.login_window)

        self.bottom_frame = tkinter.Frame(self.login_window)

        self.prompt1 = tkinter.Label(self.top_frame, \
            text="Password: ")
        
        self.password_entry = tkinter.Entry(self.top_frame, \
            width=22)

        self.hint_button = tkinter.Button(self.bottom_frame, \
            text='Hint', \
                command=self.hintanswer)
        
        self.enter_button = tkinter.Button(self.bottom_frame, \
            text='Enter', \
                command=self.check_password)
        
        self.end_button = tkinter.Button(self.bottom_frame, \
            text="Quit", \
                command=self.login_window.destroy)

        # Set number attempt
        self.remaining_attempts = self.numguesses - 1

        # PACKS
        self.top_frame.pack()
        self.bottom_frame.pack()

        self.prompt1.pack(side='left')
        self.password_entry.pack(side='left')

        self.end_button.pack(side='left')
        self.hint_button.pack(side='left')
        self.enter_button.pack(side='right')

    # Commands
    def hintanswer(self):
        tkinter.messagebox.showinfo("Hint", "I first went to Disneyland when I was 4 years old and it made me happy")

    def check_password(self):
        userentry = self.password_entry.get()
        if userentry == self.correct_password:
            tkinter.messagebox.showinfo("Success", "Password is correct!")
            self.login_window.destroy()
        else:
            self.numguesses -= 1

        if self.numguesses == 0:
            tkinter.messagebox.showerror("Account Locked", "Too many attempts made, Account holder notified!")
            self.login_window.destroy()

        else:
            tkinter.messagebox.showwarning("Failed", f"Incorrect password. {self.numguesses} attempts remaining.")
            self.password_entry.delete(0, tkinter.END)

Diamond_bank = GuessPasswordGUI()
tkinter.mainloop()