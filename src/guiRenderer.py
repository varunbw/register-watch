import customtkinter as ctk
import threading as th
import main
from main import holdVariable

buttonClicked = False

def buttonClick():
    global buttonClicked
    buttonClicked = True
    return


class MainWindow:
    def __init__(self) -> None:

        self.root = ctk.CTk()
        self.leftFrame = ctk.CTkFrame(master=self.root)
        self.rightFrame = ctk.CTkFrame(master=self.root)
        
        self.codeTitleLabel = ctk.CTkLabel(master=self.leftFrame, text="ASM Code")
        self.codeLabel = ctk.CTkTextbox(master=self.leftFrame, wrap="word")

        self.registerTitleLabel = ctk.CTkLabel(master=self.rightFrame, text="Register Contents")
        
        self.raxFrame = ctk.CTkFrame(master=self.rightFrame)
        self.rbxFrame = ctk.CTkFrame(master=self.rightFrame)
        self.rcxFrame = ctk.CTkFrame(master=self.rightFrame)
        self.rdxFrame = ctk.CTkFrame(master=self.rightFrame)
        self.rspFrame = ctk.CTkFrame(master=self.rightFrame)
        self.rbpFrame = ctk.CTkFrame(master=self.rightFrame)
        self.rsiFrame = ctk.CTkFrame(master=self.rightFrame)
        self.rdiFrame = ctk.CTkFrame(master=self.rightFrame)
        

        self.raxLabel = ctk.CTkLabel(master=self.raxFrame)
        self.rbxLabel = ctk.CTkLabel(master=self.rbxFrame)
        self.rcxLabel = ctk.CTkLabel(master=self.rcxFrame)
        self.rdxLabel = ctk.CTkLabel(master=self.rdxFrame)
        self.rspLabel = ctk.CTkLabel(master=self.rspFrame)
        self.rbpLabel = ctk.CTkLabel(master=self.rbpFrame)
        self.rsiLabel = ctk.CTkLabel(master=self.rsiFrame)
        self.rdiLabel = ctk.CTkLabel(master=self.rdiFrame)
        

        self.var = ctk.IntVar()

        #self.raxFrame = ctk.CTkFrame(master=self.rightFrame)
        #self.raxLabel = ctk.CTkLabel(master=self.raxFrame, text = 'rax')

        self.stepButton = ctk.CTkButton(master=self.rightFrame, text="Click me!", command=buttonClick)
        pass


window = MainWindow()

def makeWindow() -> MainWindow:
    
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    window.root.geometry("720x540")

    program_code = ''
    filePath = "../asm/asmFile.asm"

    with open(filePath, "r") as file:
        program_code = file.read()
            
    # Left side of window, contains code
    window.leftFrame.pack(side="left", pady=12, padx=10, fill="both", expand=True)

    # Right side of window, contains register contents
    window.rightFrame.pack(side="right", pady=12, padx=10, fill="both", expand=True)

    # Label for code
    window.codeTitleLabel.pack(pady=12, padx=10)

    # Label for ASM Code
    window.codeLabel.insert("1.0", program_code)
    window.codeLabel.pack(expand=True, fill="both")

    # Label for reg contents
    window.registerTitleLabel.pack(pady=12, padx=10)
    
    window.raxFrame.pack(pady=5, padx=5)
    window.rbxFrame.pack(pady=5, padx=5)
    window.rcxFrame.pack(pady=5, padx=5)
    window.rdxFrame.pack(pady=5, padx=5)
    window.rspFrame.pack(pady=5, padx=5)
    window.rbpFrame.pack(pady=5, padx=5)
    window.rsiFrame.pack(pady=5, padx=5)
    window.rdiFrame.pack(pady=5, padx=5)

    # Label for registers
    window.raxLabel.pack(pady=5, padx=5)
    window.rbxLabel.pack(pady=5, padx=5)
    window.rcxLabel.pack(pady=5, padx=5)
    window.rdxLabel.pack(pady=5, padx=5)
    window.rspLabel.pack(pady=5, padx=5)
    window.rbpLabel.pack(pady=5, padx=5)
    window.rsiLabel.pack(pady=5, padx=5)
    window.rdiLabel.pack(pady=5, padx=5)


    # Button to move forward
    # window.stepButton.bind('<Button-1>', buttonClick)
    window.stepButton.pack(side="bottom")


    #window.raxFrame.pack(side='left', expand=False)
    #window.raxLabel.pack(pady = 10, padx = 10)

    '''
    new_values = {'rax': 10, 'rbx': 20, 'rcx': 30, 'rdx': 40, 'rsp': 50, 'rbp': 60, 'rsi': 70, 'rdi': 80}

    stringToDisplay = "\n".join([f"{reg}  =  {val}" for reg, val in new_values.items()])

    window.registerLabel.configure(text = stringToDisplay)
    '''

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



def updateValues(cpu):

    registerContents = {
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
    for key in registerContents.keys():
        registerContents[key] = getattr(cpu, key)
	
    stringToDisplay = "\n".join([f"{reg}  =  {val}" for reg, val in registerContents.items()])

    window.raxLabel.configure(text = "rax: " + str(registerContents['rax']))
    window.rbxLabel.configure(text = "rbx: " + str(registerContents['rbx']))
    window.rcxLabel.configure(text = "rcx: " + str(registerContents['rcx']))
    window.rdxLabel.configure(text = "rdx: " + str(registerContents['rdx']))
    window.rspLabel.configure(text = "rsp: " + str(registerContents['rsp']))
    window.rbpLabel.configure(text = "rbp: " + str(registerContents['rbp']))
    window.rsiLabel.configure(text = "rsi: " + str(registerContents['rsi']))
    window.rdiLabel.configure(text = "rdi: " + str(registerContents['rdi']))

    window.root.update()
