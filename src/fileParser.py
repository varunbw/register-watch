import time

line_iter = 0
with open('addNum.asm', 'r') as file:
    
    line_iter += 1

    for line in file:
        line = line.strip()
        words = line.split()
        if(words[0][0] == '%'):
            instruction = words[0].strip()
            var1 = words[1].strip()
            var2 = words[2].strip()
            
        elif (',' in line):
            instruction = words[0]
            comma_index = line.index(',')
            var1 = line[len(instruction) + 1:comma_index].strip()
            var2 = line[comma_index + 1:].strip()

            print("Instruction:", instruction)
            print("Variable 1:", var1)
            print("Variable 2:", var2)

            print("Press Enter to continue:")
            input()

        


        
            





'''
words = line.split()
        instruction = words[0]
        operand1 = words[1]
        operand2 = words[2]
'''      
    