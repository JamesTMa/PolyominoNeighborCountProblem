This program is intended as a neighbor counting tool for poly-ominos. 
It communicates neighbor counts by color coding in a minesweeper-esque manner.
This tool is intended to help solve the problem posed in this reddit thread:
https://www.reddit.com/r/gameoflife/s/7AyYxG5HDv
A green background appears when the polyomino belongs to a valid group.

Controls:

  Click on a cell to toggle it alive or dead. Space clears the grid, and P prints
  an emoji version of the current cell arrangement. 

In v3, the main things in the code that I'll highlight (which you can mess around
with) are as follows:

Lines 8 and 9: The number of blocks in the grid and their size in pixels. The current
               code assumes that the grid is square (windowSize by windowSize). If 
               you want, you could try to rework it to allow rectangular grids, but 
               I haven't bothered.
               
Line 16-25: The colors of the blocks, currently minesweeper-themed. You can tweak them
            to make them more intuitive to you. They are in RGB values from 0-255.
            
Line 111: The symmetry variable can be used to enforce symmetry in the grid.
          Specifically, it can equal:
            "d1" (for mirror symmetry like the letter A)
            "d2" (for double mirror symmetry like X)
            "c2" (for two-fold rotational symmetry like S)
            Anything else, and there will be no symmetry applied.
          Note: Other symmetries, like diagonal mirror, c4 or d4 are not yet
          implemented. Also, the evenness of windowSize decides whether the
          mirror line(s) cuts between squares or within squares.
