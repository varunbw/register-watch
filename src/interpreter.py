from main import *
import time

def main():
    interpret()
    pass


'''
1 - basic
2 - macro calls
3 - function calls
4 - ignored (labels)
5 - define byte, etc.
6 - reserve byte, etc.
'''


def interpret(parsedList, instCode = 0):

    cpu = CPU()
    
    for line in parsedList:
        
        inst = ''
        
        # Basic case (ex: mov rax, rbx)
        if instCode == 0 and len(line) == 3:

            inst = line[0]
            op1 = line[1]
            op2 = line[2]

            if inst == 'mov':
                if isinstance(op1, str) and isinstance(op2, str):
                    setattr(cpu, op1, getattr(cpu, op2))
                    cpu.printRegContents(line)
                
                if isinstance(op2, int):
                    setattr(cpu, op1, op2)
                    cpu.printRegContents(line)


    
            
        
    return



if __name__ == '__main__':
    main()