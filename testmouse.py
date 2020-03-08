''' CSCI 204 P2 - Maze Solving using Recursive Algorithm
Author: Aidan Good
Have user select maze and path type to test out the recursive algorithim
'''
from mouserecursion import Mouse
from pathmouserecurssion import PMouse
from maze import Maze

maze = Maze()

# Input name of maze file
f_name = input( "\nEnter the name of the maze file \n(leave blank if " \
		     + "you wish to generate a random maze): ")
print( f_name )

# Try to read file. Generate random file if it fails to read.
try:
    maze.read_maze( f_name )
except:
    print('-------- Could not open file --------')
    print('-------- Generating Random Maze--------')
    pass

# Show user the maze, and ask for start and end tiles
print( '-------- The Original Maze --------' )
print( maze )

starting_row = int( input( 'Please enter the starting row : ' ) )
starting_col = int( input( 'Please enter the starting column : ' ) )

exit_row = int( input( 'Please enter the exiting row : ' ) )
exit_col = int( input( 'Please enter the exiting column : ' ) )


# Ask the user what type of path markers they would like
print("\nThe default path marker is '!'")
path_type = input("\nTo have the steps be numbered instead, type in 'numpath'."\
                   + "\nOtherwise leave blank for the default path: ")

# Check if user wanted to use numbered path markers
if path_type == 'numpath':
    mouse = PMouse()
    print("\n------Using numbered path------")
    print("---Steps taken are shown, leading from starting step '0' to end step---")
    mouse.find_maze_paths( maze, starting_row, starting_col, exit_row, exit_col )

# defaults to '!' markers 
else:
    mouse = Mouse()
    print("\n------Using default '!' path------")
    print('------Steps taken are shown------')
    mouse.find_maze_paths( maze, starting_row, starting_col, exit_row, exit_col )
