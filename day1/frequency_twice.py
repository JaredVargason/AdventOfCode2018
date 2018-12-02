changes = []
with open("input1.txt") as input1:
    for line in input1:
        changes.append(int(line))

currentFrequency = 0
seenFrequencies = [0]

found = False

#brute force solution. whenever a new value is found, add it to the list.
#on this input, it took 3-4 minutes to find the solution on my chromebook

while(not found):
    for change in changes:
        currentFrequency += change
        if currentFrequency in seenFrequencies:
            found = True

        seenFrequencies.append(currentFrequency)

print(currentFrequency) 