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