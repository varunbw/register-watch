def parse(filePath):

    gigaList = []

    with open(filePath) as file:

        for line in file:

            # Parse each item of the line
            parsedLine = line.strip().split()

            # Empty line
            if parsedLine == []:
                gigaList.append('')
                continue
            
            # Comment
            if parsedLine[0] == ';':
                gigaList.append('')
                continue
            
            # Comment after normal instruction
            if ';' in line:
                semi_index = line.index(';')
                line = line[0:semi_index]
                line.strip()
                parsedLine = line.split()
            
            finalParsedLine = list()
            
            # Remove all commas
            for item in parsedLine:
                if ',' in item:
                    item = item.replace(',', '')
                if item.isnumeric():
                    item = int(item)
                finalParsedLine.append(item)
                    
            gigaList.append(finalParsedLine)
            
    return gigaList

'''
if(parsedLine != []):
                if(parsedLine[0][0] == ';'):
                    instruction = ''

                elif (',' in line):
                    instruction = parsedLine[0].strip()
                    comma_index = line.index(',')
                    var1 = line[len(instruction) + 1:comma_index].strip()
                    var2 = line[comma_index+1:].strip()

                elif(parsedLine[0][len(parsedLine[0])-1] == ':'):
                    instruction = parsedLine[0].strip()

                elif (parsedLine[0].lower() == 'syscall'):
                    instruction = 'syscall'

                elif(parsedLine[0].lower() == '%macro'):
                    instruction = parsedLine[0].strip()
                    var1 = parsedLine[1].strip()
                    var2 = parsedLine[2].strip()
                        
                elif(parsedLine[0].lower() == '%endmacro'):
                    instruction = parsedLine[0].strip()

                elif(parsedLine[0].lower() == 'section'):
                    instruction = parsedLine[0].strip()
                    var1 = parsedLine[1].strip()

                elif(parsedLine[0].lower() == 'global'):
                    instruction = parsedLine[0].strip()
                    var1 = parsedLine[1].strip()


                elif(parsedLine[0].lower().startswith('buffer')):
                    instruction = parsedLine[0].strip()
                    var1 = parsedLine[1].strip()
                    var2 = parsedLine[2].strip()

                elif(parsedLine[1].lower() == 'equ'):
                    instruction = parsedLine[0].strip()
                    var1 = parsedLine[1].strip()
                    var2 = parsedLine[2].strip()

                elif(parsedLine[1].lower().startswith('res')):
                    instruction = parsedLine[0].strip()
                    var1 = parsedLine[1].strip()
                    var2 = parsedLine[2].strip()


                elif(parsedLine[1].lower().startswith('d')):
                    d_index = line.index(parsedLine[1])
                    instruction = line[0:d_index].strip()
                    var1 = parsedLine[1].strip()
                    var2 = line[d_index+2:].strip()

                elif (parsedLine[len(parsedLine)-2].lower() == 'db' or 'dt' or 'dq' or 'dd' or 'dw'):
                    d_index = line.index(parsedLine[len(parsedLine)-2])
                    instruction = line[0:d_index].strip()
                    var1 = parsedLine[len(parsedLine)-2]
                    var2 = line[d_index+2:].strip()

                
                    
                list_of_inputs.append(instruction)
                list_of_inputs.append(var1)
                list_of_inputs.append(var2)
                    

                gigaList.append(list_of_inputs)

            else:
                instruction = ''
                list_of_inputs.append(instruction)
                list_of_inputs.append(var1)
                list_of_inputs.append(var2)

                gigaList.append(list_of_inputs)

'''