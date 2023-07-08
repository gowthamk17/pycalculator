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
            bd=0,
            state=tk.DISABLED
        )
        self.pastCalcBox.pack()

        # Calculator Display
        self.calcDisplay = tk.Label(
            self.root,
            height=3,
            width=100,
            bg="grey22",
            bd=0
        )
        self.calcDisplay.pack()

        # Calculator Buttons
        self.backspaceBtn = tk.Button(
            self.root,
            text="⌫"
        )
        self.backspaceBtn.grid(
            row=0,
            column=0
        )
        self.openBtn = tk.Button(
            self.root,
            text="("
        )
        self.openBtn.grid(
            row=0,
            column=1
        )
        self.clsoeBtn = tk.Button(
            self.root,
            text=")"
        )
        self.clsoeBtn.grid(
            row=0,
            column=2
        )
        self.modBtn = tk.Button(
            self.root,
            text="mod"
        )
        self.modBtn.grid(
            row=0,
            column=3
        )
        self.piBtn = tk.Button(
            self.root,
            text="Π"
        )
        self.piBtn.grid(
            row=0,
            column=4
        )