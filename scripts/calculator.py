import tkinter as tk


class Calculator():
    def __init__(self):
        # window setup
        self.root = tk.Tk()
        self.root.iconphoto(False, tk.PhotoImage(file="./icon/icon.png"))
        self.root.title("Py Calculator")
        self.root.geometry("365x465")
        self.root.config(bg="gray20")
        self.root.resizable(False, False)

        # display of past calculations
        self.pastCalcBox = tk.Text(
            self.root,
            height=5,
            bg="grey30",
            highlightbackground="grey15",
            highlightthickness=1,
            bd=0
        )
        self.pastCalcBox.pack()

        # Calculator Display
        self.calcDisplay = tk.Label(
            self.root,
            height=3,
            width=100,
            bg="grey20"
        )
        self.calcDisplay.pack()
