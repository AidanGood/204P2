"""
  Class Maze defines a general structure of a maze
  which consists of a two-dimensional array of characters.
  Each symbol on the maze represents eiehter a possible path
  or a blocker.
 
  Students need to complete this class
"""

import random     # random number generator

class Maze:

    def __init__( self, max_row = 12, max_sol = 12 ):
        """Create a maze"""
        self.MAXROW = max_row
        self.MAXCOL = max_sol
        self.POSSIBLEPATH = ' '
        self.BLOCKER      = '*'
        self.THEWAYOUT    = '!'

        self.PATH_BLOCKER_RATIO = 0.5

        self.theMaze = self._genMaze()

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
        pass

    def get_col_size( self ):
        """Return column count"""
        pass

    def get_row_size( self ):
        """Return row count"""
        pass

    def read_maze( self, file_name ):
        """Reading maze from a file.
           The file should be in the form of a matrix, e.g.,
           ** *
           *  *
           ** *
           ** *
           would be a 4x4 input maze."""
        pass

    def get_maze( self ):
        """Return a copy of the maze"""
        pass

    def is_clear( self, row, col ):
        """Return True if this cell is clear (pathway)."""
        pass

    def is_in_maze( self, row, col ):
        """Return True if a cell is inside the maze."""
        pass

    def set_value( self, row, col, value ):
        """Set the value to a cell in the maze."""
        pass

    def get_value( self, row, col ):
        """Return the value of the current cell."""
        pass

