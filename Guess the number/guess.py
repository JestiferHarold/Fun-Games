from tkinter import *
from random import randint

class game:
    def __init__(self, window):
        self.window = window
        window.title("Guessing Game")
        window.geometry("400x400")
        self.label = Label(window, text = "Enter an number between 1 - 100")
        self.label.pack()
        self.butt = Button(window, text = "Submit", command = self.same_guess)
        self.entry = Entry(window)
        self.entry.pack()
        self.butt.pack()
        self.get_a_number()

    def get_a_number(self):
        self.number = randint(1,100)
        self.label.config(text = "Try to guess the number")

    def same_guess(self):
        self.gnum = int(self.entry.get())
        if self.gnum > self.number:
            self.label.config(text = "To High Try again")
        elif self.gnum < self.number:
            self.label.config(text = "To low try again")
        else:
            self.butt.config(state = DISABLED)
            self.entry.config(state = DISABLED)
            self.label.config(text = "🤩, you are right congrats.")
            self.window.after(3000, self.window.destroy)

root = Tk()
m = game(root)
root.mainloop()