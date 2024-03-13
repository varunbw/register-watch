def parse():

    giga_list = []
    with open('../asm/asmFile.asm', 'r') as file:

        for line in file:

            line = line.strip()
            words = line.split()
            list_of_inputs = []

            if(words == []):
                giga_list.append('')
                continue

            if words[0] == ';':
                giga_list.append('')
                continue
            
            if ';' in line:
                semi_index = line.index(';')
                line = line[0:semi_index]
                line.strip()
                words = line.split()
                giga_list.append(words)
                continue

            while ',' in words:
                words.remove(',')

            giga_list.append(words)
            

            
    return giga_list

'''
if(words != []):
                if(words[0][0] == ';'):
                    instruction = ''

                elif (',' in line):
                    instruction = words[0].strip()
                    comma_index = line.index(',')
                    var1 = line[len(instruction) + 1:comma_index].strip()
                    var2 = line[comma_index+1:].strip()

                elif(words[0][len(words[0])-1] == ':'):
                    instruction = words[0].strip()

                elif (words[0].lower() == 'syscall'):
                    instruction = 'syscall'

                elif(words[0].lower() == '%macro'):
                    instruction = words[0].strip()
                    var1 = words[1].strip()
                    var2 = words[2].strip()
                        
                elif(words[0].lower() == '%endmacro'):
                    instruction = words[0].strip()

                elif(words[0].lower() == 'section'):
                    instruction = words[0].strip()
                    var1 = words[1].strip()

                elif(words[0].lower() == 'global'):
                    instruction = words[0].strip()
                    var1 = words[1].strip()


                elif(words[0].lower().startswith('buffer')):
                    instruction = words[0].strip()
                    var1 = words[1].strip()
                    var2 = words[2].strip()

                elif(words[1].lower() == 'equ'):
                    instruction = words[0].strip()
                    var1 = words[1].strip()
                    var2 = words[2].strip()

                elif(words[1].lower().startswith('res')):
                    instruction = words[0].strip()
                    var1 = words[1].strip()
                    var2 = words[2].strip()


                elif(words[1].lower().startswith('d')):
                    d_index = line.index(words[1])
                    instruction = line[0:d_index].strip()
                    var1 = words[1].strip()
                    var2 = line[d_index+2:].strip()

                elif (words[len(words)-2].lower() == 'db' or 'dt' or 'dq' or 'dd' or 'dw'):
                    d_index = line.index(words[len(words)-2])
                    instruction = line[0:d_index].strip()
                    var1 = words[len(words)-2]
                    var2 = line[d_index+2:].strip()

                
                    
                list_of_inputs.append(instruction)
                list_of_inputs.append(var1)
                list_of_inputs.append(var2)
                    

                giga_list.append(list_of_inputs)

            else:
                instruction = ''
                list_of_inputs.append(instruction)
                list_of_inputs.append(var1)
                list_of_inputs.append(var2)

                giga_list.append(list_of_inputs)

'''