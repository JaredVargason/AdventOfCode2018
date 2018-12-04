grid = [[0 for i in range(1000)] for j in range(1000)]
    
with open('input.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        tokens = line.split(' ')
        coordToken = tokens[2]
        commaIndex = coordToken.find(',') 
        coord = (int(coordToken[0:commaIndex]), int(coordToken[commaIndex + 1:len(coordToken)-1]))
        dimToken = tokens[3]
        xIndex = dimToken.find('x')
        width = int(dimToken[0:xIndex])
        height = int(dimToken[xIndex + 1:len(dimToken)])
        
        for x in range(coord[0], coord[0] + width): 
            for y in range(coord[1], coord[1] + height):
                grid[x][y] += 1

total = 0

for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] > 1:
            total += 1

print(total)