import time 
import re
import operator

currentX = 0
currentY = 0
last = '' 
step = 20
grid_height = 30
grid_width = 30

seconds = 0
coords = []
velocities = []

with open('input.txt', 'r') as f:
    for line in f:
        matches = re.match(r'position=<([- ]?[0-9]+), ([- ]?[0-9]+)> velocity=<([- ]?[0-9]+), ([- ]?[0-9]+)>', line)
        coords.append((int(matches.group(1)), int(matches.group(2))))
        velocities.append((int(matches.group(3)), int(matches.group(4))))

def step_forward(n):
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

    for coord in coords:
        if coord[0] in range(coord_x, coord_x + grid_width) and coord[1] in range(coord_y, coord_y + grid_height):
            try:
                grid[coord[1] - coord_y][coord[0] - coord_x] = ' '
            
            except:
                pass

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

while True:
    command = input('Enter (s)teps, (c)oordinates, (p)rint current grid, (wsad) move the map, (r)edo last command, 1 to n. "x" to leave\n')
    if command == 'x':
        break
    elif command == 'r':
        step_forward(last)
    elif command == 'c':
        print(coords)
    elif command == 'p':
        print_grid(currentX, currentY, 30, 30)
    elif command == 'w':
        currentY += step
        print_grid(currentX, currentY, 30, 30)
    elif command == 's':
        currentY -= step 
        print_grid(currentX, currentY, 30, 30)
    elif command == 'a':
        currentX += step 
        print_grid(currentX, currentY, 30, 30)
    elif command == 'd':
        currentX -= step 
        print_grid(currentX, currentY, 30, 30)
    
    else:
        try:
            steps = int(command)
        except ValueError:
            steps = 0 
        step_forward(steps)
        last = steps
        
    dist = measure_closeness()
    print('x', currentX, currentY, )
    print('seconds:', seconds, 'dist:', dist)

    
    