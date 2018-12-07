def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

coords = []
with open('input.txt', 'r') as f:
    for line in f:
        coord = line.rstrip().split(', ')
        
        coords.append((int(coord[0]), int(coord[1])))

minX = min(coords, key=lambda t: t[0])[0]
maxX = max(coords, key=lambda t: t[0])[0]
minY = min(coords, key=lambda t: t[1])[1]
maxY = max(coords, key=lambda t: t[1])[1]

#coord index, dist (set high for initial)
grid = [[(-1, 10000) for y in range(maxY)] for x in range(maxX)]
region_sizes = {-1: -1000}

for i, coord in enumerate(coords):
    total = 0
    for y in range(maxY):
        for x in range(maxX):
            prev_owner = grid[x][y]
            manhattan_dist = manhattan_distance(coord[0], coord[1], x, y)
            if manhattan_dist < prev_owner[1]:
                grid[x][y] = (i, manhattan_dist)
                region_sizes[prev_owner[0]] -= 1
                total += 1
            elif manhattan_dist == prev_owner[1]:
                region_sizes[prev_owner[0]] -= 1
                grid[x][y] = (-1, manhattan_dist)
    
    region_sizes[i] = total

#get rid of baddies! anyone who extends to the ends of the map at all should not be counted

for y in range(maxY):
    for x in [0, maxX - 1]:
        coord_tuple = grid[x][y]
        if coord_tuple[0] in region_sizes:
            region_sizes.pop(coord_tuple[0])

for x in range(maxX):
    for y in [0, maxY - 1]:
        coord_tuple = grid[x][y]
        if coord_tuple[0] in region_sizes:
            region_sizes.pop(coord_tuple[0])

print(max(region_sizes.items(), key= lambda t: t[1] ))

region_size = 0
for y in range(maxY):
    for x in range(maxX):
        total_dist = 0
        for coord in coords:
            total_dist += manhattan_distance(x, y, coord[0], coord[1])
        
        if total_dist < 10000:
            region_size += 1

print('region size:', region_size)