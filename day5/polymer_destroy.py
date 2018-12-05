def polymer_destroy(polymer : str):
    polymerReduced = True
    while polymerReduced:
        polymerReduced = False
        for i in range(len(polymer)- 1):
            char1 = polymer[i]
            char2 = polymer[i+1]
            if opposite_char(char1, char2):
                polymer = polymer.replace(char1 + char2, '', 1)
                polymerReduced = True
                break
            
    return polymer        

def opposite_char(char1 : str, char2 : str):
    return char1 != char2 and char1.upper() == char2.upper()

def pt1():
    with open('input.txt', 'r') as f:
        newPolymer = polymer_destroy(f.read())
        print(len(newPolymer))

def pt2():
    polymer = ''
    with open('input.txt', 'r') as f:
        polymer = f.read()

    #we know we can already reduce input to 9300ish instead of 50000
    polymer = polymer_destroy(polymer)

    smallest = len(polymer) 
    for i in range(0, 26):
        char = chr(i + ord('a'))
        newPolymer = polymer.replace(char, '')
        newPolymer = newPolymer.replace(char.upper(), '')
        newPolymer = polymer_destroy(newPolymer)

        if len(newPolymer) < smallest:
            smallest = len(newPolymer)

            
    print(smallest)
         
pt2()