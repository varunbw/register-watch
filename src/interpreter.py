import time
import constants as cnst

def main():
    pass

registerList = ['rax', 'rbx', 'rcx', 'rsp', 'rbp', 'rsi', 'rdi', 'rdx']

def interpret(line, lineNum, variableList, cpu) -> int:

    inst = ''
    
    # ! Remove this case later
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
        
        # if inst[0] == 'j':
        #     inst_jmp(line[1], line[2], cpu, variableList)



        cpu.printRegContents(line)
    
    return lineNum + 1



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

    # print(variableList[0].name)
    # print(variableList[0].value)

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
    


# def inst_jmp(op1, op2, cpu, variableList) -> None:

    
    
    
    


if __name__ == '__main__':
    main()