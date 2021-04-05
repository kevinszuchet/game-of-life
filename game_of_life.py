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

# State of the cells
# Live = 1
# Dead = 0
state = np.zeros((nxC, nyC))

# Examples
# Stick
state[5, 3] = 1
state[5, 4] = 1
state[5, 5] = 1

# Movable
# state[21, 21] = 1
# state[22, 22] = 1
# state[22, 23] = 1
# state[21, 23] = 1
# state[20, 23] = 1

# Execution loop
while True:
    new_state = np.copy(state)
    screen.fill(bg)

    for y in range(0, nxC):
        for x in range(0, nyC):
            # Create the polygon to draw
            poly = [
                (x * dimCW, y * dimCH),
                ((x + 1) * dimCW, y * dimCH),
                ((x + 1) * dimCW, (y + 1) * dimCH),
                (x * dimCW, (y + 1) * dimCH)
            ]

            # How many closed neighbours has the cell
            n_neighbours = state[(x - 1) % nxC, (y - 1) % nyC] + \
                           state[x % nxC, (y - 1) % nyC] + \
                           state[(x + 1) % nxC, (y - 1) % nyC] + \
                           state[(x - 1) % nxC, y % nyC] + \
                           state[(x + 1) % nxC, y % nyC] + \
                           state[(x - 1) % nxC, (y + 1) % nyC] + \
                           state[x % nxC, (y + 1) % nyC] + \
                           state[(x - 1) % nxC, (y + 1) % nyC]

            # Rule 1: Died cell with 3 alive neighbours -> Live cell
            if state[x, y] == 0 and n_neighbours == 3:
                new_state[x, y] = 1

            # Rule 2: Live cell with less than 2 or more than 3 alive neighbours -> Died cell
            elif state[x, y] == 1 and (n_neighbours < 2 or n_neighbours > 3):
                new_state[x, y] = 0

            # Draw the new cell for each (x, y)
            if new_state[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, width=1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, width=0)

    # Update state
    state = np.copy(new_state)

    pygame.display.flip()
