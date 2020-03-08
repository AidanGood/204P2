''' CSCI 204 P2 - Maze Solving using Recursive Algorithm
Author: Aidan Good
Using a recursive algorithim, finding and numbering all the exits to a maze.
Displays the exit path in order of the steps taken
i.e.
*******
0123456
*******
'''
from maze import Maze
import copy

class PMouse:
    def __init__(self):
        self.num_unique_exits = 1

    def find_maze_paths ( self, maze, s_row, s_col, e_row, e_col ):
        """ Function to run the recursive algorithim to find all possible exits
            out of the maze """
        
        # Make copy of maze for recursive calls 
        maze_copy = copy.deepcopy( maze )
        maze_copy.theMaze[s_row][s_col] = maze.THEWAYOUT

        # Tracking the step # while solving the maze
        counter = int(maze_copy.THEWAYOUT)
        counter += 1
        if counter == 10:
            counter = 0
        maze_copy.THEWAYOUT = str( counter )
        

        # Check to see if the exit tile is found, and return the map if it is.
        cur = [s_row, s_col]
        if cur == [e_row, e_col]:
            print('-----Unique Exit', self.num_unique_exits, 'Found----- \n')
            print( maze_copy )
            self.num_unique_exits +=1
            
        else:
            """ Check each direction to see if it is an open space. If it's open,
                recursively call find_maze_paths() to run through each
                possible path to see if the open tile leads to the exit tile."""
 
            # Look Up
            if maze_copy.is_clear(s_row - 1, s_col) == True: 
                self.find_maze_paths( maze_copy, s_row - 1, s_col, e_row, e_col )

            # Look Left
            if maze_copy.is_clear(s_row, s_col - 1) == True: 
                self.find_maze_paths( maze_copy, s_row, s_col - 1, e_row, e_col )

            # Look Down
            if maze_copy.is_clear(s_row + 1, s_col) == True: 
                self.find_maze_paths( maze_copy, s_row + 1, s_col, e_row, e_col )

            # Look Right
            if maze_copy.is_clear(s_row, s_col + 1) == True: 
                self.find_maze_paths( maze_copy, s_row, s_col + 1, e_row, e_col )

            else:
                return
