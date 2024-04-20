import interpreter as ipr
import fileParser as fp
import time as time

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

        

    

def main():
    # Temporary ASM file to debug
    filePath = '../asm/temp.asm'

    # start = time.time()
    gigaList = fp.parseMainFile(filePath)
    variableList = fp.parseVariables(gigaList=gigaList)
    fp.parseLabels(gigaList)
    # end = time.time()
    # print('Time taken to parse: ', end - start)

    # for line in gigaList:
    #     print(line)

    lineNum = 0
    while lineNum < len(gigaList):
        lineNum = ipr.interpret(gigaList[lineNum], lineNum, variableList, cpu)




if __name__ == '__main__':
    # Instantiate an object
    cpu = CPU()
    main()
