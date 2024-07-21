# Conway's Game of Life

import random,copy

WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # Create a new column.
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#') # Add a living cell
        else:
            column.append(' ') # Add a dead cell
    nextCells.append(column) # nextCells is a list of column lists.

while True:
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        print()

for x in range(WIDTH):
    for y in range(HEIGHT):
        leftCoord = (x - 1) % WIDTH
        rightCoord = (x + 1) %  WIDTH
        aboveCoord = (y - 1) % HEIGHT
        belowCoord = (y + 1) % HEIGHT
        numNeighbors = 0
        if currentCells[leftCoord][aboveCoord] == '#':
            numNeighbors += 1
        if currentCells[x][aboveCoord] == '#':
            numNeighbors += 1
        if currentCells[rightCoord][aboveCoord] == '#':
            numNeighbors += 1
        if currentCells[leftCoord][y] == '#':
            numNeighbors += 1
        if currentCells[rightCoord][y] == '#':
            numNeighbors += 1
        if currentCells[leftCoord][belowCoord] == '#':
            numNeighbors += 1
        if currentCells[x][belowCoord] == '#':
            numNeighbors += 1
        if currentCells[rightCoord][belowCoord] == '#':
            numNeighbors += 1

        if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
            nextCells[x][y] = '#'
        elif currentCells[x][y] == ' ' and numNeighbors == 3:
            nextCells[x][y] = '#'
        else:
            nextCells[x][y] = ''
    time.sleep(5)