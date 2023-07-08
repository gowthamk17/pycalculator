import tkinter as tk
import math

class Calculator():
    # color codes for the application
    ORANGE = "#eb6536"
    COOL_GREY = "#333333"
    LIGHT_GREY = "#474747"
    MID_GREY = "#3d3d3d"
    WARM_GREY = "#AEA79F"
    LIGHT_BTN = "#555555"
    DARK_BTN = "#404040"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    RESET = "\033[0m"

    def __init__(self):
        # window setup
        self.root = tk.Tk()
        self.root.iconphoto(False, tk.PhotoImage(file="./icon/icon.png"))
        self.root.title("Py Calculator")
        self.root.geometry("375x470")
        self.root.config(bg=self.COOL_GREY)
        self.root.resizable(False, False)

        # display of past calculations
        self.calcHistoryBox = tk.Frame(self.root)
        self.calcHistoryBox.pack(fill="both", expand=True)
        # disalbling auto resizing for taking constant space
        self.calcHistoryBox.pack_propagate(False)

        # creating canvas scrollable behavious the labels will be added to canvas
        self.hsCanvas = tk.Canvas(self.calcHistoryBox, 
                                    bg=self.LIGHT_GREY,
                                    highlightthickness=1,
                                    highlightbackground=self.LIGHT_GREY,
                                    bd=0)
        self.hsCanvas.pack(fill="both", expand=True)

        # Calculator Display
        self.calcDisplay = tk.Frame(self.root)
        self.calcDisplay.pack()
        
        self.evalDisplay = tk.Label(
            self.calcDisplay,
            width=100,
            bg=self.MID_GREY,
            highlightbackground=self.MID_GREY,
            highlightthickness=1,
            bd=0,
            fg="white",
            font=("TkDefaultFont", 14),
            anchor="nw",
            padx=16,
            pady=8
        )
        self.evalDisplay.pack()

        self.malCalcLabel = tk.Label(self.calcDisplay,
                                width=100,
                                bg=self.MID_GREY,
                                highlightbackground=self.MID_GREY,
                                highlightthickness=1,
                                bd=0,
                                fg="white",
                                font=("TkDefaultFont", 10),
                                anchor="nw",
                                padx=10,
                                pady=5)
        self.malCalcLabel.pack()

        self.createKeypad()

    def createKeypad(self):
        # creating Calculator Buttons
        # frame for all the buttons in keypad
        self.keypadFrame = tk.Frame(self.root, bg=self.COOL_GREY)
        self.keypadFrame.pack(expand=True, fill=tk.BOTH)
        self.keypadFrame.pack_configure(padx=10, pady=10)
        
        # this code is for setting the buttons grid to equal width and height for each row & column
        for i in range(5):
            self.keypadFrame.grid_columnconfigure(i, weight=1, uniform="row")
            self.keypadFrame.grid_rowconfigure(i, weight=1, uniform="column")  

        # list of all the keypad buttons
        self.numButtons = []

        # create all the keypad buttons and add them to the buttons list
        self.createKeypadButtons()
        
        for button in self.numButtons:
            button.config(bg="grey26",
                            fg="white",
                            bd=0,
                            relief=tk.FLAT,
                            highlightthickness=0,
                            highlightbackground="grey26")

        # below code setting is for mimiking ubuntu calculator theme
        # setting orange color for equal button onlye
        self.equalBtn.config(bg=self.ORANGE)
        # setting numbers only to slightly white background
        self.btn0.config(bg=self.LIGHT_BTN)
        self.btn1.config(bg=self.LIGHT_BTN)
        self.btn2.config(bg=self.LIGHT_BTN)
        self.btn3.config(bg=self.LIGHT_BTN)
        self.btn4.config(bg=self.LIGHT_BTN)
        self.btn5.config(bg=self.LIGHT_BTN)
        self.btn6.config(bg=self.LIGHT_BTN)
        self.btn7.config(bg=self.LIGHT_BTN)
        self.btn8.config(bg=self.LIGHT_BTN)
        self.btn9.config(bg=self.LIGHT_BTN)

    def createKeypadButtons(self):
        self.backspaceBtn = tk.Button(self.keypadFrame,
                                        text="\u232B",
                                        font=("TkDefaultFont", 7, "bold"),
                                        command=self.onBackSpace)
        self.backspaceBtn.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.backspaceBtn)

        self.openBtn = tk.Button(self.keypadFrame,
                                    text="(",
                                    font=("TkDefaultFont", 12),
                                    command=lambda: self.OperandBtnClick("("))
        self.openBtn.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.openBtn)

        self.closeBtn = tk.Button(self.keypadFrame,
                                    text=")", 
                                    font=("TkDefaultFont", 12),
                                    command=lambda: self.OperandBtnClick(")"))
        self.closeBtn.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.closeBtn)

        self.modBtn = tk.Button(self.keypadFrame,
                                    text="mod", 
                                    font=("TkDefaultFont", 10),
                                    command=lambda: self.OperandBtnClick("mod"))
        self.modBtn.grid(row=0, column=3, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.modBtn)

        self.piBtn = tk.Button(self.keypadFrame,
                                text="\u03A0",
                                font=("TkDefaultFont", 10),
                                command=lambda: self.OperandBtnClick("\u03A0"))
        self.piBtn.grid(row=0,column=4, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.piBtn)

        self.btn7 = tk.Button(self.keypadFrame, 
                                text="7",
                                font=("TkDefaultFont", 12, "bold"),
                                command=lambda: self.OperandBtnClick("7"))
        self.btn7.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.btn7)

        self.btn8 = tk.Button(self.keypadFrame, 
                                text="8", 
                                font=("TkDefaultFont", 12, "bold"),
                                command=lambda: self.OperandBtnClick("8"))
        self.btn8.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.btn8)

        self.btn9 = tk.Button(self.keypadFrame, 
                                text="9", 
                                font=("TkDefaultFont", 12, "bold"),
                                command=lambda: self.OperandBtnClick("9"))
        self.btn9.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.btn9)

        self.divBtn = tk.Button(self.keypadFrame, 
                                    text="\u00F7", 
                                    command=lambda: self.OperandBtnClick("\u00F7"))
        self.divBtn.grid(row=1, column=3, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.divBtn)

        self.sqrtBtn = tk.Button(self.keypadFrame, 
                                    text="\u221A", 
                                    command=lambda: self.OperandBtnClick("\u221A"))
        self.sqrtBtn.grid(row=1, column=4, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.sqrtBtn)

        self.btn4 = tk.Button(self.keypadFrame, 
                                text="4", 
                                font=("TkDefaultFont", 12, "bold"),
                                command=lambda: self.OperandBtnClick("4"))
        self.btn4.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.btn4)

        self.btn5 = tk.Button(self.keypadFrame, 
                                text="5", 
                                font=("TkDefaultFont", 12, "bold"),
                                command=lambda: self.OperandBtnClick("5"))
        self.btn5.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.btn5)

        self.btn6 = tk.Button(self.keypadFrame, 
                                text="6", 
                                font=("TkDefaultFont", 12, "bold"),
                                command=lambda: self.OperandBtnClick("6"))
        self.btn6.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.btn6)

        self.mulBtn = tk.Button(self.keypadFrame, 
                                    text="x", 
                                    command=lambda: self.OperandBtnClick("x"))
        self.mulBtn.grid(row=2, column=3, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.mulBtn)

        self.sqrBtn = tk.Button(self.keypadFrame, 
                                    text="x²", 
                                    command=lambda: self.OperandBtnClick("²"))
        self.sqrBtn.grid(row=2, column=4, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.sqrBtn)

        self.btn1 = tk.Button(self.keypadFrame, 
                                text="1", 
                                font=("TkDefaultFont", 12, "bold"),
                                command=lambda: self.OperandBtnClick("1"))
        self.btn1.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.btn1)

        self.btn2 = tk.Button(self.keypadFrame, 
                                text="2", 
                                font=("TkDefaultFont", 12, "bold"),
                                command=lambda: self.OperandBtnClick("2"))
        self.btn2.grid(row=3, column=1, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.btn2)

        self.btn3 = tk.Button(self.keypadFrame, 
                                text="3", 
                                font=("TkDefaultFont", 12, "bold"),
                                command=lambda: self.OperandBtnClick("3"))
        self.btn3.grid(row=3, column=2, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.btn3)

        self.minusBtn = tk.Button(self.keypadFrame, 
                                    text="-", 
                                    command=lambda: self.OperandBtnClick("-"))
        self.minusBtn.grid(row=3, column=3, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.minusBtn)

        self.equalBtn = tk.Button(self.keypadFrame, 
                                    text="\u003D", 
                                    command=self.evaluateExpression)
        self.equalBtn.grid(row=3, column=4, rowspan=2, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.equalBtn)

        self.btn0 = tk.Button(self.keypadFrame, 
                                text="0", 
                                font=("TkDefaultFont", 12, "bold"),
                                command=lambda: self.OperandBtnClick("0"))
        self.btn0.grid(row=4, column=0, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.btn0)

        self.dotBtn = tk.Button(self.keypadFrame, 
                                    text=".", 
                                    command=lambda: self.OperandBtnClick("."))
        self.dotBtn.grid(row=4, column=1, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.dotBtn)

        self.percentBtn = tk.Button(self.keypadFrame, 
                                        text="\u0025", 
                                        command=lambda: self.OperandBtnClick("\u0025"))
        self.percentBtn.grid(row=4, column=2, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.percentBtn)

        self.plusBtn = tk.Button(self.keypadFrame, 
                                    text="\u002B", 
                                    command=lambda: self.OperandBtnClick("\u002B"))
        self.plusBtn.grid(row=4, column=3, sticky="nsew", padx=2, pady=2)
        self.numButtons.append(self.plusBtn)

    def onBackSpace(self):
        self.evalDisplay.config(text="")
        self.malCalcLabel.config(text="")

    def OperandBtnClick(self, Operand):
        displaytext = self.evalDisplay["text"] + Operand
        self.evalDisplay.config(text=displaytext)

    def evaluateExpression(self):
        original_exp = self.evalDisplay["text"]
        edited_exp = original_exp.replace("Π", "3.141592654").replace("÷", "/").replace("x", "*").replace("%", "/100").replace("²", "**2").replace("mod", "%")
        if "√" in edited_exp:
            edited_exp = edited_exp.replace("√", "+math.sqrt(") + ")"
        print(self.BLUE + "Converted Expression:", edited_exp + self.BLUE)
        try:
            # First the the expression is evaluated and converted to a 
            # float number then rounding the number to 9 decimal for 
            # limiting the calculation because ubuntu calc also only 
            # calcualtes to 9 digits
            result = round(float(eval(edited_exp)), 9)
            
            resultTxt = result
            if result.is_integer():
                resultTxt = int(result)
            resultTxt = str(resultTxt)
            self.evalDisplay.config(text=resultTxt)
            print(self.GREEN + "Evaluated Result:", resultTxt + self.RESET)

            # insertint the result to history
            historyTxt = original_exp + " = " + resultTxt
            calcDataFrame = tk.Frame(self.hsCanvas, bg=self.LIGHT_GREY)
            expLabel = tk.Label(calcDataFrame, 
                        text=original_exp,
                        anchor="w",
                        justify="left",
                        bg=self.LIGHT_GREY,
                        font=("TkDefaultFont", 12),
                        fg="white",
                        padx=6,
                        pady=6)
            expLabel.pack(side=tk.LEFT)
            resultLabel = tk.Label(calcDataFrame, 
                        text=resultTxt,
                        anchor="w",
                        justify="left",
                        bg=self.LIGHT_GREY,
                        font=("TkDefaultFont", 12),
                        fg="white",
                        padx=6,
                        pady=6)
            resultLabel.pack(side=tk.RIGHT)
            eqLabel = tk.Label(calcDataFrame, 
                        text="=",
                        anchor="w",
                        justify="left",
                        bg=self.LIGHT_GREY,
                        font=("TkDefaultFont", 12),
                        fg="white",
                        padx=6,
                        pady=6)
            eqLabel.pack(side=tk.RIGHT)
            calcDataFrame.pack(expand=True, fill="x", anchor="n")
        except Exception as e:
            print(self.RED + "Expression Evaluation Failed ->", e, self.RESET,)
            self.malCalcLabel.config(text="Malformed expression")
        finally:
            print(self.YELLOW + "------------------------------" + self.RESET)
