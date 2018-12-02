import sys

lines = []
with open('input.txt', 'r') as f:
    for line in f:
        lines.append(line.rstrip())

for line1 in lines:
    for line2 in lines:
        differingChars = 0

        for i in range(len(line1)):
            if line1[i] != line2[i]:
                differingChars += 1
        
        if differingChars == 1:
            key = ''
            for i in range(len(line1)):
                if line1[i] == line2[i]:
                    key += line1[i]
            
            print(key)
            sys.exit()



    