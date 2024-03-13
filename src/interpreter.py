from main import *

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

    regMap = {
        'rax' : cpu.rax,
        'rbx' : cpu.rbx,
        'rcx' : cpu.rcx,
        
        'rdx' : cpu.rdx,
        
        'rsp' : cpu.rsp,
        'rbp' : cpu.rbp,
        
        'rsi' : cpu.rsi,
        'rdi' : cpu.rdi
    }

    # Basic case (ex: mov rax, rbx)
    if instCode == 0:

        inst = parsedList[0]
        op1 = parsedList[1]
        op2 = parsedList[2]

        if inst == 'mov':
            regMap[op1] = regMap[op2]



    return



if __name__ == '__main__':
    main()