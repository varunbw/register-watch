import customtkinter as ctk

buttonClicked = False
fontUsed = 'Consolas Monospace'


def buttonClick():
    global buttonClicked
    buttonClicked = True
    return

    
def stopProg(root):
    root.quit()
    root.destroy()


class MainWindow:
    def __init__(self) -> None:

        self.root = ctk.CTk()
        self.leftFrame = ctk.CTkFrame(master=self.root)
        self.rightFrame = ctk.CTkFrame(master=self.root)
        
        self.codeTitle = ctk.CTkLabel(master=self.leftFrame, text="ASM Code", font=(fontUsed, 24))

        self.actualCode = ctk.CTkTextbox(master=self.leftFrame, wrap="word", font=(fontUsed, 24))

        self.registerTitle = ctk.CTkLabel(master=self.rightFrame, text="Register  New   Old",font=(fontUsed, 24))

        # Register frames
        self.raxFrame = ctk.CTkFrame(master=self.rightFrame)
        self.rbxFrame = ctk.CTkFrame(master=self.rightFrame)
        self.rcxFrame = ctk.CTkFrame(master=self.rightFrame)
        self.rdxFrame = ctk.CTkFrame(master=self.rightFrame)
        self.rspFrame = ctk.CTkFrame(master=self.rightFrame)
        self.rbpFrame = ctk.CTkFrame(master=self.rightFrame)
        self.rsiFrame = ctk.CTkFrame(master=self.rightFrame)
        self.rdiFrame = ctk.CTkFrame(master=self.rightFrame)
    
    
        # The corresponding values inside above frames
        self.raxLabel = ctk.CTkLabel(master=self.raxFrame, font=(fontUsed, 24))
        self.rbxLabel = ctk.CTkLabel(master=self.rbxFrame, font=(fontUsed, 24))
        self.rcxLabel = ctk.CTkLabel(master=self.rcxFrame, font=(fontUsed, 24))
        self.rdxLabel = ctk.CTkLabel(master=self.rdxFrame, font=(fontUsed, 24))
        self.rspLabel = ctk.CTkLabel(master=self.rspFrame, font=(fontUsed, 24))
        self.rbpLabel = ctk.CTkLabel(master=self.rbpFrame, font=(fontUsed, 24))
        self.rsiLabel = ctk.CTkLabel(master=self.rsiFrame, font=(fontUsed, 24))
        self.rdiLabel = ctk.CTkLabel(master=self.rdiFrame, font=(fontUsed, 24))
        

        self.printFrame = ctk.CTkFrame(master=self.rightFrame, width=100)
        self.printLabel = ctk.CTkLabel(master=self.printFrame, text='...', width=100, font=(fontUsed, 24))

        self.currentLineFrame = ctk.CTkFrame(master=self.leftFrame)
        self.currentLine = ctk.CTkLabel(master=self.currentLineFrame, text='Current Line:\nlorem ipsum', font=(fontUsed, 24))
        

        self.stepButton = ctk.CTkButton(master=self.rightFrame, text="Step", command=buttonClick)
        pass


window = MainWindow()


def makeMainWindow(filePath) -> MainWindow:
    
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    
    window.root.geometry("960x540")

    program_code = ''

    with open(filePath, "r") as file:
        program_code = file.read()
            
    # Left side of window, contains code
    window.leftFrame.pack(side="left", pady=12, padx=10, fill="both", expand=True)

    # Right side of window, contains register contents
    window.rightFrame.pack(side="right", pady=12, padx=10, fill="both", expand=True)

    # Label for cod, font=(fontUsed, 24)e
    window.codeTitle.pack(pady=12, padx=10)

    # Label for ASM Cod, font=(fontUsed, 24)e
    window.actualCode.insert("1.0", program_code)
    window.actualCode.pack(expand=True, fill="both")

    # Label for reg content, font=(fontUsed, 24)s
    window.registerTitle.pack(pady=12, padx=10)
    
    window.raxFrame.pack(pady=5, padx=5)
    window.rbxFrame.pack(pady=5, padx=5)
    window.rcxFrame.pack(pady=5, padx=5)
    window.rdxFrame.pack(pady=5, padx=5)
    window.rspFrame.pack(pady=5, padx=5)
    window.rbpFrame.pack(pady=5, padx=5)
    window.rsiFrame.pack(pady=5, padx=5)
    window.rdiFrame.pack(pady=5, padx=5)

    # Label for registers
    window.raxLabel.pack(pady=5, padx=5,)
    window.rbxLabel.pack(pady=5, padx=5,)
    window.rcxLabel.pack(pady=5, padx=5,)
    window.rdxLabel.pack(pady=5, padx=5,)
    window.rspLabel.pack(pady=5, padx=5,)
    window.rbpLabel.pack(pady=5, padx=5,)
    window.rsiLabel.pack(pady=5, padx=5,)
    window.rdiLabel.pack(pady=5, padx=5,)

    # Button to move forward
    # window.stepButton.bind('<Button-1>', buttonClick)
    window.stepButton.pack(side="bottom")

    # Printing values
    window.printFrame.pack(expand=True)
    window.printLabel.pack(expand=True)

    # Current line
    window.currentLineFrame.pack()
    window.currentLine.pack()

    return window


def renderWindow(window):
    window.root.mainloop()


def waitForButtonClick():

    global buttonClicked
    
    if buttonClicked == False:
        return False
    else:
        buttonClicked = False
        return True



def updateValues(cpu, oldCPU, lineList, toPrint):

    registerContents_New = {
        'rax': 0,
        'rbx': 0,
        'rcx': 0,
        'rdx': 0,
        'rsp': 0,
        'rbp': 0,
        'rsi': 0,
        'rdi': 0
    }

    # Get values from CPU
    for key in registerContents_New.keys():
        registerContents_New[key] = getattr(cpu, key)


    registerContents_Old = {
        'rax': 0,
        'rbx': 0,
        'rcx': 0,
        'rdx': 0,
        'rsp': 0,
        'rbp': 0,
        'rsi': 0,
        'rdi': 0
    }

    # Get values from old CPU
    for key in registerContents_Old.keys():
        registerContents_Old[key] = getattr(oldCPU, key)

    line = "Current Line\n"
    for ele in lineList:
        line += " " + str(ele)
	
    window.currentLine.configure(text = str(line))

    window.raxLabel.configure(text = "rax  |   " + str(registerContents_New['rax']) + "  |  " + str(registerContents_Old['rax']))
    window.rbxLabel.configure(text = "rbx  |   " + str(registerContents_New['rbx']) + "  |  " + str(registerContents_Old['rbx']))
    window.rcxLabel.configure(text = "rcx  |   " + str(registerContents_New['rcx']) + "  |  " + str(registerContents_Old['rcx']))
    window.rdxLabel.configure(text = "rdx  |   " + str(registerContents_New['rdx']) + "  |  " + str(registerContents_Old['rdx']))
    window.rspLabel.configure(text = "rsp  |   " + str(registerContents_New['rsp']) + "  |  " + str(registerContents_Old['rsp']))
    window.rbpLabel.configure(text = "rbp  |   " + str(registerContents_New['rbp']) + "  |  " + str(registerContents_Old['rbp']))
    window.rsiLabel.configure(text = "rsi  |   " + str(registerContents_New['rsi']) + "  |  " + str(registerContents_Old['rsi']))
    window.rdiLabel.configure(text = "rdi  |   " + str(registerContents_New['rdi']) + "  |  " + str(registerContents_Old['rdi']))

    window.printLabel.configure(text = "stdout\n" + str(toPrint))

    window.root.update()