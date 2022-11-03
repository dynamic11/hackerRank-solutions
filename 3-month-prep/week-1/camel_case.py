import sys

STR_START_INDEX=4

def capitalizeAndSpaceOutWords(stringList):
    for index, letter in enumerate(stringList):
        if letter.isupper():
            stringList[index]=stringList[index].lower()
            if(index>0):
                stringList.insert(index,' ')
    
    return stringList

def capitalizeAndMergeWords(stringList):
    for index, letter in enumerate(stringList):
        if letter==' ':
            stringList[index+1]=stringList[index+1].upper()
            stringList.pop(index)
    
    return stringList

def capitalizeFirstLetter(stringList):
    stringList[0]=stringList[0].upper()
    return stringList
    
def removeMethodBrackets(stringList):
    del stringList[len(stringList)-2:]
    return stringList

def addMethodBrackets(stringList):
    stringList.extend(['(', ')'])
    return stringList

if __name__ == '__main__':

    for line in sys.stdin:
        cleanString = line.strip('\n').strip('\r')
        stringToEdit = list(cleanString[STR_START_INDEX:])
        
        if line[0]=='S':
            if(line[2]=='M'):
                stringToEdit = removeMethodBrackets(stringToEdit)
                
            stringToEdit = capitalizeAndSpaceOutWords(stringToEdit)
                         
        elif line[0]=='C':
            if line[2]=='C':
                stringToEdit = capitalizeFirstLetter(stringToEdit)
            elif(line[2]=='M'):
                stringToEdit = addMethodBrackets(stringToEdit)
                
            stringToEdit = capitalizeAndMergeWords(stringToEdit)         
            
    
        print(''.join(stringToEdit))
                    