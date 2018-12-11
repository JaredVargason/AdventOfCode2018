GRID_SIZE = 300
GRID_SERIAL_NUMBER = 8444
WINDOW_WIDTH = 3

grid = [[y for y in range(GRID_SIZE)] for x in range(GRID_SIZE)]

def calculate_power_level(x, y):
    rackId = x + 1 + 10   
    powerLevel = rackId * (y + 1)
    powerLevel += GRID_SERIAL_NUMBER 
    powerLevel *= rackId
    powerLevel = int(str(powerLevel)[::-1][2])
    powerLevel -= 5
    
    return powerLevel

for y in range(GRID_SIZE):
    for x in range(GRID_SIZE):
        grid[x][y] = calculate_power_level(x,y)

for WINDOW_WIDTH in range(2, 301):
    maxPower = 0
    maxX = maxY = 0 
    for y in range(0, GRID_SIZE-WINDOW_WIDTH + 1):
        for x in range(0, GRID_SIZE-WINDOW_WIDTH + 1):
            total = 0
            for i in range(0, WINDOW_WIDTH):
                for j in range(0, WINDOW_WIDTH):
                    total += grid[x+i][y+j]
            if total > maxPower:
                maxPower = total
                maxX = x
                maxY = y
        
    print('coord:', (maxX + 1, maxY + 1), 'window width:', WINDOW_WIDTH, 'max:', maxPower)