import time

with open('../asm/asmFile.asm', 'r') as file:
    
    for line in file:

        line = line.strip()
        words = line.split()
        instruction = ''
        var1 = ''
        var2 = ''
        if(words != []):
            if(words[0] == '%macro'):
                instruction = words[0].strip()
                var1 = words[1].strip()
                var2 = words[2].strip()
                    
            elif(words[0] == '%endmacro'):
                instruction = words[0].strip()
                var1 = None
                var2 = None

            elif(words[0] == 'section'):
                
                instruction = words[0].strip()
                var1 = words[1].strip()
                var2 = None

            elif(words[0] == 'global'):
                instruction = words[0].strip()
                var1 = words[1].strip()
                var2 = None

            elif(words[0][len(words[0])-1] == ':'):
                instruction = words[0]
                var1 = None
                var2 = None

                

            elif (',' in line):
                instruction = words[0]
                comma_index = line.index(',')
                var1 = line[len(instruction) + 1:comma_index].strip()
                var2 = line[comma_index + 1:].strip()

                
            list_of_inputs = []
            list_of_inputs.append(instruction)
            list_of_inputs.append(var1)
            list_of_inputs.append(var2)
                

            print("[Instruction, Variable 1, Variable 2]:\n", list_of_inputs)
            print("Press Enter to continue:")
            input()
        else:
            continue

        
            





'''
words = line.split()
        instruction = words[0]
        operand1 = words[1]
        operand2 = words[2]
'''      
    