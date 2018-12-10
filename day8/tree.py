import sys
string = ''

with open('input.txt', 'r') as f:
    string = f.read()

def create_node(substr : str) -> int:
    headerRest = substr.split(' ', 2)
    numChildren = int(headerRest[0])
    numMetadata = int(headerRest[1])
    restOfString = headerRest[2]

    total = 0 
    for i in range(numChildren):
        result, restOfString = create_node(restOfString) 
        total += result
        
    metadataRest = restOfString.split(' ', numMetadata)
    for i in range(numMetadata):
        total += int(metadataRest[i])
    
    return total, metadataRest[len(metadataRest) - 1]

def create_node2(substr : str) -> int:
    headerRest = substr.split(' ', 2)
    numChildren = int(headerRest[0])
    numMetadata = int(headerRest[1])
    restOfString = headerRest[2]

    childrenVals = [0] * numChildren
    for i in range(numChildren):
        childrenVals[i], restOfString = create_node2(restOfString) 

    
    total = 0
    metadataRest = restOfString.split(' ', numMetadata)
    if numChildren > 0:
        for i in range(numMetadata):
            index = int(metadataRest[i]) - 1

            if index < numChildren and index >= 0 :
                total += childrenVals[index]

    else:
        for i in range(numMetadata):
            total += int(metadataRest[i])
    
    return total, metadataRest[len(metadataRest) - 1]


result = create_node2(string)
print(result[0])
