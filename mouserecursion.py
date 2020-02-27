''' CSCI 204 P2 - Maze Solving using Recursive Algorithm
Author: Aidan Good
'''
from maze import Maze
import copy

class Mouse:
    def __init__(self):
        pass
        

    def find_maze_paths ( self, maze, s_row, s_col, e_row, e_col ):
        
        maze_copy = copy.deepcopy( maze )
        maze_copy.theMaze[s_row][s_col] = maze.THEWAYOUT
        cur = [s_row, s_col]
        # print(cur)
        # print( maze )
        
        if cur == [e_row, e_col]:
            print('\n-----Unique Exit Found----- \n')
            print( maze_copy )

        else:
            
            # Look Up
            if maze_copy.is_clear(s_row - 1, s_col) == True: 
                # print('Above is clear')
                self.find_maze_paths( maze_copy, s_row - 1, s_col, e_row, e_col )

            # Look Left
            if maze_copy.is_clear(s_row, s_col - 1) == True: 
                # print('Left is Clear')
                self.find_maze_paths( maze_copy, s_row, s_col - 1, e_row, e_col )

            # Look Down
            if maze_copy.is_clear(s_row + 1, s_col) == True: 
                # print('Below is clear')
                self.find_maze_paths( maze_copy, s_row + 1, s_col, e_row, e_col )

            # Look Right
            if maze_copy.is_clear(s_row, s_col + 1) == True: 
                # print('Right is Clear')
                self.find_maze_paths( maze_copy, s_row, s_col + 1, e_row, e_col )

            else:
                return

        
        

            
