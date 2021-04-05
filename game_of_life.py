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

    for x in range(0, nxC):
        for y in range(0, nyC):
            # Create the polygon to draw
            poly = [
                (x * dimCW, y * dimCH),
                ((x + 1) * dimCW, y * dimCH),
                ((x + 1) * dimCW, (y + 1) * dimCH),
                (x * dimCW, (y + 1) * dimCH)
            ]

            pygame.draw.polygon(screen, (128, 128, 128), poly, width=1)

    pygame.display.flip()