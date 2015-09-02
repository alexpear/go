#!/usr/bin/python

import app

class GoGame(app.App):
  # Go commands
  def drawGrid(self, params=[]):
    print 'pretend this sentence is a gameboard.'

  def put(self, params=[]):
    pass

  def makeInputMap(self):
    return {
      'ls': self.drawGrid,
      'put': self.put
    }

  def __init__(self):
    app.App.__init__(self)
    self.inputMap.update(self.makeInputMap())
    # self.gamestate = gamestate.Gamestate()

# for testing
game = GoGame()
game.ui()
