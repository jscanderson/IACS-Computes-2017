import numpy as np
import matplotlib.pyplot as plt
from random import randint

'''
From Wikipedia: https://en.wikipedia.org/wiki/Conway's_Game_of_Life

The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.

The "game" is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves or, for advanced players, by creating patterns with particular properties.

The Rules of Life:

The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead. Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

  1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
  2. Any live cell with two or three live neighbours lives on to the next generation.
  3. Any live cell with more than three live neighbours dies, as if by overcrowding.
  4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

'''

# The box is [0,L] in both x and y
L = 100

# The maximum number of steps
max_steps = 100000

#The grids of step n and n+1, padded so that we can take things off screen before we terminate them
previous1 = np.zeros((L,L))
previous2 = np.zeros((L,L))
current = np.zeros((L,L))
future  = np.zeros((L,L))

# Random initial positions for 300 pixels
# Concentrating them in the center
for i in range(0,500):
    x = randint(20,L-20)
    y = randint(20,L-20)
    current[x][y] = 1

# Display initial graphics   
im = plt.imshow(current, cmap = 'Greys', interpolation = 'nearest')
im.axes.get_xaxis().set_visible(False)
im.axes.get_yaxis().set_visible(False)
plt.ion()
plt.show()

props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
box = plt.text(1,1, 'Initial Configuration. Click to start', fontsize=14, verticalalignment='top', bbox=props)
 
# Freeze image
plt.waitforbuttonpress() 
box.remove()

# Step counter
n = 0

# Play the game of Life
while 1:

    # Test if steady state has been reached (Only works for period 2 and less oscillations) or if max steps reached
    if np.array_equal(current, previous1) or np.array_equal(current,previous2) or n > max_steps:

        # Let user know we've reached steady state and are about to close
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        plt.text(1,1, 'Final Configuration. Click to exit', fontsize=14, verticalalignment='top', bbox=props)
 
        # Freeze image
        plt.waitforbuttonpress() 
  
        # Unfreezes on click and finalizes
        break

    # Update previous1 and previous2
    previous2 = np.copy(previous1)
    previous1 = np.copy(current)

    # Count the number of steps
    n += 1

    # Calculate next step
    # Clear old update
    future = np.zeros((L,L))

    # Check each cell for its living neighbors to see if it lives in the next iteration
    for i in range(0,L):
        for j in range(0,L):
            neighbors = 0
            neighbors += current[i-1][j-1] + current[i][j-1] + current[(i+1)%L][j-1] +  \
                         current[i-1][j]   +                   current[(i+1)%L][j]   +  \
                         current[i-1][(j+1)%L] + current[i][(j+1)%L] + current[(i+1)%L][(j+1)%L]
            
            #Living cell dies due to underpopulation
            if current[i][j] == 1 and neighbors < 2:
                future[i][j] = 0
            #Living cell continues living 
            elif current[i][j] == 1 and neighbors == 2 or neighbors == 3:   
                future[i][j] = 1
            #Cell dies, as if by overcrowding
            elif current[i][j] == 1 and neighbors > 3:
                future[i][j] = 0
            #Dead cell is now living, as if by reproduction
            elif current[i][j] == 0 and neighbors == 3:
                future[i][j] == 1

    # Save new step as current step    
    current = np.copy(future)

    # Update visualization of the board 
    im.set_data(current)
    plt.draw()
    plt.pause(0.01)
   
