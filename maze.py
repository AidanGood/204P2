"""
  Class Maze defines a general structure of a maze
  which consists of a two-dimensional array of characters.
  Each symbol on the maze represents either a possible path
  or a blocker.
 
  Students need to complete this class
"""

import random     # random number generator
import copy

class Maze:

    def __init__( self, max_row = 12, max_sol = 12 ):
        """Create a maze"""
        self.MAXROW = max_row
        self.MAXCOL = max_sol
        self.POSSIBLEPATH = ' '
        self.BLOCKER      = '*'
        self.THEWAYOUT    = '0'

        self.PATH_BLOCKER_RATIO = 0.5

        self.theMaze = self._gen_maze()

    def _gen_maze( self ):
        """Generate a random maze based on probability"""
        local_maze = [['*' for i in range( self.MAXROW )] \
                         for j in range( self.MAXCOL )]

        for row in range( self.MAXROW ):
            for col in range( self.MAXCOL ):
                threshold = random.random()
                if threshold > self.PATH_BLOCKER_RATIO:
                    local_maze[ row ][ col ] = self.POSSIBLEPATH
                else:
                    local_maze[ row ][ col ] = self.BLOCKER

        return local_maze

    def __str__( self ):
        """Generate a string representation of the maze"""
        string = ' 012345678901\n'
        i = 0
        # Add each maze 'tile' to the string individually
        for row in range( len(self.theMaze) ):
            string += str(i)
            i += 1
            if i == 10: 
                i = 0
            for col in range( len(self.theMaze[row]) ):
                string += str( self.theMaze[row][col] )
            string += '\n'
        return string

    def get_col_size( self ):
        """Return column count"""
        return self.MAXCOL

    def get_row_size( self ):
        """Return row count"""
        return self.MAXROW

    def read_maze( self, file_name ):
        """Reading maze from a file.
           The file should be in the form of a matrix, e.g.,
           ** *
           *  *
           ** *
           ** *
           would be a 4x4 input maze."""
        # Opens the file requested
        file = open( file_name, "r" )

        i = 0
        # Copy maze from the file over to self.theMaze
        for line in file:
            item = list(line) # makes list containing each 'tile' individually
            for x in range(self.MAXROW):
                self.theMaze[i][x] = item[x] 
            i += 1
            
                

    def get_maze( self ):
        """Return a copy of the maze"""
        maze_copy = copy.deepcopy( self )
        return maze_copy

    def is_clear( self, row, col ):
        """Return True if this cell is clear (pathway)."""
        if self.is_in_maze( row, col ):
            
            if self.theMaze[row][col] == self.POSSIBLEPATH:
                return True
            else:
                return False
        else:
            return False

    def is_in_maze( self, row, col ):
        """Return True if a cell is inside the maze."""
        if row < self.MAXROW:
            if col < self.MAXCOL:
                if row >= 0:
                    if col >= 0:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def set_value( self, row, col, value ):
        """Set the value to a cell in the maze."""
        if self.is_in_maze( row, col ) == True:
            self.theMaze[row][col] = value
            
    def get_value( self, row, col ):
        """Return the value of the current cell."""
        if self.is_in_maze( row, col ) == True:
            return self.theMaze[row][col]

