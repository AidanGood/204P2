from maze import Maze
import copy

class Mouse:
    def __init__(self):
        pass

    def find_maze_paths ( self, maze, s_row, s_col, e_row, e_col ):
        # maze_copy = copy.deepcopy( maze )
        
        maze_copy = copy.deepcopy( maze )
        maze_copy.theMaze[s_row][s_col] = maze.THEWAYOUT
        
        s = int(maze_copy.THEWAYOUT)
        s += 1
        if s == 10:
            s = 0
        maze_copy.THEWAYOUT = str(s)
        
        cur = [s_row, s_col]
        # print(cur)
        # print( maze )
        
        if cur == [e_row, e_col]:
            print('\n-----Unique Exit Found----- \n')
            print( maze_copy )
            self.exit_found = True
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
