import re

class VariableInfo:
    def __init__(self) -> None:

        self.name = ''
        self.type = ''
        self.value = ''
        self.isArray = False
        self.sizeOfArray = 0
    

def parseMainFile(filePath):

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


def parseVariables(gigaList):
    """
        Format of Variable List:
        +------+------+-------+--------+---------------+
        | Name | Type | Value | Array? | Size of array |
        +------+------+-------+--------+---------------+
        | str  | str  | str   | bool   | int           |
        +------+------+-------+--------+---------------+
    """
    variableList = list()

    currentlyInDataSection = False

    for line in gigaList:

        if len(line) == 0:
            continue
        
        if line[1] == '.data' or line[1] == '.bss':
            currentlyInDataSection = True
            continue

        elif line[1] == '.text':
            currentlyInDataSection = False
            break

        if currentlyInDataSection:
            variable = VariableInfo()
            lineStr = str()

            for ele in line:
                lineStr += str(ele)
            
            # Var Name
            variable.name = line[0]
            
            # Var Type
            dataType = re.findall('db|dw|dd|dq|resb|resw|resd|resq', lineStr)
            if len(dataType) != 0:
                variable.type = dataType[0]

                # Determine index of the datatype
                indexOfDT = lineStr.index(dataType[0])

            # Var Value
            variable.value = lineStr[indexOfDT + 2:len(lineStr)]

            # Check if array
            if len(re.findall('times', lineStr)) == 1:
                variable.isArray = True
                
                indexOfTimes = lineStr.index('times')

                sizeOfVar = re.findall('times\d', lineStr)
                if len(sizeOfVar) > 0:
                    variable.sizeOfArray = re.findall('\d', sizeOfVar[0])[0]
                
                
            else:
                variable.isArray = False

            variableList.append(variable)
    
    return variableList

    # for var in variableList:
    #     print(var.name, var.type, var.value, var.sizeOfArray, var.isArray)


def parseLabels(gigaList):
    """
        Format of label dictionary:
        Label Name : Line Number in file
    """
    labels = dict()

    for lineNum in range(len(gigaList)):
        if len(gigaList[lineNum]) != 1:
           continue

        potentialLabel = re.findall('\w+:', gigaList[lineNum][0])

        if len(potentialLabel) == 1:
            labels.update({potentialLabel[0] : lineNum})

    return labels