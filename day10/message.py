import time 
import re
import operator


seconds = 0
coords = []
velocities = []

with open('input.txt', 'r') as f:
    for line in f:
        matches = re.match(r'position=<([- ]?[0-9]+), ([- ]?[0-9]+)> velocity=<([- ]?[0-9]+), ([- ]?[0-9]+)>', line)
        coords.append((int(matches.group(1)), int(matches.group(2))))
        velocities.append((int(matches.group(3)), int(matches.group(4))))

def step(n):
    global coords, velocities
    if n == 1:
        coords = [(coords[i][0] + velocities[i][0],coords[i][1] + velocities[i][1]) for i in range(len(coords))]
    else:
        coords = [(coords[i][0] + velocities[i][0] * n, coords[i][1] + velocities[i][1] * n) for i in range(len(coords))]

    global seconds 
    seconds += n
    #print_grid()

def backstep(n):
    global coords, velocities
    for i in range(abs(n)):
        coords = list(map(operator.sub, coords, velocities))
    
    global seconds
    seconds -= n 

def print_grid(coord_x, coord_y, grid_width, grid_height):
    global coords
    global seconds 
    grid = [['X' for x in range(grid_width)] for y in range(grid_height)]

    strings = []    
    for y in range(len(grid)):
        string = ' '.join(grid[y]) 
        strings.append(string)

    print(seconds)

    minX = min(coords, key= lambda t: t[0])[0]
    maxX = max(coords, key= lambda t: t[0])[0]
    minY = min(coords, key= lambda t: t[1])[1]
    maxY = max(coords, key= lambda t: t[1])[1]
    for coord in coords:
            if coord[0] in range(coord_x, coord_x + grid_width) and coord[1] in range(coord_y, coord_y + grid_height):
                grid[coord[1] - minY][coord[0] - minX] = ' '

    strings = []    
    for y in range(len(grid)):
        string = ''.join(grid[y]) 
        strings.append(string)

    print('\n'.join(strings)) 

def measure_closeness():
    total_dist = 0 
    global coords
    for coord1 in coords:
        for coord2 in coords:
            if coord1 == coord2:
                continue
            else:
                total_dist += abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

    return total_dist
            
currentX = 0
currentY = 0
while True:
    string = input('Enter number of steps, 1 to n. "x" to leave\n')
    if string == 'x':
        break
    elif string == 'r':
        step(last)
    elif string == 'c':
        print(coords)
    elif string == 'p':
        print_grid(currentX, currentY, 30, 30)
    elif string == 'w':
        currentY += 1
        print_grid(currentX, currentY, 30, 30)
    elif string == 's':
        currentY -= 1
        print_grid(currentX, currentY, 30, 30)
    elif string == 'a':
        currentX += 1
        print_grid(currentX, currentY, 30, 30)
    elif string == 'd':
        currentX -= 1
        print_grid(currentX, currentY, 30, 30)
    
    else:
        try:
            steps = int(string)
        except:
            steps = 0 
        step(steps)
        last = steps
        
    dist = measure_closeness()
    print('seconds:', seconds, 'dist:', dist)

    
    