import interpreter as ipr
import fileParser as fp
import guiRenderer as gr
import threading as th
import sys

class CPU:

    # Initialize register values
    def __init__(self) -> None:

        # General Purpose
        self.rax = 0x0000
        self.rbx = 0x0000
        self.rcx = 0x0000

        # Data
        self.rdx = 0x0000

        # Stack Pointer
        self.rsp = 0x0000
        # Base Pointer
        self.rbp = 0x0000
        
        # Source Index
        self.rsi = 0x0000
        # op1ination Index
        self.rdi = 0x0000

        self.cmpResult = 0x0000


    # Reset the system to its default state
    def reset(self):

        # General Purpose
        self.rax = 0x0000
        self.rbx = 0x0000
        self.rcx = 0x0000

        # Stack Pointer
        self.rsp = 0x0000
        # Base Pointer
        self.rbp = 0x0000
        
        # Source Index
        self.rsi = 0x0000
        # Destination Index
        self.rdi = 0x0000
        
        # Data
        self.rdx = 0x0000

        self.cmpResult = 0x0000


    def printRegContents(self, line):
        print('+------------------------')
        print('|', line)
        print('| rax: ', self.rax)
        print('| rbx: ', self.rbx)
        print('| rcx: ', self.rcx)
        print('| rdx: ', self.rdx)
        print('+------------------------\n')


holdVariable = 0

def pseudoMain(filePath):
    # Temporary ASM file to debug

    lineNum = 0

    mainList = fp.parseMainFile(filePath)
    variableList = fp.parseVariables(mainList)
    labelsDict = fp.parseLabels(mainList)

    codeSize = len(mainList)

    while lineNum < codeSize:
        
        currentLineNum = lineNum

        lineNum, printStr = ipr.interpret(mainList[lineNum], lineNum, variableList, labelsDict, cpu)
        gr.updateValues(cpu, mainList[currentLineNum], printStr)

        while gr.waitForButtonClick() == False:
            continue
    
    gr.updateValues(cpu, 'Program over', '------')

    print('Program over')
    
    return
    



def main():

    if len(sys.argv) == 1:
        print('Provide file path as argument')
        print('Usage: main.py <File-Path>')
        return
    
    filePath = str(sys.argv[1])
    
    window = gr.makeMainWindow(filePath=filePath)

    everythingButGUI = th.Thread(target=pseudoMain, args=(filePath,), daemon=True)
    everythingButGUI.start()

    gr.renderWindow(window)



if __name__ == '__main__':
    # Instantiate an object
    cpu = CPU()
    main()
