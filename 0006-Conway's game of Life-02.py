import random
import copy
import time

WIDTH = 60
HEIGHT = 20

def create_cells():
    return [[(' ' if random.randint(0, 1) else '#') for _ in range(HEIGHT)] for _ in range(WIDTH)]

def print_cells(cells):
    for row in cells:
        print(''.join(row))
    print()

def count_neighbors(cells, x, y):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = (x + dx) % WIDTH, (y + dy) % HEIGHT
            count += cells[nx][ny] == '#'
    return count

def update_cells(cells):
    new_cells = create_cells()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            neighbors = count_neighbors(cells, x, y)
            if cells[x][y] == '#' and (neighbors == 2 or neighbors == 3):
                new_cells[x][y] = '#'
            elif cells[x][y] == ' ' and neighbors == 3:
                new_cells[x][y] = '#'
            else:
                new_cells[x][y] = ' '
    return new_cells

cells = create_cells()
while True:
    print_cells(cells)
    cells = update_cells(cells)
    time.sleep(1)  # 控制更新速度