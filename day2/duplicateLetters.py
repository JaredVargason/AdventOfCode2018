twoLetterCount = threeLetterCount = 0
orda = ord('a')

with open('input.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        letterCount = [0] * 26

        twoIncluded = False
        threeIncluded = False

        for char in line:

            index = ord(char) - orda
            letterCount[index] += 1

        for i in range(len(letterCount)):
            if letterCount[i] == 2 and not twoIncluded:
                twoLetterCount += 1
                twoIncluded = True
            elif letterCount[i] == 3 and not threeIncluded:
                threeLetterCount += 1
                threeIncluded = True
    
print(twoLetterCount * threeLetterCount)
print(twoLetterCount, threeLetterCount)