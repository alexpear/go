#!/usr/bin/python

from app import App
from gamestate import Gamestate

class GoGame(App):
  # Go commands
  def drawGrid(self, params=[]):
    print 'pretend this sentence is a gameboard.'

  # put(['[4,3]', 'w'])
  def put(self, params=[]):
    # TODO this function needs asserts.

    # self.gamestate.put

  def makeInputMap(self):
    return {
      'ls': self.drawGrid,
      'put': self.put
    }

  def __init__(self):
    App.__init__(self)
    self.inputMap.update(self.makeInputMap())
    self.gamestate = Gamestate()

# for testing
game = GoGame()
game.ui()
