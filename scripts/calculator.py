import tkinter as tk

class Calculator():
    def __init__(self):
        # window setup
        self.root = tk.Tk()
        self.root.iconphoto(False, tk.PhotoImage(file="./icon/icon.png"))
        self.root.title("Py Calculator")
        self.root.geometry("365x465")
        self.root.config(bg="grey16")
        self.root.resizable(False, False)

        # display of past calculations
        self.calcHistoryBox = tk.Text(
            self.root,
            height=5,
            bg="grey30",
            highlightbackground="grey15",
            highlightthickness=1,
            bd=0,
            state=tk.DISABLED
        )
        self.calcHistoryBox.pack()

        # Calculator Display
        self.calcDisplay = tk.Label(
            self.root,
            height=3,
            width=100,
            bg="grey22",
            bd=0,
            fg="white",
            font=("TkDefaultFont", 13),
            text="1+1"
        )
        self.calcDisplay.pack()
        self.createKeypad()

    def createKeypad(self):
        # creating Calculator Buttons
        # frame for all the buttons in keypad
        self.keypadFrame = tk.Frame(self.root, bg="grey16")
        self.keypadFrame.pack(expand=True, fill=tk.BOTH)
        self.keypadFrame.pack_configure(padx=10, pady=10)
        
        # this code is for setting the buttons grid to equal width and height for each row & column
        for i in range(5):
            self.keypadFrame.columnconfigure(i, weight=1)
            self.keypadFrame.rowconfigure(i, weight=1)
        self.keypadFrame.columnconfigure(1, weight=2)
        self.keypadFrame.columnconfigure(2, weight=2)
        self.keypadFrame.columnconfigure(4, weight=2)
        


        # list of all the keypad buttons
        self.numButtons = []

        # create all the keypad buttons and add them to the list
        self.createKeypadButtons()
        
        for button in self.numButtons:
            button.config(bg="grey26",
                            fg="white",
                            bd=0,
                            relief=tk.FLAT,
                            highlightthickness=0,
                            highlightbackground="grey26",
                            font=("TkDefaultFont", 12))
            # button.configure()

        # below color setting is for mimiking ubuntu calculator theme
        # setting orange color for equal button onlye
        self.equalBtn.config(bg="#E95420")
        # setting numbers only to slightly white background
        self.btn0.config(bg="grey36")
        self.btn1.config(bg="grey36")
        self.btn2.config(bg="grey36")
        self.btn3.config(bg="grey36")
        self.btn4.config(bg="grey36")
        self.btn5.config(bg="grey36")
        self.btn6.config(bg="grey36")
        self.btn7.config(bg="grey36")
        self.btn8.config(bg="grey36")
        self.btn9.config(bg="grey36")

    def createKeypadButtons(self):
        self.backspaceBtn = tk.Button(self.keypadFrame,text="\u232B",)
        self.backspaceBtn.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.backspaceBtn)

        self.openBtn = tk.Button(self.keypadFrame,text="(")
        self.openBtn.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.openBtn)

        self.clsoeBtn = tk.Button(self.keypadFrame,text=")")
        self.clsoeBtn.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.clsoeBtn)

        self.modBtn = tk.Button(self.keypadFrame,text="mod")
        self.modBtn.grid(row=0, column=3, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.modBtn)

        self.piBtn = tk.Button(self.keypadFrame,text="\u03C0")
        self.piBtn.grid(row=0,column=4, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.piBtn)

        self.btn7 = tk.Button(self.keypadFrame, text="7")
        self.btn7.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.btn7)

        self.btn8 = tk.Button(self.keypadFrame, text="8")
        self.btn8.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.btn8)

        self.btn9 = tk.Button(self.keypadFrame, text="9")
        self.btn9.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.btn9)

        self.divBtn = tk.Button(self.keypadFrame, text="\u00F7")
        self.divBtn.grid(row=1, column=3, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.divBtn)

        self.sqrtBtn = tk.Button(self.keypadFrame, text="\u221A")
        self.sqrtBtn.grid(row=1, column=4, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.sqrtBtn)

        self.btn4 = tk.Button(self.keypadFrame, text="4")
        self.btn4.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.btn4)

        self.btn5 = tk.Button(self.keypadFrame, text="5")
        self.btn5.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.btn5)

        self.btn6 = tk.Button(self.keypadFrame, text="6")
        self.btn6.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.btn6)

        self.mulBtn = tk.Button(self.keypadFrame, text="\u00D7")
        self.mulBtn.grid(row=2, column=3, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.mulBtn)

        self.sqrBtn = tk.Button(self.keypadFrame, text="x\u00B2")
        self.sqrBtn.grid(row=2, column=4, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.sqrBtn)

        self.btn1 = tk.Button(self.keypadFrame, text="1")
        self.btn1.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.btn1)

        self.btn2 = tk.Button(self.keypadFrame, text="2")
        self.btn2.grid(row=3, column=1, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.btn2)

        self.btn3 = tk.Button(self.keypadFrame, text="3")
        self.btn3.grid(row=3, column=2, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.btn3)

        self.minusBtn = tk.Button(self.keypadFrame, text="\u2212")
        self.minusBtn.grid(row=3, column=3, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.minusBtn)

        self.equalBtn = tk.Button(self.keypadFrame, text="\u003D")
        self.equalBtn.grid(row=3, column=4, rowspan=2, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.equalBtn)

        self.btn0 = tk.Button(self.keypadFrame, text="0")
        self.btn0.grid(row=4, column=0, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.btn0)

        self.dotBtn = tk.Button(self.keypadFrame, text=".")
        self.dotBtn.grid(row=4, column=1, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.dotBtn)

        self.percentBtn = tk.Button(self.keypadFrame, text="\u0025")
        self.percentBtn.grid(row=4, column=2, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.percentBtn)

        self.plusBtn = tk.Button(self.keypadFrame, text="\u002B")
        self.plusBtn.grid(row=4, column=3, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.plusBtn)
