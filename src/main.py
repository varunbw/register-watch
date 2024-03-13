import interpreter as ipr

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
        # Destination Index
        self.rdi = 0x0000


    # Reset the system to its default state
    def reset(self, reg = ''):

        # If a specific register is not passed, reset all of them
        if reg == '':
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
        
        # Else, reset only the specified register
        else:
            strToRegDict = {
                'rax' : self.rax,
                'rbx' : self.rbx,
                'rcx' : self.rcx,
                
                'rdx' : self.rdx,
                
                'rsp' : self.rsp,
                'rbp' : self.rbp,
                
                'rsi' : self.rsi,
                'rdi' : self.rdi
            }

            strToRegDict[reg] = 0x0000

        

    

def main():
    # Temporary ASM file to debug
    filePath = '../asm/asmFile.asm'

    # Instantiate an object


if __name__ == '__main__':
    cpu = CPU()
    main()