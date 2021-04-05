import pygame
import numpy as np

pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode((height, width))

bg = 25, 25, 25
# Fill the background with the selected color
screen.fill(bg)

# Number of cells
nxC, nyC = 25, 25

# Dimensions
dimCW = width / nxC
dimCH = height / nyC

while True:
    pass