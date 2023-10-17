#Pygame init
import pygame
import math
import random
from copy import deepcopy
#Start up pygame
pygame.init()
pygame.font.init
pygame.display.set_caption("Path_finding_robot")

screen_width, screen_height=600, 600
center = (screen_width//2, screen_height//2)
tile_size = 10
grid_width,grid_height = screen_width//tile_size, screen_height//tile_size
blue = (0, 0, 255)
green = (0, 255, 0)



def main():

    screen = pygame.display.set_mode((screen_width, screen_height)) #Set display size
    screen.fill((255, 255, 255)) #Fill screen with background color

    grid = make_grid((64, 48))
    
    

    


    print(grid)



    #Keep pygame running
    run_flag = True
    while run_flag is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_flag = False
        pygame.display.flip()    

def map(screen):
    # Draw a map
    # Draw random colored tiles
    for x in range(grid_width):
        for y in range(grid_height):
            rand_num = random.random()  # Generate a random number between 0 and 1
            if rand_num < 0.2:
                color = (0, 0, 255)  # Blue (RGB)
            else:
                color = (0, 255, 0)  # Green (RGB)
            pygame.draw.rect(screen, color, (x * tile_size, y * tile_size, tile_size, tile_size))


def make_grid(size):
    grid = []
    for _ in range(size[0]):
            rand_num = random.random()  # Generate a random number between 0 and 1
            if rand_num < 0.2:
                grid.append(1)  # Add a None element to represent an empty cell
            grid[-1].append(0)
    return grid      
    
def grid_line(grid, start_coord, end_coord):
    assert(start_coord[0] == end_coord[0] or start_coord[1] == end_coord[1])
    grid = deepcopy(grid)
    if start_coord[1] == end_coord[1]:
        for x in range(start_coord[0], end_coord[0]+1):
            grid[start_coord[1]][x] = 1
    else:
        for y in range(start_coord[1], end_coord[1]+1):
            grid[y][start_coord[0]] = 1
    return grid


def draw_grid(screen, grid):
    block_size = 10
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if value == 1:
                pygame.draw.rect(screen, (0, 0, 0), (x*block_size, y * block_size, block_size, block_size))

if __name__ == "__main__":
    main()