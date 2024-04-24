import constants as cnst

def main():
    pass

registerList = ['rax', 'rbx', 'rcx', 'rsp', 'rbp', 'rsi', 'rdi', 'rdx']

def interpret(line, lineNum, variableList, labelsList, cpu) -> int:

    inst = ''
    toPrint = ''
    
    # Basic case (ex: mov rax, rbx)
    if len(line) == 3:

        inst = line[0]

        if inst == 'mov':
            inst_mov(line[1], line[2], cpu, variableList)

        if inst == 'add':
            inst_add(line[1], line[2], cpu, variableList)
        
        if inst == 'sub':
            inst_sub(line[1], line[2], cpu, variableList)

        if inst == 'mul':
            inst_mul(line[1], line[2], cpu, variableList)
        
        if inst == 'cmp':
            inst_cmp(line[1], line[2], cpu, variableList)
    

    # jump instructions
    elif len(line) == 2:

        inst = line[0]
        
        # all forms of jump
        if inst[0] == 'j':
            retVal = inst_jmp(line[0], line[1], labelsList, cpu.cmpResult)

            if retVal == -1:
                return line + 1
            else:
                return retVal
    
    # syscall + others
    elif len(line) == 1:
        
        inst = line[0]

        if inst == 'syscall':
            print('here')
            toPrint = handleSyscall(cpu)
                

    cpu.printRegContents(line)
    
    return lineNum + 1, toPrint



# -- mov
def inst_mov(op1, op2, cpu, variableList) -> None:

    if isinstance(op1, str) and isinstance(op2, str):
        
        # mov reg, reg
        if op1 in registerList and op2 in registerList:
            setattr(cpu, op1, getattr(cpu, op2))
        
        # mov reg, var
        if op1 in registerList:
            for var in variableList:
                if op2 == var.name:
                    print('val: ', var.value)
                    setattr(cpu, op1, var.value)
        
        # mov var, reg
        if op2 in registerList:
            for var in variableList:
                if op1 == var.name:
                    var.value = getattr(cpu, op2)
        
    # mov reg, const
    elif isinstance(op2, int):
        setattr(cpu, op1, op2)

    return



# -- add
def inst_add(op1, op2, cpu, variableList) -> None:

    if isinstance(op1, str) and isinstance(op2, str):
        
        # add reg, reg
        if op1 in registerList and op2 in registerList:
            result = int((getattr(cpu, op1))) + int(getattr(cpu, op2))
        
        # add reg, var
        if op1 in registerList:
            for var in variableList:
                if op2 == var.name:
                    result = int(getattr(cpu, op1)) + int(var.value)
                    
        if result <= cnst.INT64_MAX:
            setattr(cpu, op1, result)
        else:
            setattr(cpu, op1, result - cnst.OVERFLOW_CORRECTION)

    
    # add reg, const
    elif isinstance(op2, int):
        result = int(getattr(cpu, op1)) + op2

        if result <= cnst.INT64_MAX:
            setattr(cpu, op1, result)
        else:
            setattr(cpu, op1, result - cnst.OVERFLOW_CORRECTION)
    
    return



# -- sub
def inst_sub(op1, op2, cpu, variableList) -> None:

    if isinstance(op1, str) and isinstance(op2, str):
        
        # sub reg, reg
        if op1 in registerList and op2 in registerList:
            result = int((getattr(cpu, op1))) - int(getattr(cpu, op2))
        
        # sub reg, var
        if op1 in registerList:
            for var in variableList:
                if op2 == var.name:
                    result = int(getattr(cpu, op1)) - int(var.value)
                    
        if result <= cnst.INT64_MAX:
            setattr(cpu, op1, result)
        else:
            setattr(cpu, op1, result - cnst.OVERFLOW_CORRECTION)
        
    
    # sub reg, const
    elif isinstance(op2, int):
        val_op1 = int(getattr(cpu, op1))
        setattr(cpu, op1, val_op1 - op2)
    
    return



# -- mul
def inst_mul(op1, op2, cpu, variableList) -> None:

    if isinstance(op1, str) and isinstance(op2, str):
        
        # mul reg, reg
        if op1 in registerList and op2 in registerList:
            result = int((getattr(cpu, op1))) * int(getattr(cpu, op2))
        
        # mul reg, var
        if op1 in registerList:
            for var in variableList:
                if op2 == var.name:
                    result = int(getattr(cpu, op1)) * int(var.value)
                    
        if result <= cnst.INT64_MAX:
            setattr(cpu, op1, result)
        else:
            setattr(cpu, op1, result - cnst.OVERFLOW_CORRECTION)
    
    # mul reg, const
    elif isinstance(op2, int):
        val_op1 = int(getattr(cpu, op1))
        setattr(cpu, op1, val_op1 * op2)
    
    return



# -- cmp
def inst_cmp(op1, op2, cpu, variableList) -> None:

    if isinstance(op1, str) and isinstance (op2, str):

        # cmp reg, reg
        if op1 in registerList and op2 in registerList:
            val1 = getattr(cpu, op1)
            val2 = getattr(cpu, op2)

        # cmp reg, value
        elif op1 in registerList:
            val1 = getattr(cpu, op1)
            for var in variableList:
                if op2 == var.name:
                    val2 = var.value
        
    # cmp reg, const
    elif isinstance(op2, int):
        val1 = getattr(cpu, op1)
        val2 = int(op2)


    if val1 == val2:
        cpu.cmpResult = 0
    else:
        cpu.cmpResult = val1 - val2

    return
    

# -- jmp
def inst_jmp(inst, op1, labelsDict, cmpValue) -> int:

    match inst:
        case 'jmp':
            return labelsDict[op1]
        
        case 'jbe':
            if cmpValue <= 0:
                return labelsDict[op1]
            else:
                return -1
        
        case 'jb':
            if cmpValue < 0:
                return labelsDict[op1]
            else:
                return -1
            
        case 'jae':
            if cmpValue >= 0:
                return labelsDict[op1]
            else:
                return -1
            
        case 'ja':
            if cmpValue > 0:
                return labelsDict[op1]
            else:
                return -1
        
        case 'je':
            if cmpValue == 0:
                return labelsDict[op1]
            else:
                return -1
        
    return -1
    


def handleSyscall(cpu) -> str:

    # Printing
    if cpu.rax == 1 and cpu.rdi == 1:
        # print('Print: {}\n'.format(cpu.rsi))
        return str(cpu.rsi)
    
    # Input
    elif cpu.rax == 0 and cpu.rdi == 0:
        cpu.rsi = int(input('Enter: '))

    return
    


if __name__ == '__main__':
    main()