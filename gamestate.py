#!/usr/bin/python

# Gamestate object for class GoGame
# Board is represented as a grid of '.', 'w', or 'b' strings

class Gamestate:
  WHITE_CHAR = 'w'
  BLACK_CHAR = 'b'
  NEUTRAL_CHAR = '.'

  def __init__(self):
    self.sideLength = 9
    self.grid = [
      [Gamestate.NEUTRAL_CHAR for c in range(self.sideLength)]
      for r in range(self.sideLength)
    ]

  def height(self):
    return len(self.grid)

  def width(self):
    return len(self.grid[0])

  def printGrid(self):
    columnIndexLine = '  c ' + ' '.join([str(c) for c in range(self.width())])
    dashesLine = 'r   ' + ' '.join(['-' for i in range(self.height())])

    print ''
    print columnIndexLine
    print dashesLine
    for r in range(self.height()):
      print str(r) + ' |',
      for c in range(self.width()):
        curChar = self.grid[r][c]
        if (curChar == Gamestate.WHITE_CHAR or
            curChar == Gamestate.BLACK_CHAR):
          print curChar,
        elif curChar == Gamestate.NEUTRAL_CHAR:
          print ' ',
        else:
          print '?',
      print '| ' + str(r)
    print dashesLine
    print columnIndexLine
    print ''

  def put(self, coord, color):
    # TODO this function needs asserts.
    self.grid[coord[0]][coord[1]] = color
