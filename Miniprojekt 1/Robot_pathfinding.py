#Pygame init
import pygame
import math
import random
#Start up pygame
pygame.init()
pygame.font.init
pygame.display.set_caption("Path_finding_robot")

screen_witdh, screen_height=600, 600
center = (screen_witdh//2, screen_height//2)
tile_size = 10
grid_width,grid_height = screen_witdh//tile_size, screen_height//tile_size
blue = (0, 0, 255)
green = (0, 255, 0)



def main():

    screen = pygame.display.set_mode((screen_witdh, screen_height)) #Set display size
    screen.fill((255, 255, 255)) #Fill screen with background color

    map(screen)










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


main()